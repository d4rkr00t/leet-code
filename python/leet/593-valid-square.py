# Valid Square
# https://leetcode.com/problems/valid-square/
# medium
#
# Time:  O(1)
# Space: O(1)
#
# Solution:
# a^2 + b^2 = c
#
# y |
# 1 |x         x
#   |
#   |
# 0 |x         x
#    ________________
#    0         1    x
#
# y |
# 3 |
# 1 |      x
# 0 | x         x
# -1|      x
#    ________________
#     -1   0    1   x
#

import math
from functools import cmp_to_key


def validSquare(p1: [int], p2: [int], p3: [int], p4: [int]) -> bool:
    def dist(x, y):
        return math.sqrt(
            pow(abs(y[0] - x[0]), 2) + pow(abs(y[1] - x[1]), 2))

    p = [p1, p2, p3, p4]
    p.sort(key=cmp_to_key(
        lambda x, y: x[1] - y[1] if y[0] == x[0] else x[0] - y[0]))

    if dist(p[0], p[1]) == dist(p[0], p[2]) and dist(p[1], p[3]) == dist(p[2], p[3]) and dist(p[0], p[1]) == dist(p[1], p[3]):
        return True

    return False


print(validSquare([0, 0], [1, 1], [1, 0], [0, 1]))

print(validSquare([1, 0],
                  [-1, 0],
                  [0, 1],
                  [0, -1]))

print(validSquare([1134, -2539],
                  [492, -1255],
                  [-792, -1897],
                  [-150, -3181]))
