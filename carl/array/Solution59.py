from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        x = y = 0
        loop, mid = n // 2, n // 2
        count = 1
        offset = 1
        while loop:
            # 从左到右
            for index in range(y, n - offset):
                result[x][index] = count
                count += 1
            # 从上到下
            for index in range(x, n - offset):
                result[index][n - offset] = count
                count += 1
            # 从右到左
            for index in range(n - offset, y, -1):
                result[n - offset][index] = count
                count += 1
            # 从下到上
            for index in range(n - offset, x, -1):
                result[index][y] = count
                count += 1

            x += 1
            y += 1
            offset += 1
            loop -= 1

        if n % 2 != 0:
            result[mid][mid] = count

        return result


if __name__ == "__main__":
    n = 4
    solution = Solution()
    print(solution.generateMatrix(n))
