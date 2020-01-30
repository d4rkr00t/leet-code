# Rotate Function
# https://leetcode.com/problems/rotate-function/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# rotation - last * n + sum_A - last

def maxRotateFunction(A: [int]) -> int:
    n = len(A) - 1
    # calculate first rotation
    # calculate sum
    sum_a = rotation = max_rotation = 0

    for i, x in enumerate(A):
        sum_a += x
        rotation += i * x

    max_rotation = rotation

    # use the formula for other rotations
    for i in range(n, -1, -1):
        last = A[i]
        rotation = rotation - (last * n) + (sum_a - last)
        max_rotation = max(max_rotation, rotation)

    return max_rotation


print(maxRotateFunction([4, 3, 2, 6]))

# n            = 3
# sum_a        = 15
# max_rotation = 25
# rotation     = 16 - 2 * 3 + 15 - 2
# i    = 2
# last = 2

# 0 1 2 3
# 4 3 2 6
# 15
# 25 - 6 * 3 [18] + 9 = 16
# 16 - 2 * 3 [6] + 13 = 23
# 23 - 3 * 3 [9] + 12 = 26
# 4 3 2 6 = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
# 6 4 3 2 = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
# 2 6 4 3 = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
# 3 2 6 4 = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
