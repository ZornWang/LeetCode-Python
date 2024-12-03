from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        l = len(nums)
        for i in range(l):
            if nums[i] > 0:
                break
            # a去重
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = l - 1
            while right > left:
                cur = nums[i] + nums[left] + nums[right]
                if cur > 0:
                    right = right - 1
                elif cur < 0:
                    left = left + 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    # b和c去重
                    while right > left and nums[right] == nums[right - 1]:
                        right = right - 1
                    while right > left and nums[left] == nums[left + 1]:
                        left = left + 1
                    left = left + 1
                    right = right - 1
        return result


if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))
