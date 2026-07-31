import sys

from _pytest.capture import CaptureFixture
from _pytest.monkeypatch import MonkeyPatch

from algorithm_toolkit.main import main


def test_main_returns_success_exit_code(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "algorithm-toolkit",
            "two-sum",
            "--nums",
            "2",
            "7",
            "11",
            "15",
            "--target",
            "9",
        ],
    )

    result = main()

    captured = capsys.readouterr()

    assert result == 0
    assert "[0, 1]" in captured.out
