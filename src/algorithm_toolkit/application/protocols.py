from typing import Protocol

from algorithm_toolkit.models.result import AlgorithmResult


class FindMaxService(Protocol):
    def run_find_max(
        self,
        nums: list[int],
    ) -> AlgorithmResult: ...


class TwoSumService(Protocol):
    def run_two_sum(
        self,
        nums: list[int],
        target: int,
    ) -> AlgorithmResult: ...


class AlgorithmServiceProtocol(
    FindMaxService,
    TwoSumService,
    Protocol,
):
    pass
