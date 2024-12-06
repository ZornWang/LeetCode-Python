from typing import List


class Solution:
    # # Normal Solution
    # def strStr(self, haystack: str, needle: str) -> int:
    #     n = len(haystack)
    #     m = len(needle)
    #     for i in range(n - m + 1):
    #         a = i
    #         b = 0
    #         while b < m and haystack[a] == needle[b]:
    #             a += 1
    #             b += 1
    #         if b == m:
    #             return i
    #     return -1

    def getNext(self, next: List[int], s: str) -> None:
        j = 0
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
            next[i] = j

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0
        next = [0] * len(needle)
        self.getNext(next, needle)
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = next[j - 1]
            if haystack[i] == needle[j]:
                j += 1
            if j == len(needle):
                return i - j + 1
        return -1


if __name__ == "__main__":
    s = "abaac"
    solution = Solution()
    next = [0] * len(s)
    solution.getNext(next, s)
    print(next)
