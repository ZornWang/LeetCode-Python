class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        right, result = -1, 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i - 1])
            while right + 1 < n and s[right + 1] not in occ:
                occ.add(s[right + 1])
                right += 1
            result = max(result, right - i + 1)

        return result


if __name__ == "__main__":
    s = "abcabcbb"
    print(Solution().lengthOfLongestSubstring(s))
