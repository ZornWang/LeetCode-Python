from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        # 反转整个数组
        nums.reverse()
        # 反转前k个元素
        nums[:k] = reversed(nums[:k])
        # 反转后n-k个元素
        nums[k:] = reversed(nums[k:])
        return nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums, k)
    print(nums)
