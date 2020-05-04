# Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/
# medium
#
# Time:  O(n*m)
# Space: O(1)
#
# Solution:
# 1. Find all rotten oranges
# 2. BFS from them all at the same time
# 3. Check if there are any unprocessed items left

def orangesRotting(grid: [[int]]) -> int:
    stack = []
    time = 0
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    # 1. Find all rotten oranges
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 2:
                stack.append((i, j, 0))

    # 2. BFS from them all at the same time
    while stack:
        i, j, t = stack.pop(0) # 2, 1, 3
        time = max(t, time)

        for x, y in dirs:
            ni = i + x
            nj = j + y
            if ni >= 0 and ni < len(grid) and nj >= 0 and nj < len(grid[0]) and grid[ni][nj] == 1:
                stack.append((ni, nj, t+1))
                grid[ni][nj] = 2

    # 3. Check if there are any unprocessed items left
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                return -1

    return time

print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)
