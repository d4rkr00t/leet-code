# Shortest Path in Binary Matrix
# https://leetcode.com/problems/shortest-path-in-binary-matrix/
# medium
#
# Time:  O(e+v)
# Space: O(e+v)
#
# Solution:
# BFS

def shortestPathBinaryMatrix(grid: [[int]]) -> int:
    def get(grid, i, j):
        return grid[i][j] if i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0 else None

    # if start or end is blocked return
    if not grid or not grid[0] or grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    end = (len(grid) - 1, len(grid[0]) - 1)
    queue = [(0, 0, 1)]

    while queue:
        i, j, dist = queue.pop(0)

        if i == end[0] and j == end[1]:
            return dist

        for x, y in [(i-1, j-1), (i-1, j), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i+1, j+1)]:
            if get(grid, x, y) == 0:
                grid[x][y] = 1
                queue.append((x, y, dist + 1))

    return -1


print(shortestPathBinaryMatrix([[0,1],[1,0]]), 2)
print(shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]), 4)
print(shortestPathBinaryMatrix([[0]]), 1)
print(shortestPathBinaryMatrix([[]]), -1)
print(shortestPathBinaryMatrix([[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0]]), 7)
print(shortestPathBinaryMatrix([[0, 1, 0], [0, 1, 0], [0, 1, 0]]), -1)
print(shortestPathBinaryMatrix([[0, 1, 0], [0, 1, 0], [0, 0, 1]]), -1)
