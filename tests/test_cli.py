from algorithm_toolkit.cli.commands import create_parser


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
