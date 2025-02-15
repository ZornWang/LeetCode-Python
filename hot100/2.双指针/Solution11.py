from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            # 木桶原理
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
