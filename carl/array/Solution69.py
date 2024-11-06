class Solution:
    def mySqrt(self, x: int) -> int:
        left, right, result = 0, x, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= x:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result


if __name__ == "__main__":
    x = 0
    s = Solution()
    print(s.mySqrt(x))
