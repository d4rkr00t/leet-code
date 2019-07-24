# Making A Large Island
# https://leetcode.com/problems/making-a-large-island/
# hard


def largest_island(grid):  # [1, 1], [1, 0]
    N = len(grid)

    def neighbors(r, c):
        for nr, nc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
            if 0 <= nr < N and 0 <= nc < N:
                yield nr, nc

    def dfs(r, c, index):
        ans = 1
        grid[r][c] = index
        for nr, nc in neighbors(r, c):
            if grid[nr][nc] == 1:
                ans += dfs(nr, nc, index)
        return ans

    area = {}
    index = 2
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 1:
                area[index] = dfs(r, c, index)
                index += 1

    ans = max(area.values() or [0])
    for r in range(N):
        for c in range(N):
            if grid[r][c] == 0:
                seen = {grid[nr][nc]
                        for nr, nc in neighbors(r, c) if grid[nr][nc] > 1}
                ans = max(ans, 1 + sum(area[i] for i in seen))

    return ans


print(largest_island([[1, 0], [0, 1]]), 3)
print(largest_island([[1, 1], [1, 0]]), 4)
print(largest_island([[1, 1], [1, 1]]), 4)
print(largest_island([[1, 0], [1, 1]]), 4)
print(largest_island([[1, 0], [1, 0]]), 3)
