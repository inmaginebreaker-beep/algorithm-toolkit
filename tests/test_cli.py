import argparse
from unittest.mock import create_autospec

from _pytest.capture import CaptureFixture

from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.cli.commands import create_parser, run_command
from algorithm_toolkit.models.algorithm import AlgorithmName
from algorithm_toolkit.models.result import AlgorithmResult


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

    service = FakeAlgorithmService()

    exit_code = run_command(
        args,
        service,
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "999"


def test_run_two_sum_command(
    capsys: CaptureFixture[str],
) -> None:
    args = argparse.Namespace(
        command="two-sum",
        nums=[2, 7, 11, 15],
        target=9,
    )

    service = FakeAlgorithmService()

    exit_code = run_command(
        args,
        service,
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "[8, 9]"


class FakeAlgorithmService:
    def run_two_sum(
        self,
        nums: list[int],
        target: int,
    ) -> AlgorithmResult:
        return AlgorithmResult(
            algorithm=AlgorithmName.TWO_SUM,
            input_size=len(nums),
            result=[8, 9],
        )

    def run_find_max(
        self,
        nums: list[int],
    ) -> AlgorithmResult:
        return AlgorithmResult(
            algorithm=AlgorithmName.FIND_MAX,
            input_size=len(nums),
            result=999,
        )


def test_run_find_max_calls_service(
    capsys: CaptureFixture[str],
) -> None:
    service = create_autospec(
        AlgorithmService,
        instance=True,
    )

    service.run_find_max.return_value = AlgorithmResult(
        algorithm=AlgorithmName.FIND_MAX,
        input_size=4,
        result=999,
    )

    args = argparse.Namespace(
        command="find-max",
        nums=[4, 9, 2, 7],
    )

    exit_code = run_command(args, service)

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "999"

    service.run_find_max.assert_called_once_with(
        nums=[4, 9, 2, 7],
    )


def test_run_two_sum_calls_service(
    capsys: CaptureFixture[str],
) -> None:
    service = create_autospec(
        AlgorithmService,
        instance=True,
    )

    service.run_two_sum.return_value = AlgorithmResult(
        algorithm=AlgorithmName.TWO_SUM,
        input_size=4,
        result=[8, 9],
    )

    args = argparse.Namespace(
        command="two-sum",
        nums=[2, 7, 11, 15],
        target=9,
    )

    exit_code = run_command(args, service)

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out.strip() == "[8, 9]"

    service.run_two_sum.assert_called_once_with(
        nums=[2, 7, 11, 15],
        target=9,
    )
