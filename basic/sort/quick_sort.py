from typing import List


def quick_sort(nums: List[int]):
    if len(nums) < 1:
        return nums

    pivot = nums.pop()
    left = [num for num in nums if num <= pivot]
    right = [num for num in nums if num > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == "__main__":
    nums = [1, 2, 12, 12, 6, 3, 1, 7, 5, 9, 10]
    print(quick_sort(nums))
