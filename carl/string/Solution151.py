class Solution:
    # def reverseWords(self, s: str) -> str:
    #     return " ".join(reversed(s.split()))

    # 移除多余空格
    def trim_spaces(self, s: str) -> list:
        left, right = 0, len(s) - 1

        # 移除开头空格
        while left <= right and s[left] == " ":
            left += 1

        # 移除结尾空格
        while left <= right and s[right] == " ":
            right -= 1

        # 移除中间多余空格
        output = []
        while left <= right:
            # 如果不是空格，加入
            if s[left] != " ":
                output.append(s[left])
            # 如果是空格，且当前最后一个字符不是空格，加入
            elif output[-1] != " ":
                output.append(s[left])
            left += 1

        return output

    # 翻转列表中的指定部分
    def reverse(self, l: list, left: int, right: int) -> None:
        while left < right:
            l[left], l[right] = l[right], l[left]
            left += 1
            right -= 1

    # 翻转每个单词
    def reverse_words(self, l: list) -> None:
        n = len(l)
        start = end = 0

        while start < n:
            # 将 end 移到单词末尾
            while end < n and l[end] != " ":
                end += 1
            # 翻转单词
            self.reverse(l, start, end - 1)
            # start移到下一单词开头
            start = end + 1
            end += 1

    # 组装
    def reverseWords(self, s: str) -> str:
        # 移除多余空格
        l = self.trim_spaces(s)

        # 翻转整个序列
        self.reverse(l, 0, len(l) - 1)

        # 翻转每个单词
        self.reverse_words(l)

        return "".join(l)
