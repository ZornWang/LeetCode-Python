from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for index, num in enumerate(nums):
            if target - num in table:
                return [table[target - num], index]
            table[num] = index
