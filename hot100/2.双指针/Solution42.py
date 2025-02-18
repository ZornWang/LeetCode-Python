from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = rightMax = result = 0

        while left < right:
            # 从左往右考虑
            if height[left] < height[right]:
                if height[left] > leftMax:
                    leftMax = height[left]
                else:
                    result += leftMax - height[left]
                left += 1
            # 从右往左考虑
            else:
                if height[right] > rightMax:
                    rightMax = height[right]
                else:
                    result += rightMax - height[right]
                right -= 1

        return result

    # 单调栈
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = list()

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                top = stack.pop()
                if not stack:
                    break
                left = stack[-1]
                cur_w = i - left - 1
                cur_h = min(height[i], height[left]) - height[top]
                result += cur_w * cur_h
            stack.append(i)

        return result

    # 动态规划
    def trap(self, height: List[int]) -> int:
        result = 0
        n = len(height)
        if n < 3:
            return 0

        leftMax = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rightMax = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])

        for i in range(n):
            result += min(leftMax[i], rightMax[i]) - height[i]

        return result
