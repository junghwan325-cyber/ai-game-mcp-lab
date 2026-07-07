from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ai_game_mcp_lab.repo_checks import scan_private_absolute_paths, scan_secret_like_text


class RepositoryChecks(unittest.TestCase):
    def test_no_secret_like_values(self) -> None:
        self.assertEqual([], scan_secret_like_text(ROOT))

    def test_no_private_absolute_paths(self) -> None:
        self.assertEqual([], scan_private_absolute_paths(ROOT))

    def test_sample_godot_project_has_required_files(self) -> None:
        project = ROOT / "godot" / "coin-runner"
        for rel in ["project.godot", "main.tscn", "scripts/player.gd", "scripts/game.gd"]:
            self.assertTrue((project / rel).exists(), rel)
        self.assertIn('run/main_scene="res://main.tscn"', (project / "project.godot").read_text())

    def test_sample_assets_are_small(self) -> None:
        assets = list((ROOT / "samples" / "assets").glob("*.glb"))
        self.assertTrue(assets)
        for asset in assets:
            self.assertLess(asset.stat().st_size, 2_000_000, asset)

    def test_shell_scripts_are_valid_bash(self) -> None:
        for script in (ROOT / "scripts").glob("*.sh"):
            subprocess.run(["bash", "-n", str(script)], check=True)


if __name__ == "__main__":
    unittest.main()
