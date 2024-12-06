class Solution:
    # Normal Solution
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):
            a = i
            b = 0
            while b < m and haystack[a] == needle[b]:
                a += 1
                b += 1
            if b == m:
                return i
        return -1
