# Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# hard

from math import ceil

def numSubmatrixSumTarget(matrix: [[int]], target: int) -> int:
    m, n = len(matrix), len(matrix[0])
    for x in range(m):
        for y in range(n - 1):
            matrix[x][y+1] += matrix[x][y]
    res = 0
    for y1 in range(n):
        for y2 in range(y1, n):
            preSums = {0: 1}
            s = 0
            for x in range(m):
                s += matrix[x][y2] - (matrix[x][y1-1] if y1 > 0 else 0)
                res += preSums.get(s - target, 0)
                preSums[s] = preSums.get(s, 0) + 1
    return res

print(numSubmatrixSumTarget(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0), 4)
print(numSubmatrixSumTarget(matrix = [[0,1,0,1],[1,1,1,1],[0,1,0,1]], target = 0), 4)
print(numSubmatrixSumTarget(matrix = [[1,-1],[-1,1]], target = 0), 5)
print(numSubmatrixSumTarget([[0,1,0,0,1],[0,0,1,1,1],[1,1,1,0,1],[1,1,0,1,1],[0,1,1,0,0]], 1), 47)
