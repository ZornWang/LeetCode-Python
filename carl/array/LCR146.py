from typing import List


class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if not array:
            return list()

        m, n = len(array), len(array[0])
        result = []
        top, bottom, left, right = 0, m - 1, 0, n - 1
        count = m * n
        loop = max(m, n) // 2
        while loop:
            # 从左往右
            for i in range(left, right):
                if not count:
                    break
                result.append(array[top][i])
                count -= 1
            # 从上往下
            for i in range(top, bottom):
                if not count:
                    break
                result.append(array[i][right])
                count -= 1
            # 从右往左
            for i in range(right, left, -1):
                if not count:
                    break
                result.append(array[bottom][i])
                count -= 1
            # 从下往上
            for i in range(bottom, top, -1):
                if not count:
                    break
                result.append(array[i][left])
                count -= 1

            top += 1
            bottom -= 1
            left += 1
            right -= 1
            loop -= 1

        if count and (m * n) % 2 == 1:
            result.append(array[m // 2][n // 2])

        return result


if __name__ == "__main__":
    array = []
    solution = Solution()
    print(solution.spiralArray(array))
