# Rectangle Area
# https://leetcode.com/problems/rectangle-area/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# 1. Compute areas of both rectangles independetly
# 2. Find intersection size and substract it from sum of two areas
#
# Edge cases:
# 1. One rectangle inside another one
# 2. Not overlapping


def computeArea(A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
    width = max(0, min(D, H) - max(B, F))
    height = max(0, min(C, G) - max(A, E))

    return (C-A)*(D-B) + (G-E)*(H-F) - width * height


print(computeArea(-3, 0, 3, 4, 0, -1, 9, 2))
