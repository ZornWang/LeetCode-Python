from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = dict()
        for i, num in enumerate(nums):
            if target - num in mp.keys():
                return [mp[target - num], i]
            mp[num] = i
        return []
