from collections import Counter
from typing import List


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        cnt = Counter()

        left = result = 0
        for right, fruit in enumerate(fruits):
            cnt[fruit] += 1
            while len(cnt) > 2:
                cnt[fruits[left]] -= 1
                if cnt[fruits[left]] == 0:
                    cnt.pop(fruits[left])
                left += 1
            result = max(result, right - left + 1)

        return result


if __name__ == "__main__":
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    solution = Solution()
    print(solution.totalFruit(fruits))
