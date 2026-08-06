import pytest

from algorithm_toolkit.algorithms.array import find_max, two_sum


def test_two_sum_found() -> None:
    result = two_sum([2, 7, 11, 15], 9)

    assert result == [0, 1]


def test_two_sum_not_found() -> None:
    result = two_sum([1, 2, 3], 100)

    assert result == []


def test_find_max_returns_largest_number() -> None:
    result = find_max([4, 9, 2, 7])

    assert result == 9


def test_find_max_supports_negative_numbers() -> None:
    result = find_max([-8, -3, -12, -5])

    assert result == -3


def test_find_max_rejects_empty_list() -> None:
    with pytest.raises(ValueError, match="不能为空"):
        find_max([])
