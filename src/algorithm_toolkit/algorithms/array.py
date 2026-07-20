def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Find two numbers in the array that add up to the target sum.

    Args:
        nums:整数列表
        target:目标和

    Returns:
        两个整数的索引列表，如果没有找到则返回空列表。
    """

    if not isinstance(nums,list):
        raise TypeError("nums必须是一个列表")

    if not isinstance(target,int):
        raise TypeError("target必须是一个整数")

    if not all(isinstance(num,int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    seen: dict[int, int] = {}
    for index,number in enumerate(nums):
        complement = target - number
        if complement in seen:
            return [seen[complement], index]
        seen[number] = index

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
    if not isinstance(nums,list):
        raise TypeError("nums必须是一个列表")

    if not all(isinstance(num,int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    if len(nums) == 0:
        raise ValueError("数组不能为空")

    max_num = nums[0]

    for i in range(1,len(nums)):
        if nums[i] > max_num:
            max_num = nums[i]

    return max_num





def reverse_array(nums: list[int]) -> list[int]:
    """
    Reverse the order of elements in the array.

    Args:
        nums:整数列表

    Returns:
        反转后的整数列表。
    """
    if not isinstance(nums,list):
        raise TypeError("nums必须是一个列表")

    if not all(isinstance(num,int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    new_nums = []
    right = len(nums) -1
    while right >= 0:
        new_nums.append(nums[right])
        right -=1

    return new_nums


def remove_duplicates(nums: list[int]) -> list[int]:
    """
    Remove duplicate elements from the array.

    Args:
        nums:整数列表

    Returns:
        去重后的整数列表。
    """
    if not isinstance(nums,list):
        raise TypeError("nums必须是一个列表")

    if not all(isinstance(num,int) for num in nums):
        raise TypeError("nums的元素必须是整数")

    seen = set()
    result = []

    for i in range(len(nums)):
        if nums[i] not in seen:
            result.append(nums[i])
            seen.add(nums[i])
    return result