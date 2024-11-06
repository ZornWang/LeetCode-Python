from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        result = float("inf")
        cur = 0

        while right < n:
            cur += nums[right]
            while cur >= target:
                result = min(result, right - left + 1)
                cur -= nums[left]
                left += 1
            right += 1

        return result if result != float("inf") else 0


if __name__ == "__main__":
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    solution = Solution()
    print(solution.minSubArrayLen(target, nums))
