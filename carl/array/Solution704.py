# 相关题目推荐
# 35.搜索插入位置(opens new window)
# 34.在排序数组中查找元素的第一个和最后一个位置(opens new window)
# 69.x 的平方根(opens new window)
# 367.有效的完全平方数(opens new window)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
        return -1


if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    s = Solution()
    print(s.search(nums, target))
