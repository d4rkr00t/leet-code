# Minimum Area Rectangle II
# https://leetcode.com/problems/minimum-area-rectangle-ii/
# medium

import itertools

def minAreaFreeRect(points: [[int]]) -> float:
    EPS = 1e-7
    points = set(map(tuple, points))

    ans = float('inf')
    for p1, p2, p3 in itertools.permutations(points, 3):
        p4 = p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1]
        if p4 in points:
            v21 = complex(p2[0] - p1[0], p2[1] - p1[1])
            v31 = complex(p3[0] - p1[0], p3[1] - p1[1])
            if abs(v21.real * v31.real + v21.imag * v31.imag) < EPS:
                area = abs(v21) * abs(v31)
                if area < ans:
                    ans = area

    return ans if ans < float('inf') else 0

print(minAreaFreeRect([[1,2],[2,1],[1,0],[0,1]]), 2.0)
print(minAreaFreeRect([[0,1],[2,1],[1,1],[1,0],[2,0]]), 1.0)
print(minAreaFreeRect([[0,3],[1,2],[3,1],[1,3],[2,1]]), 0)
print(minAreaFreeRect([[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]), 2.0)
print(minAreaFreeRect([[7,3],[8,12],[13,5],[6,2],[8,0],[12,8],[14,2],[2,6]]), 20.0)

