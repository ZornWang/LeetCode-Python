from typing import List


class Solution:
    def fourSumCount(
        self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]
    ) -> int:
        mp = dict()
        for i in nums1:
            for j in nums2:
                mp[i + j] = mp.get(i + j, 0) + 1

        count = 0

        for i in nums3:
            for j in nums4:
                if 0 - (i + j) in mp.keys():
                    count += mp[0 - (i + j)]

        return count
