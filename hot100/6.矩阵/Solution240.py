from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        # 从右上角开始 (也可以从左下角开始)
        row = 0
        col = m - 1

        while row < n and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # 向左移动
            else:
                row += 1  # 向下移动

        return False
