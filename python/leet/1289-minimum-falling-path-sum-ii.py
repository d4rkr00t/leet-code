# Minimum Falling Path Sum II
# https://leetcode.com/problems/minimum-falling-path-sum-ii/
# hard
#
# Time:  O(n*m)
# Space: O(n*m)
#
# Solution:
# Dynamic Programming

def minFallingPathSum(arr: [[int]]) -> int:
    rl, cl = len(arr), len(arr[0])
    memo = [float('inf') for _ in range(cl)]

    #m1, m2 are the two smallest number in the given arr, and i1 is the index of the smallest number
    def find_two_smallest(a):
        m1, m2 = float('inf'), float('inf')
        for i, x in enumerate(a):
            if x <= m1:
                m1, m2, i1 = x, m1, i
            elif x < m2:
                m2 = x
        return [m1, m2, i1]

    d = find_two_smallest(arr[0])
    for i in range(1,rl):
        for j in range(cl):
            if d[2] == j:
                memo[j] = d[1] + arr[i][j]
            else:
                memo[j] = d[0] + arr[i][j]
        d = find_two_smallest(memo)
    return d[0]

print(minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]), 13)
print(minFallingPathSum([[1]]), 1)
print(minFallingPathSum([[1,2,3],[4,-5,6],[7,8,9]]), 3)
print(minFallingPathSum([[-73,61,43,-48,-36],[3,30,27,57,10],[96,-76,84,59,-15],[5,-49,76,31,-7],[97,91,61,-46,67]]), -192)

