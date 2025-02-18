from typing import List
from collections import defaultdict


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.arr = arr
        self.table = defaultdict(list)
        for index, x in enumerate(self.arr):
            self.table[x].append(index)

    def bis_l(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if nums[mid] < x:
                l = mid + 1
            else:
                r = mid
        return l

    def bis_r(self, nums: List[int], x: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) // 2
            if x < nums[mid]:
                r = mid
            else:
                l = mid + 1
        return l

    def query(self, left: int, right: int, value: int) -> int:
        assert self.arr
        pos = self.table[value]
        l = self.bis_l(pos, left)
        r = self.bis_r(pos, right)
        return r - l


if __name__ == "__main__":
    arr = [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]
    obj = RangeFreqQuery(arr)
    print(obj.query(1, 2, 4))
    print(obj.query(0, 11, 33))
