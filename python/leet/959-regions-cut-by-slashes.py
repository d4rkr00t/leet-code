# Regions Cut By Slashes
# https://leetcode.com/problems/regions-cut-by-slashes/
# medium


def regionsBySlashes(grid):  # [0, 1, 1, 3, 4, 5, 6, 7]
    uf = [x for x in range(pow(len(grid[0]), 2) * 2)]
    level_len = len(grid[0]) * 2  # 4

    def find_parent(a):
        parent = uf[a]

        while parent != uf[parent]:
            parent = uf[parent]

        return parent

    def union(a, b):  # 2, 1
        if (a < 0 or b < 0):
            return

        fp = find_parent(a)  # 2
        tp = find_parent(b)  # 1

        uf[fp] = tp

    for l in range(len(grid)):  # 1
        offset = l * level_len  # 4
        for i, c in enumerate(grid[l]):  # 0 '\'
            fi = i * 2  # 0
            si = i * 2 + 1  # 1

            if c == ' ':  # False
                union(offset + fi, offset + si)

            if fi > 0:
                union(offset + fi, offset + fi - 1)  # 2, 1

            if c != '\\' and l > 0:
                square = 1 if grid[l - 1][i] != '\\' else 0
                union(offset + fi, (l - 1) * level_len + fi + square)

            if c == '\\' and l > 0:
                square = -1 if grid[l - 1][i] == '\\' else 0  # 0
                union(offset + si, (l - 1) * level_len + si + square)  # 5, 1

    ans = 0

    for i, e in enumerate(uf):
        if i == e:
            ans += 1

    return ans


print(regionsBySlashes([
    " /",
    "/ "
]), 2)

print(regionsBySlashes([
    " /",
    "  "
]), 1)
print(regionsBySlashes([
    "\\/",
    "/\\"
]), 4)
print(regionsBySlashes([
    "/\\",
    "\\/"
]), 5)
print(regionsBySlashes([
    "//",
    "/ "
]), 3)
