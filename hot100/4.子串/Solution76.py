# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'
from collections import Counter


class Solution:
    # 滑动窗口，分别记录需要的字符串种类和每个种类需要的数量，对比窗口内的种类和种类数量
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        # 记录目标字符串中的字符频次
        t_cnt = Counter(t)
        # 记录窗口中字符频次
        w_cnt = Counter()

        t_cls = len(t_cnt)  # 需要匹配的字符种类数
        w_cls = 0  # 窗口中已满足的字符种类数

        result = ""

        l = 0
        for r in range(len(s)):
            c = s[r]
            w_cnt[c] += 1

            # 当前字符数量已满足
            if w_cnt[c] == t_cnt[c]:
                w_cls += 1

            # 缩小窗口（注意 l<=r）
            while l <= r and w_cls == t_cls:
                # 更新结果（注意 result 为空时）
                if not result or r - l + 1 < len(result):
                    result = s[l : r + 1]

                # 缩小窗口
                w_cnt[s[l]] -= 1
                # 更新已满足的字符种类数
                if w_cnt[s[l]] < t_cnt[s[l]]:
                    w_cls -= 1

                l += 1

        return result


if __name__ == "__main__":
    s = "a"
    t = "a"
    print(Solution().minWindow(s, t))
