from algorithm_toolkit.algorithms.array import two_sum


def test_two_sum_found() -> None:
    result = two_sum([2, 7, 11, 15], 9)

    assert result == [0, 1]


def test_two_sum_not_found() -> None:
    result = two_sum([1, 2, 3], 100)

    assert result == []