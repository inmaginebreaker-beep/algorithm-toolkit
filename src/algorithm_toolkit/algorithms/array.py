import logging

logger = logging.getLogger(__name__)


def two_sum(nums: list[int], target: int) -> list[int]:
    """返回和为 target 的两个元素下标。

    Args:
        nums: 整数列表。
        target: 目标整数。

    Returns:
        匹配元素的两个下标；不存在时返回空列表。
    """
    logger.debug("two_sum started: nums_size=%s target=%s", len(nums), target)

    seen: dict[int, int] = {}

    for index, number in enumerate(nums):
        complement = target - number

        if complement in seen:
            result = [seen[complement], index]
            logger.debug("two_sum result found: result=%s", result)
            return result

        seen[number] = index

    logger.debug("two_sum completed without result")
    return []


def find_max(nums: list[int]) -> int:
    """返回非空整数列表中的最大值。

    Raises:
        ValueError: 当 nums 为空时抛出。
    """
    if not nums:
        raise ValueError("nums 不能为空")

    current_max = nums[0]

    for number in nums[1:]:
        if number > current_max:
            current_max = number

    return current_max


def reverse_array(nums: list[int]) -> list[int]:
    """返回一个反转后的新列表，不修改原列表。"""
    return list(reversed(nums))


def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Remove duplicate elements from the array.

    Args:
        nums:整数列表

    Returns:
        去重后的整数列表。
    """
    if not isinstance(nums, list):
        raise TypeError("nums必须是一个列表")

    seen = set()
    result = []

    for i in range(len(nums)):
        if nums[i] not in seen:
            result.append(nums[i])
            seen.add(nums[i])
    return result
