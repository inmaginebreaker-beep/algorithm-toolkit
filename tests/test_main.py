from algorithm_toolkit.main import main


def test_main_returns_success_exit_code() -> None:
    result = main()

    assert result == 0
