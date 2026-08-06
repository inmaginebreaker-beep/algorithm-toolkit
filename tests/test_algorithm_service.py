import pytest

from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.exceptions import InvalidInputError


def test_run_two_sum_returns_matching_indices() -> None:
    service = AlgorithmService()

    result = service.run_two_sum([2, 7, 11, 15], 9)

    assert result == [0, 1]


def test_run_two_sum_returns_empty_list_when_not_found() -> None:
    service = AlgorithmService()

    result = service.run_two_sum([1, 2, 3], 100)

    assert result == []


def test_run_two_sum_rejects_non_integer_target() -> None:
    service = AlgorithmService()

    with pytest.raises(InvalidInputError, match="target 必须是整数"):
        service.run_two_sum([1, 2, 3], "3")  # type: ignore[arg-type]


def test_run_find_max_returns_largest_number() -> None:
    service = AlgorithmService()

    result = service.run_find_max([4, 9, 2, 7])

    assert result == 9


def test_run_find_max_rejects_empty_list() -> None:
    service = AlgorithmService()

    with pytest.raises(
        InvalidInputError,
        match="不接受空列表",
    ):
        service.run_find_max([])


def test_run_reverse_array_does_not_modify_original() -> None:
    service = AlgorithmService()
    nums = [1, 2, 3]

    result = service.run_reverse_array(nums)

    assert result == [3, 2, 1]
    assert nums == [1, 2, 3]
