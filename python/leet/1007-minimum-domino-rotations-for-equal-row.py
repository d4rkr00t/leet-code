# Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def minDominoRotations(A: [int], B: [int]) -> int:
    for x in [A[0],B[0]]:
        if all(x in d for d in zip(A, B)):
            return len(A) - max(A.count(x), B.count(x))
    return -1



print(minDominoRotations(A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]), 2)
print(minDominoRotations(A = [3,5,1,2,3], B = [3,6,3,3,4]), -1)
print(minDominoRotations(A = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], B = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]), 0)

# A = [2,1,2,4,2,2],
# B = [5,2,6,2,3,2]
#
# A = [3,5,1,2,3],
# B = [3,6,3,3,4]
#
# A = [5,5,5,5,4,5,2,2,1,0],
# B = [2,2,5,6,5,3,5,5,5,5]
