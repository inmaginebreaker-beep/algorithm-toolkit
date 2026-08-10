from algorithm_toolkit.models.algorithm import AlgorithmName


def test_algorithm_name_value() -> None:
    assert AlgorithmName.TWO_SUM.value == "two-sum"
    assert AlgorithmName.FIND_MAX.value == "find-max"


def test_algorithm_name_members_are_distinct() -> None:
    assert AlgorithmName.TWO_SUM is not AlgorithmName.FIND_MAX


def test_algorithm_name_can_be_created_from_value() -> None:
    algorithm = AlgorithmName("find-max")

    assert algorithm is AlgorithmName.FIND_MAX
