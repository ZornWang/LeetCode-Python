class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)

        for cur in range(0, len(s), 2 * k):
            res[cur : cur + k] = reversed(res[cur : cur + k])

        return "".join(res)


if __name__ == "__main__":
    s = "abcd"
    k = 3
    solution = Solution()
    print(solution.reverseStr(s, k))
