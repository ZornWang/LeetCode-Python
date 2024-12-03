from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        size = len(nums)
        for i in range(size):
            # 考虑 target 为负数的情况
            if nums[i] > target and target > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, size):
                # 考虑 target 为负数的情况
                if nums[i] + nums[j] > target and target > 0:
                    break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = size - 1
                while left < right:
                    cur = nums[i] + nums[j] + nums[left] + nums[right]
                    if cur > target:
                        right -= 1
                    elif cur < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        left += 1
                        right -= 1
        return result


if __name__ == "__main__":
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    target = 0
    s = Solution()
    print(s.fourSum(nums, target))
