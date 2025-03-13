from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # matrix[::-1] 将矩阵上下翻转
        # zip(*matrix[::-1]) 将翻转后的矩阵转置
        # list(map(list, ...)) 将转置后的结果转换回列表形式
        # matrix[:] = ... 使用切片赋值
        # matrix[:] = list(map(list, zip(*matrix[::-1])))

        n = len(matrix)

        # 1. 沿主对角线翻转
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # 2. 每行进行反转
        for row in matrix:
            row.reverse()


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    solution = Solution()
    solution.rotate(matrix)
    print(matrix)
