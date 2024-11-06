from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums: List[int], target: int) -> int:
            left, right = 0, len(nums)
            while left < right:
                mid = int((left + right) / 2)
                if nums[mid] > target:
                    right = mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return -1

        # 找到出现target的位置
        idx = binary_search(nums, target)
        if idx == -1:
            return [-1, -1]

        # 分别从idx往左往右走，扩展边界
        left, right = idx, idx
        while left - 1 >= 0 and nums[left - 1] == target:
            left -= 1
        while right + 1 < len(nums) and nums[right + 1] == target:
            right += 1
        return [left, right]


if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    s = Solution()
    print(s.searchRange(nums, target))
