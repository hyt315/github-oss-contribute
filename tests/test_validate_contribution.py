"""scripts/validate_contribution.py 的测试：在临时 git 仓库里构造好/坏贡献分支。

运行：python -m unittest discover tests
"""

from __future__ import annotations

import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import validate_contribution as vc  # noqa: E402

AUTHOR = "Dev <dev@example.org>"


class ContributionTest(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.repo = pathlib.Path(self._tmp.name)
        self.git("init", "-q", "-b", "main")
        self.git("config", "user.name", "Dev")
        self.git("config", "user.email", "dev@example.org")
        # 上游已有的文件里含个人路径：不应误报，因为不是本分支新增
        (self.repo / "legacy.txt").write_text("/" + "home/alice/old\n", encoding="utf-8")
        self.git("add", ".")
        self.git("commit", "-q", "-m", "chore: init")
        self.git("update-ref", "refs/remotes/upstream/main", "HEAD")
        self.git("switch", "-q", "-c", "fix/typo")

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def git(self, *args: str) -> None:
        subprocess.run(["git", *args], cwd=self.repo, check=True, capture_output=True)

    def commit(self, name: str, content: str, message: str, signoff: bool = True) -> None:
        (self.repo / name).write_text(content, encoding="utf-8")
        self.git("add", name)
        self.git("commit", "-q", *(["-s"] if signoff else []), "-m", message)

    def test_clean_branch_passes(self) -> None:
        self.commit("a.txt", "hello\n", "fix: correct typo")
        report = vc.check(self.repo)
        self.assertEqual(report["status"], "PASS", report)
        self.assertEqual(report["warnings"], [])
        self.assertEqual(report["base"], "upstream/main")

    def test_secret_in_added_line_fails(self) -> None:
        self.commit("cfg.py", "TOKEN = '" + "gh" + "p_" + "A" * 36 + "'\n", "feat: add config")
        report = vc.check(self.repo)
        self.assertEqual(report["status"], "FAIL")
        self.assertTrue(any("cfg.py" in e for e in report["errors"]), report["errors"])

    def test_quick_skips_content_scan(self) -> None:
        self.commit("cfg.py", "TOKEN = '" + "gh" + "p_" + "A" * 36 + "'\n", "feat: add config")
        self.assertEqual(vc.check(self.repo, quick=True)["status"], "PASS")

    def test_missing_signoff_and_bad_subject_warn(self) -> None:
        self.commit("a.txt", "x\n", "update stuff", signoff=False)
        report = vc.check(self.repo)
        self.assertEqual(report["status"], "PASS")
        self.assertTrue(any(w.startswith("[DCO]") for w in report["warnings"]))
        self.assertTrue(any(w.startswith("[提交标题]") for w in report["warnings"]))

    def test_signoff_email_mismatch_warns(self) -> None:
        (self.repo / "a.txt").write_text("x\n", encoding="utf-8")
        self.git("add", "a.txt")
        self.git("commit", "-q", "-m", "fix: x\n\nSigned-off-by: Other <other@example.org>")
        report = vc.check(self.repo)
        self.assertTrue(any("不一致" in w for w in report["warnings"]), report["warnings"])

    def test_main_branch_warns(self) -> None:
        self.git("switch", "-q", "main")
        report = vc.check(self.repo)
        self.assertTrue(any(w.startswith("[分支]") for w in report["warnings"]))

    def test_not_a_repo(self) -> None:
        with tempfile.TemporaryDirectory() as empty:
            self.assertEqual(vc.main([empty]), 2)

    def test_upstream_preferred_over_stale_fork_origin(self) -> None:
        # origin/HEAD 指向落后的 Fork main，上游已有新提交（未签署、含凭据样式内容）
        self.git("update-ref", "refs/remotes/origin/main", "refs/remotes/upstream/main")
        self.git("symbolic-ref", "refs/remotes/origin/HEAD", "refs/remotes/origin/main")
        self.git("switch", "-q", "main")
        (self.repo / "up.txt").write_text("k = '" + "gh" + "p_" + "C" * 36 + "'\n", encoding="utf-8")
        self.git("add", "up.txt")
        self.git("commit", "-q", "-m", "upstream change without signoff")
        self.git("update-ref", "refs/remotes/upstream/main", "HEAD")
        self.git("switch", "-q", "-C", "fix/typo", "upstream/main")
        self.commit("a.txt", "hello\n", "fix: correct typo")
        report = vc.check(self.repo)
        self.assertEqual(report["base"], "upstream/main")
        self.assertEqual(report["status"], "PASS", report)
        self.assertEqual(report["warnings"], [])

    def test_missing_explicit_base_is_error(self) -> None:
        self.commit("a.txt", "hello\n", "fix: correct typo")
        self.assertEqual(vc.check(self.repo, "upstream/nope")["status"], "ERROR")
        self.assertEqual(vc.main([str(self.repo), "--base", "upstream/nope"]), 2)

    def test_added_line_starting_with_plus_plus_is_scanned(self) -> None:
        self.commit("文档/说明.md".replace("/", "_"), "ok\n++ " + "gh" + "p_" + "D" * 36 + "\n", "docs: add")
        report = vc.check(self.repo)
        self.assertEqual(report["status"], "FAIL", report)
        self.assertTrue(any("文档_说明.md:2:" in e for e in report["errors"]), report["errors"])

    def test_word_boundary_no_false_positive(self) -> None:
        self.commit("doc.md", "disk-encryption-configuration-settings-guide\n", "docs: add guide")
        self.assertEqual(vc.check(self.repo)["status"], "PASS")


if __name__ == "__main__":
    unittest.main()
