from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class AlgorithmResult:
    algorithm: str
    input_size: int
    result: int | list[int]
    success: bool = True
