# Maximal Square
# https://leetcode.com/problems/maximal-square/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# DP, TBD details


def maximalSquare(matrix: [[str]]) -> int:
    max_square = 0

    def get_cell_value(matrix, i, j):
        if i >= len(matrix) or j >= len(matrix[i]):
            return 0

        return matrix[i][j]

    def get_size(matrix, i, j):
        tr = int(get_cell_value(matrix, i, j+1))
        br = int(get_cell_value(matrix, i+1, j+1))
        bb = int(get_cell_value(matrix, i+1, j))

        return min(tr, br, bb)

    for i in range(len(matrix)-1, -1, -1):
        for j in range(len(matrix[i])-1, -1, -1):
            matrix[i][j] = int(matrix[i][j])
            if matrix[i][j] != 0:
                matrix[i][j] = get_size(matrix, i, j) + matrix[i][j]

            if pow(matrix[i][j], 2) > max_square:
                max_square = pow(matrix[i][j], 2)

    return max_square


print(maximalSquare([["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], [
      "1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]), 4)

# print(maximalSquare([[]]), 0)
print(maximalSquare([[1, 0, 1, 0, 0, 0], [
      1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1], [1, 0, 0, 1, 1, 1], [0, 0, 0, 1, 1, 1]]), 9)


print(maximalSquare([["1", "1", "0", "1"], [
      "1", "1", "0", "1"], ["1", "1", "1", "1"]]), 4)

# Input:
#   J
# I 1 0 1 0 0
#   1 0 1 1 1
#   1 1 1 1 1
#   1 0 0 1 0

# Output: 4


# 1 0 1 0 0 0
# 1 0 1 1 1 0
# 1 1 1{1 1 1}
# 1 0 0{1 1 1}
# 0 0 0{1 1 1}


# ["1","1","0","1"],
# ["1","1","0","1"],
# ["1","1","1","1"]
