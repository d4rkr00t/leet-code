# Diagonal Traverse
# https://leetcode.com/problems/diagonal-traverse/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def findDiagonalOrder(matrix: [[int]]) -> [int]:
    res = []
    if not matrix:
        return res

    # group values in matrix by the sum of their indices in a map
    map = {}
    for i in range(len(matrix) + len(matrix[0]) - 1):
        map[i] = []

    # populate the map
    for i, row in enumerate(matrix):
        for j, val in enumerate(row):
            map[i + j].append(val)

    # iterate through map and reverse values where key is divisible by two
    for k, v in map.items():
        if k % 2 == 0:
            map[k] = v[::-1]

    # populate output
    for v in map.values():
        for val in v:
            res.append(val)

    return res


print(findDiagonalOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]), [1,2,4,7,5,3,6,8,9])

print(findDiagonalOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]), [1,2,5,9,6,3,4,7,10,13,14,11,8,12,15,16])

# 1
# 4 2
# 3 5 7
#
#
