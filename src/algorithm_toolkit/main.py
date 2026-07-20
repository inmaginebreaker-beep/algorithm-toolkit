from algorithm_toolkit.algorithms.array import (
    find_max,
    remove_duplicates,
    reverse_array,
    two_sum,
)


def main() -> None:
    nums = [2, 7, 2, 11, 15]

    print("两数之和：", two_sum(nums, 9))
    print("最大值：", find_max(nums))
    print("反转：", reverse_array(nums))
    print("去重：", remove_duplicates(nums))


if __name__ == "__main__":
    main()