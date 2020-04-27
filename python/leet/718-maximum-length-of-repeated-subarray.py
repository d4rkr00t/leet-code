# Maximum Length of Repeated Subarray
# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
# medium
#
# Time:  O(n*m)
# Space: O(n*m)
#
# Solution:
# DP

def findLength(A: [int], B: [int]) -> int:
    memo = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(len(A) - 1, -1, -1):
        for j in range(len(B) - 1, -1, -1):
            if A[i] == B[j]:
                memo[i][j] = memo[i+1][j+1]+1
    return max(max(row) for row in memo)


print(findLength([1,2,3,2,1], [3,2,1,4,7]), 3)
print(findLength([1], [3,2,1,4,7]), 1)
print(findLength([], [3,2,1,4,7]), 0)
print(findLength([], []), 0)
print(findLength([0,1,1,1,1], [1,0,1,0,1]), 2)
print(findLength([1,0,0,0,1], [1,0,0,1,1]), 3)
