from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        result = 0
        for num in num_set:
            # 剪枝：连续序列的第一个数-1不存在
            if num - 1 not in num_set:
                cur_num = num
                count = 1
                while cur_num + 1 in num_set:
                    cur_num += 1
                    count += 1
                result = max(result, count)

        return result


if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(nums))
