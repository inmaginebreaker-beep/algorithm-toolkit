from dataclasses import dataclass

from algorithm_toolkit.models.algorithm import AlgorithmName


@dataclass(frozen=True, slots=True)
class AlgorithmResult:
    algorithm: AlgorithmName
    input_size: int
    result: int | list[int]
    success: bool = True
