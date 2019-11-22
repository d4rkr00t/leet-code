# Prison Cells After N Days
# https://leetcode.com/problems/prison-cells-after-n-days/
# medium
#
# Time:  O(1)
# Space: O(1)
#
# Solution:
# Stupid magic number

def prisonAfterNDays(cells: [int], N: int) -> [int]:
    def get_next(cells):
        new_cells = ""

        for i in range(len(cells)):
            left = cells[i - 1] if i > 0 else -1
            right = cells[i+1] if i < len(cells) - 1 else -2

            new_cells += "1" if left == right else "0"

        return new_cells

    def key(cells):
        res = ""

        for c in cells:
            res += str(c)

        return res;

    cells = key(cells)
    cache = {}
    mutation = N % 14 or 14

    for i in range(mutation):
        cells = get_next(cells)

    return cells

print(prisonAfterNDays(cells = [1,0,0,1,0,0,1,0], N = 1000000000), [0,0,1,1,1,1,1,0])
