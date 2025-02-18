from typing import List

# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。


class Solution:
    # 动态规划
    def maxSubArray(self, nums: List[int]) -> int:
        # 前一个最大和
        pre_max = nums[0]
        # 当前最大和
        cur_max = nums[0]

        for i in range(1, len(nums)):
            # 更新前一个最大和，如果当前值大于其前面的所有元素只和，取当前值作为新的开始
            pre_max = max(nums[i], pre_max + nums[i])
            # 更新现最大值
            cur_max = max(cur_max, pre_max)

        return cur_max

    # 前缀和
    def maxSubArray(self, nums: List[int]) -> int:
        result = float("-inf")
        min_pre_sum = pre_sum = 0
        for num in nums:
            pre_sum += num  # 当前前缀和
            result = max(result, pre_sum - min_pre_sum)  # 减去前缀和的最小值
            min_pre_sum = min(min_pre_sum, pre_sum)
        return result


if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
