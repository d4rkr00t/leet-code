# Uncrossed Lines
# https://leetcode.com/problems/uncrossed-lines/
# medium
#
# Time:  O(MN)
# Space: O(MN)
#
# Solution:
# DP
#
# dp[i][j] = dp[i-1][j-1] + 1 if A[i] == A[j] else max(dp[i-1][j], dp[i][j-1])

def maxUncrossedLines(A: [int], B: [int]) -> int:
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

    for i in range(1, len(A)+1):
        for j in range(1, len(B)+1):
            EA = A[i-1]
            EB = B[j-1]

            dp[i][j] = dp[i-1][j-1] + 1 if EA == EB else max(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]

# A = [1,4,2], B = [1,2,4]
#
#     1 2 4
#   0 0 0 0
# 1 0 1 1 1
# 4 0 1 1 2
# 2 0 1 2 2

# A = [ 2,5,1,2,5],
# B = [10,5,2,1,5,2]
#
#     2 5 1 2 5
#   0 0 0 0 0 0
#10 0 0 0 0 0 0
# 5 0 0 1 1 1 1
# 2 0 1 1 1 2 2
# 1 0 1 1 2 2 2
# 5 0 1 2 2 2 3
# 2 0 1 2 2 3 3

# A = [1,3,7,1,7,5],
# B = [1,9,2,5,1]
#
#     1 3 7 1 7 5
#   0 0 0 0 0 0 0
# 1 0 1 1 1 1 1 1
# 9 0 1 1 1 1 1 1
# 2 0 1 1 1 1 1 1
# 5 0 1 1 1 1 1 2
# 1 0 1 1 1 2 2 2

print(maxUncrossedLines(A = [1,4,2], B = [1,2,4]), 2)
print(maxUncrossedLines(A = [2,5,1,2,5], B = [10,5,2,1,5,2]), 3)
print(maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]), 2)
print(maxUncrossedLines(A = [], B = [1,9,2,5,1]), 0)
print(maxUncrossedLines(A = [], B = []), 0)
