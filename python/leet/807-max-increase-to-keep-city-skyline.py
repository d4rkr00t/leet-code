# Max Increase to Keep City Skyline
# https://leetcode.com/problems/max-increase-to-keep-city-skyline/
# medium
#
# Time:  O(n^2)
# Space: O(n)
#
# Solution:
#
# The grid is:
#           j
# [3, 0, 8, 4] i
# [2, 4, 5, 7]
# [9, 2, 6, 3]
# [0, 3, 1, 0]
#
#  vertical   = [9, 4, 8, 7]
#  horizontal = [8, 7, 9, 3]


def maxIncreaseKeepingSkyline(grid: [[int]]) -> int:
    vertical = [0] * len(grid)    # [9, 4, 8, 7]
    horizontal = [0] * len(grid)  # [8, 7, 9, 3]

    for i in range(len(grid)):
        for j in range(len(grid)):
            item = grid[i][j]

            if item > vertical[j]:
                vertical[j] = item

            if item > horizontal[i]:
                horizontal[i] = item

    diff = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            item = grid[i][j]
            max_val = min(vertical[j], horizontal[i])

            if item < max_val:
                grid[i][j] = max_val
                diff += max_val - item

    return diff


print(maxIncreaseKeepingSkyline(
    [[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]]), 35)
