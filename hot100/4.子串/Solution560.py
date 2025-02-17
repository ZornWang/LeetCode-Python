from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        for num in nums:
            prefix += num
            count += prefix_count[prefix - k]
            prefix_count[prefix] += 1

        return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))
