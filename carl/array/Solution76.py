from collections import Counter
from typing import List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = right = 0
        result = ""
        cnt = Counter(t)
        required = len(cnt)
        formed = 0
        window = {}
        while right < len(s):
            char = s[right]
            window[char] = window.get(char, 0) + 1
            if char in cnt and window[char] == cnt[char]:
                formed += 1
            while left <= right and formed == required:
                if not result or right - left + 1 < len(result):
                    result = s[left : right + 1]
                window[s[left]] -= 1
                if s[left] in cnt and window[s[left]] < cnt[s[left]]:
                    formed -= 1
                left += 1
            right += 1
        return result


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    solution = Solution()
    print(solution.minWindow(s, t))
