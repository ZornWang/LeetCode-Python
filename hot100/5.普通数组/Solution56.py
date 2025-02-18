from typing import List


class Solution:
    def q_sort(self, arr: List[List[int]]):
        if len(arr) < 1:
            return arr

        pivot = arr.pop()
        left = [x for x in arr if x[0] <= pivot[0]]
        right = [x for x in arr if x[0] > pivot[0]]

        return self.q_sort(left) + [pivot] + self.q_sort(right)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        intervals = self.q_sort(intervals)

        merged = []
        for interval in intervals:
            # 如果上一个区间的结束小于下一个区间的开始，添加
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            # 更新上一个区间的结束
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))
