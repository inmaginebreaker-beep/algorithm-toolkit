import logging

from algorithm_toolkit.algorithms.array import find_max, reverse_array, two_sum
from algorithm_toolkit.exceptions import InvalidInputError

logger = logging.getLogger(__name__)


class AlgorithmService:
    """组织算法调用、输入验证和业务日志。"""

    def run_two_sum(self, nums: list[int], target: int) -> list[int]:
        """验证输入并执行 two_sum。"""
        self._validate_integer_list(nums)

        if not isinstance(target, int):
            raise InvalidInputError("target 必须是整数")

        logger.info(
            "Running two_sum: nums_size=%s target=%s",
            len(nums),
            target,
        )

        result = two_sum(nums, target)

        if result:
            logger.info("two_sum completed: result=%s", result)
        else:
            logger.warning("two_sum completed without a matching pair")

        return result

    def run_find_max(self, nums: list[int]) -> int:
        """验证输入并返回最大值。"""
        self._validate_integer_list(nums)

        if not nums:
            raise InvalidInputError("find_max 不接受空列表")

        logger.info("Running find_max: nums_size=%s", len(nums))

        result = find_max(nums)

        logger.info("find_max completed: result=%s", result)
        return result

    def run_reverse_array(self, nums: list[int]) -> list[int]:
        """验证输入并返回反转后的新列表。"""
        self._validate_integer_list(nums)

        logger.info("Running reverse_array: nums_size=%s", len(nums))

        result = reverse_array(nums)

        logger.info("reverse_array completed")
        return result

    @staticmethod
    def _validate_integer_list(nums: list[int]) -> None:
        if not isinstance(nums, list):
            raise InvalidInputError("nums 必须是列表")

        if not all(isinstance(number, int) for number in nums):
            raise InvalidInputError("nums 中的所有元素都必须是整数")
