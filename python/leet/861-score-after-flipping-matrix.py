# Score After Flipping Matrix
# https://leetcode.com/problems/score-after-flipping-matrix/
# medium
#
# Time:  O(n*m) – where n number of rows and m number of cols
# Space: O(1)
#
# Solution:
# Greedy

def matrixScore(A: [[int]]) -> int:
    result = 0
    rows = len(A)

    if not A or not A[0]:
        return result

    def toggleRow(row):
        for i in range(len(row)):
            row[i] = 1 if row[i] == 0 else 0

    def toggleColumn(A, col):
        for i in range(len(A)):
            A[i][col] = 1 if A[i][col] == 0 else 0

    # 1. Toggle rows if first is not 1
    for row in A:
        if row[0] == 0:
            continue
        toggleRow(row)

    # 2. Toggle columns to maximize 1 in a column
    for i in range(len(A[0])):
        onesincol = 0
        for row in A:
            onesincol = onesincol + 1 if row[i] == 1 else onesincol

        if onesincol < rows - onesincol:
            toggleColumn(A, i)

    # 3. Calc sum
    for row in A:
        num = 0
        for i in row:
            num = num << 1
            if i == 1:
                num = num | 1

        result += num

    return result

print(matrixScore([[0,0,1,1],[1,0,1,0],[1,1,0,0]]), 39)

# 0,0,1,1
# 1,0,1,0
# 1,1,0,0
# ----
# 1,1,0,0
# 1,0,1,0
# 1,1,0,0
# ----
# 1,1,1,0
# 1,0,0,0
# 1,1,1,0
# ----
# 1,1,1,1
# 1,0,0,1
# 1,1,1,1
