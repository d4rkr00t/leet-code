# Reconstruct a 2-Row Binary Matrix
# https://leetcode.com/problems/reconstruct-a-2-row-binary-matrix/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Greedy

def reconstructMatrix(upper: int, lower: int, colsum: [int]) -> [[int]]:
    ans = [[0] * len(colsum), [0] * len(colsum)]

    for i, c in enumerate(colsum):
        if c == 2:
            upper -= 1
            lower -= 1
            ans[0][i] = ans[1][i] = 1
        elif c == 1:
            if upper >= lower:
                upper -= 1
                ans[0][i] = 1
            else:
                lower -= 1
                ans[1][i] = 1

    if upper == lower == 0:
        return ans

    return []

# upper = 0
# lower = 0
# colsum = [1,1,1]
#                ^
# ans = [[1, 1, 0], [0, 0, 1]]
print(reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]), [[1,1,0],[0,0,1]])

# upper = -1
# lower = 0
# colsum = [2,2,1,1]
#                 ^
# ans = []
print(reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]), [])

# upper = 0
# lower = 0
# colsum = [2,1,2,0,1,0,1,2,0,1]
#                             ^
# ans = [[1, 1, 1, 0, 0, 0, 1, 1, 0, 0],[1, 0, 1, 0, 1, 0, 0, 1, 0, 1]]
print(reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]), [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]])
