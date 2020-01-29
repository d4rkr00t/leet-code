# Count Square Submatrices with All Ones
# https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# medium
#
# Time:  O(n*m)
# Space: O(1)

def countSquares(matrix: [[int]]) -> int:
    for i in range(len(matrix) - 2, -1, -1):
      for j in range(len(matrix[0]) - 2, -1, -1):
        if matrix[i][j] != 1:
          continue

        size = min(matrix[i][j+1], matrix[i+1][j+1], matrix[i+1][j])
        matrix[i][j] += size

    total = 0

    for i in range(len(matrix)):
      total += sum(matrix[i])

    return total

print(countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]), 15)
print(countSquares([
  [1,0,1],
  [1,1,0],
  [1,1,0]
]), 7)
print(countSquares([]), 0)
print(countSquares([[1], [1], [1]]), 3)
print(countSquares([[1, 1, 1]]), 3)
