class Solution:
    def change(self, s):
        lst = list(s)
        for i in range(len(lst)):
            if lst[i].isdigit():
                lst[i] = "number"
        # return "".join(["number" if c.isdigit() else c for c in s])
        return "".join(lst)
