from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # 第一步：将非正整数替换为 n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        # 第二步：标记出现过的正整数
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])

        # 第三步：找到第一个为正数的位置
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        # 如果所有位置都是负数，返回 n+1
        return n + 1


if __name__ == "__main__":
    nums = [3, 4, -1, 1]
    solution = Solution()
    print(solution.firstMissingPositive(nums))  # 2
