# Range Sum Query 2D - Immutable
# https://leetcode.com/problems/range-sum-query-2d-immutable/
# medium
#
# Time:  O(mn)
# Space: O(mn)
#
# Solution:
# DP


class NumMatrix:
    def __init__(self, matrix: [[int]]):
        self.matrix = matrix
        self.dp = [[0 for _ in range(len(matrix) + 1)]
                   for _ in range(len(matrix) + 1)]

        for r in range(len(matrix)):
            for c in range(len(matrix)):
                self.dp[r + 1][c + 1] = self.dp[r + 1][c] + \
                    self.dp[r][c + 1] + matrix[r][c] - self.dp[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - \
            self.dp[row2 + 1][col1] + self.dp[row1][col1]


matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]

nummatrix = NumMatrix(matrix)

print(nummatrix.sumRegion(2, 1, 4, 3), 8)
print(nummatrix.sumRegion(1, 1, 2, 2), 11)
print(nummatrix.sumRegion(1, 2, 2, 4), 12)
