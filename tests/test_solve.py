import logging
from importlib import reload

import pytest
from pyroll.core import solve
from pyroll.ui import Reporter
import pyroll.freiberg_spreading


def test_solve(tmp_path, monkeypatch: pytest.MonkeyPatch, caplog):
    caplog.set_level(logging.DEBUG, logger="pyroll")

    import pyroll.ui.cli.res.input_trio as input_py
    reload(input_py)

    sequence = input_py.sequence

    solve(sequence, input_py.in_profile)

    report = Reporter()

    rendered = report.render(sequence)
    print()

    report_file = tmp_path / "report.html"
    report_file.write_text(rendered)
    print(report_file)

    print("\nLog:")
    print(caplog.text)

    assert "Geuze" not in caplog.text

    # assert "No Freiberg spreading coefficients available for Rund III" in result.output
