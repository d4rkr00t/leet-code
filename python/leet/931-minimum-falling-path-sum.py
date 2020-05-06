# Minimum Falling Path Sum
# https://leetcode.com/problems/minimum-falling-path-sum/
# medium
#
# Time:  O(n^2)
# Space: O(1)
#
# Solution:
# DP

def minFallingPathSum(A: [[int]]) -> int:
    def get(A, i, j):
        return A[i][j] if i < len(A) and i >= 0 and j < len(A[0]) and j >= 0 else float("inf")

    for i in range(len(A) - 2, -1, -1):
        for j in range(len(A[0]) - 1, -1, -1):
            A[i][j] = A[i][j] + min(get(A, i + 1, j - 1), get(A, i + 1, j), get(A, i + 1, j + 1))

    return min(A[0]) if A and A[0] else None

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]), 12)
print(minFallingPathSum([[]]))

# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# 0, 0, 0

# 12, 13, 15
# 11, 12, 14
# 7, 8, 9
