from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        neg = -1
        for i, num in enumerate(nums):
            if num < 0:
                neg = i
            else:
                break

        result = list()
        i, j = neg, neg + 1
        while i >= 0 or j < n:
            if i < 0:
                result.append(nums[j] ** 2)
                j += 1
            elif j == n:
                result.append(nums[i] ** 2)
                i -= 1
            elif abs(nums[i]) < abs(nums[j]):
                result.append(nums[i] ** 2)
                i -= 1
            else:
                result.append(nums[j] ** 2)
                j += 1
        return result


if __name__ == "__main__":
    nums = [-4, -1, 0, 3, 10]
    s = Solution()
    print(s.sortedSquares(nums))
