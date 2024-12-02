from typing import List
from collections import Counter


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)

        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1

        res = []
        for num in nums2:
            if num in table.keys() and table[num] != 0:
                res.append(num)
                table[num] = table[num] - 1

        return res
