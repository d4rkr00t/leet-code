# Spiral Matrix II
# https://leetcode.com/problems/spiral-matrix-ii/
# medium
#
# Time:  O(n^2)
#
# Solution:
# TBD

def generateMatrix(n: int) -> [[int]]:
    A = [[0] * n for _ in range(n)]
    i, j, di, dj = 0, 0, 0, 1
    for k in range(0, n*n):
        A[i][j] = k + 1
        if A[(i+di)%n][(j+dj)%n]:
            di, dj = dj, -di
        i += di
        j += dj
    return A



print(generateMatrix(3), [
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
])

print(generateMatrix(4))

# 3
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
# 0 0
# 0 1
# 0 2
# 1 2
# 2 2
# 2 1
# 2 0
# 1 0
# 1 1

# 4
# [ 1,   2,  3, 4 ],
# [ 12, 13, 14, 5 ],
# [ 11, 16, 15, 6 ],
# [ 10,  9,  8, 7 ],
