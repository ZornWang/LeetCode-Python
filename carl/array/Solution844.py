from typing import List


class Solution:
    # # 构造字符串
    # def backspaceCompare(self, s: str, t: str) -> bool:
    #     def backspace(string: str):
    #         result = ""
    #         for ch in string:
    #             if ch == "#":
    #                 result = result[:-1]
    #             else:
    #                 result += ch
    #         return result

    #     return backspace(s) == backspace(t)

    # 双指针
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        ship_s = ship_t = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    ship_s += 1
                    i -= 1
                elif ship_s > 0:
                    ship_s -= 1
                    i -= 1
                else:
                    break
            while j >= 0:
                if t[j] == "#":
                    ship_t += 1
                    j -= 1
                elif ship_t > 0:
                    ship_t -= 1
                    j -= 1
                else:
                    break
            if i >= 0 and j >= 0:
                if s[i] != t[j]:
                    return False
            elif i >= 0 or j >= 0:
                return False
            i -= 1
            j -= 1
        return True


if __name__ == "__main__":
    s = "a##c"
    t = "#a#b"
    solution = Solution()
    print(solution.backspaceCompare(s, t))
