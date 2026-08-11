from algorithm_toolkit.application.algorithm_service import AlgorithmService
from algorithm_toolkit.application.protocols import FindMaxService
from algorithm_toolkit.models.algorithm import AlgorithmName
from algorithm_toolkit.models.result import AlgorithmResult


def execute_find_max(
    service: FindMaxService,
    nums: list[int],
) -> int:
    result = service.run_find_max(nums)

    if not isinstance(result.result, int):
        raise TypeError("find-max result must be an integer")

    return result.result


class FakeFindMaxService:
    def run_find_max(
        self,
        nums: list[int],
    ) -> AlgorithmResult:
        return AlgorithmResult(
            algorithm=AlgorithmName.FIND_MAX,
            input_size=len(nums),
            result=999,
        )


def test_algorithm_service_matches_find_max_protocol() -> None:
    service = AlgorithmService()

    result = execute_find_max(
        service,
        [4, 9, 2, 7],
    )

    assert result == 9


def test_fake_service_matches_find_max_protocol() -> None:
    service = FakeFindMaxService()

    result = execute_find_max(
        service,
        [1, 2, 3],
    )

    assert result == 999
