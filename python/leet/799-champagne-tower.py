# Champagne Tower
# https://leetcode.com/problems/champagne-tower/
# medium


def champagneTower(poured, query_row, query_glass):
    tower = [[0] * k for k in range(1, 102)]

    tower[0][0] = poured

    for r in range(query_row + 1):
        for c in range(r + 1):
            exces = (tower[r][c] - 1.0) / 2.0
            if exces > 0:
                tower[r+1][c] += exces
                tower[r+1][c+1] += exces

    return min(1, tower[query_row][query_glass])


print(champagneTower(2, 1, 1))

# Poor: 0
# Query: (5, 4)
#               [0.0]
#            [0.0] [0.0]
#         [0.0] [0.0] [0.0]
#       [0.0] [0.0] [0.0] [0.0]
#    [0.0] [0.0] [0.0] [0.0] [0.0]
# [0.0] [0.0] [0.0] [0.0] [0.0] [0.0]
