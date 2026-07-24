import logging


logger = logging.getLogger(__name__)



def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that add up to the target sum.

    Args:
        nums:整数列表
        target:目标和

    Returns:
        两个整数的索引列表，如果没有找到则返回空列表。
    """

    logger.info(
        "two_sum started"
    )

    if not isinstance(nums, list):
        raise TypeError("nums必须是一个列表")

    if not isinstance(target, int):
        raise TypeError("target必须是一个整数")

    if not all(isinstance(num, int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    seen: dict[int, int] = {}
    for index, number in enumerate(nums):
        complement = target - number
        if complement in seen:
            logger.info(
                "two_sum found result"
            )
            return [seen[complement], index]
        seen[number] = index
    logger.warning(
        "two_sum no result"
    )

    return []


def find_max(nums: list[int]) -> int:
    """
    Find the maximum number in the array.

    Args:
        nums:整数列表

    Returns:
        数组中的最大整数。

    Raises:
        ValueError: 如果数组为空。
    """
    if not isinstance(nums, list):
        raise TypeError("nums必须是一个列表")

    if not all(isinstance(num, int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    if len(nums) == 0:
        raise ValueError("数组不能为空")

    max_num = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]

    return max_num


def reverse_array(nums: list[int]) -> list[int]:
    """返回一个顺序反转的新列表，不修改原列表。

    Args:
        nums: 需要反转的整数列表。

    Returns:
        顺序反转后的新列表。
    """
    result: list[int] = []

    for index in range(len(nums) - 1, -1, -1):
        result.append(nums[index])

    return result


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

    if not all(isinstance(num, int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    seen = set()
    result = []

    for i in range(len(nums)):
        if nums[i] not in seen:
            result.append(nums[i])
            seen.add(nums[i])
    return result
