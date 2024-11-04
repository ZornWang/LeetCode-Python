from typing import List


class Solution:
    # def moveZeroes(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     left = 0
    #     right = 1
    #     while right < len(nums):
    #         if nums[left] == 0 and nums[right] != 0:
    #             nums[left], nums[right] = nums[right], nums[left]
    #             left += 1
    #             right += 1
    #         elif nums[left] != 0:
    #             left += 1
    #             right += 1
    #         else:
    #             right += 1

    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)
