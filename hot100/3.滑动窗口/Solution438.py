from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return list()

        result = []
        p_count, s_count = [0] * 26, [0] * 26

        for cp, cs in zip(p, s):
            p_count[ord(cp) - ord("a")] += 1
            s_count[ord(cs) - ord("a")] += 1

        if s_count == p_count:
            result.append(0)

        for i in range(len(s) - len(p)):
            s_count[ord(s[i]) - ord("a")] -= 1
            s_count[ord(s[i + len(p)]) - ord("a")] += 1

            if s_count == p_count:
                result.append(i + 1)

        return result


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    print(Solution().findAnagrams(s, p))
