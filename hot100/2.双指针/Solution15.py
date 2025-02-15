from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for i, num in enumerate(nums):
            # 剪枝
            if num > 0:
                return result

            # a 去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                cur = num + nums[left] + nums[right]
                if cur > 0:
                    right -= 1
                elif cur < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    # b, c 去重
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    right -= 1
                    left += 1

        return result
