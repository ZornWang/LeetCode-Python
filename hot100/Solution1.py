from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i


if __name__ == "__main__":
    nums = [3, 3]
    target = 6
    s = Solution()
    print(s.twoSum(nums, target))
