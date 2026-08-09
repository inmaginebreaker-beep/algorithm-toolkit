import logging

from algorithm_toolkit.algorithms.array import find_max, two_sum
from algorithm_toolkit.exceptions import InvalidInputError
from algorithm_toolkit.models.result import AlgorithmResult

logger = logging.getLogger(__name__)


class AlgorithmService:
    """组织算法调用、输入验证和业务日志。"""

    def run_two_sum(
        self,
        nums: list[int],
        target: int,
    ) -> AlgorithmResult:
        """验证输入并执行 two_sum。"""
        self._validate_integer_list(nums)

        if not isinstance(target, int):
            raise InvalidInputError("target 必须是整数")

        logger.info(
            "Running two_sum: nums_size=%s target=%s",
            len(nums),
            target,
        )

        indices = two_sum(nums, target)

        if indices:
            logger.info("two_sum completed: result=%s", indices)
        else:
            logger.warning("two_sum completed without a matching pair")

        return AlgorithmResult(
            algorithm="two-sum",
            input_size=len(nums),
            result=indices,
        )

    def run_find_max(self, nums: list[int]) -> AlgorithmResult:
        self._validate_integer_list(nums)

        if not nums:
            raise InvalidInputError("find_max 不接受空列表")

        logger.info("Running find_max: nums_size=%s", len(nums))

        maximum = find_max(nums)

        logger.info("find_max completed: result=%s", maximum)

        return AlgorithmResult(
            algorithm="find-max",
            input_size=len(nums),
            result=maximum,
        )

    @staticmethod
    def _validate_integer_list(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise InvalidInputError("nums 必须是列表")

        if not all(isinstance(number, int) for number in nums):
            raise InvalidInputError("nums 中的所有元素都必须是整数")
