from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = L[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            R[i] = R[i + 1] * nums[i + 1]
        res = [L[i] * R[i] for i in range(n)]
        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))
