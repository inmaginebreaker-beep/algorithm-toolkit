from algorithm_toolkit.models.algorithm import AlgorithmName
from algorithm_toolkit.models.result import AlgorithmResult


def test_algorithem_result_stores_values() -> None:
    result = AlgorithmResult(
        algorithm=AlgorithmName.FIND_MAX,
        input_size=4,
        result=9,
    )

    assert result.algorithm is AlgorithmName.FIND_MAX
    assert result.input_size == 4
    assert result.result == 9
    assert result.success is True


def test_algorithm_result_supports_list_result() -> None:
    result = AlgorithmResult(
        algorithm=AlgorithmName.TWO_SUM, input_size=4, result=[0, 1]
    )

    assert result.result == [0, 1]
