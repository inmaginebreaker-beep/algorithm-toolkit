import pytest

from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.exceptions import InvalidInputError
from algorithm_toolkit.models.algorithm import AlgorithmName


def test_run_two_sum_returns_result() -> None:
    service = AlgorithmService()

    result = service.run_two_sum(
        nums=[2, 7, 11, 15],
        target=9,
    )

    assert result.algorithm is AlgorithmName.TWO_SUM
    assert result.input_size == 4
    assert result.result == [0, 1]
    assert result.success is True


def test_run_two_sum_returns_empty_list_when_not_found() -> None:
    service = AlgorithmService()

    result = service.run_two_sum([1, 2, 3], 100)

    assert result.algorithm is AlgorithmName.TWO_SUM
    assert result.input_size == 3
    assert result.result == []
    assert result.success is True


def test_run_two_sum_rejects_non_integer_target() -> None:
    service = AlgorithmService()

    with pytest.raises(InvalidInputError, match="target 必须是整数"):
        service.run_two_sum([1, 2, 3], "3")  # type: ignore[arg-type]


def test_run_find_max_returns_result() -> None:
    service = AlgorithmService()

    result = service.run_find_max([4, 9, 2, 7])

    assert result.algorithm is AlgorithmName.FIND_MAX
    assert result.input_size == 4
    assert result.result == 9
    assert result.success is True


def test_run_find_max_rejects_empty_list() -> None:
    service = AlgorithmService()

    with pytest.raises(
        InvalidInputError,
        match="不接受空列表",
    ):
        service.run_find_max([])
