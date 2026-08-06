import argparse

from _pytest.capture import CaptureFixture

from algorithm_toolkit.cli.commands import create_parser, run_command


def test_two_sum_cli_arguments() -> None:
    parser = create_parser()

    args = parser.parse_args(
        [
            "two-sum",
            "--nums",
            "2",
            "7",
            "11",
            "15",
            "--target",
            "9",
        ]
    )

    assert args.command == "two-sum"
    assert args.nums == [2, 7, 11, 15]
    assert args.target == 9


def test_find_max_cli_arguments() -> None:
    parser = create_parser()

    args = parser.parse_args(
        [
            "find-max",
            "--nums",
            "4",
            "9",
            "2",
            "7",
        ]
    )

    assert args.command == "find-max"
    assert args.nums == [4, 9, 2, 7]


def test_run_find_max_command(
    capsys: CaptureFixture[str],
) -> None:
    args = argparse.Namespace(
        command="find-max",
        nums=[4, 9, 2, 7],
    )

    exit_code = run_command(args)
    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "9"
