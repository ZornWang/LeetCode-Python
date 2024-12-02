class Solution:
    def isHappy(self, n: int) -> bool:
        def get_sum(n: int):
            total = 0
            while n:
                n, r = divmod(n, 10)
                total += r**2
            return total

        record = set()
        while True:
            n = get_sum(n)
            if n == 1:
                return True
            if n in record:
                return False
            else:
                record.add(n)


if __name__ == "__main__":
    n = 1
    s = Solution()
    print(s.isHappy(n))
