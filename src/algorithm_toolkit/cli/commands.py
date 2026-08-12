import argparse

from algorithm_toolkit.application.protocols import AlgorithmServiceProtocol


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="algorithm-toolkit",
        description="Algorithm Toolkit CLI",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    create_two_sum_parser(subparsers)
    create_find_max_parser(subparsers)

    return parser


def create_two_sum_parser(
    subparsers: argparse._SubParsersAction,
) -> None:
    parser = subparsers.add_parser(
        "two-sum",
        help="Find two numbers whose sum equals target",
    )

    parser.add_argument(
        "--nums",
        nargs="+",
        type=int,
        required=True,
    )

    parser.add_argument(
        "--target",
        type=int,
        required=True,
    )


def create_find_max_parser(
    subparsers: argparse._SubParsersAction,
) -> None:
    parser = subparsers.add_parser(
        "find-max",
        help="Find the maximum number in a list",
    )

    parser.add_argument(
        "--nums",
        nargs="+",
        type=int,
        required=True,
    )


def run_command(
    args: argparse.Namespace,
    service: AlgorithmServiceProtocol,
) -> int:
    if args.command == "two-sum":
        result = service.run_two_sum(
            nums=args.nums,
            target=args.target,
        )

        print(result.result)
        return 0

    if args.command == "find-max":
        result = service.run_find_max(
            nums=args.nums,
        )

        print(result.result)
        return 0

    return 1
