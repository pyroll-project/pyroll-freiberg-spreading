from pathlib import Path
from click.testing import CliRunner

import pytest

THIS_DIR = Path(__file__).parent
INPUT = (THIS_DIR / "input.py").read_text()
CONFIG = (THIS_DIR / "config.yaml").read_text()


def test_solve(tmp_path, monkeypatch: pytest.MonkeyPatch):
    from pyroll.ui.cli.program import main

    (tmp_path / "input.py").write_text(INPUT)
    (tmp_path / "config.yaml").write_text(CONFIG)

    monkeypatch.chdir(tmp_path)
    runner = CliRunner()
    result = runner.invoke(
        main,
        [
            "input-py",
            "solve",
            "report",
        ],

    )

    print("\n")
    print((tmp_path / "pyroll.log").read_text())

    print(tmp_path / 'report.html')
