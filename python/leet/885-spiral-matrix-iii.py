# Spiral Matrix III
# https://leetcode.com/problems/spiral-matrix-iii/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# https://leetcode.com/problems/spiral-matrix-iii/discuss/158971/Python-Sort-All-Coordinates

from math import pi
from math import atan2

def spiralMatrixIII(R: int, C: int, r0: int, c0: int) -> [[int]]:
    return sorted([[i,j] for i in range(R) for j in range(C)], key = lambda x: (max(abs(x[0]-r0),abs(x[1]-c0)), -((atan2(-1,1)-atan2(x[0]-r0,x[1]-c0))%(2*pi))))

print(spiralMatrixIII(R = 1, C = 4, r0 = 0, c0 = 0), [[0,0],[0,1],[0,2],[0,3]])
print(spiralMatrixIII(R = 5, C = 6, r0 = 1, c0 = 4), [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]])

# r -> d -> l -> u

#
# R = 1
# C = 4
#
# 0, 0
# 0, 3
#
# path = [(0, 0), (0, 1)]
# visited = [(0, 0), (0, 1), (1, 1), (1, 0)]
# not_visited = 2
#
# dir = "l"
# r0 = 1
# c0 = -1
#
# nd = "l"
# r0n = 1
# c0n = -1
#
#
#
