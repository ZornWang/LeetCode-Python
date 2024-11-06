from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid
            elif nums[mid] < target:
                left = mid + 1
        return left


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 2
    s = Solution()
    print(s.searchInsert(nums, target))
