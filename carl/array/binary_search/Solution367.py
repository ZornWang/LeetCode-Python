class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right, result = 0, num, -1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid <= num:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return True if result * result == num else False


if __name__ == "__main__":
    num = 14
    s = Solution()
    print(s.isPerfectSquare(num))
