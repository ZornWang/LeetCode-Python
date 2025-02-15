from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        result = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                cur = num
                count = 1
                while cur + 1 in nums_set:
                    count += 1
                    cur += 1
                result = max(count, result)
        return result
