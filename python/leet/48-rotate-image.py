# Rotate Image
# url: https://leetcode.com/problems/rotate-image/
# medium


def rotate(matrix):
    i = j = 0
    s = len(matrix)

    while (i <= s // 2):
        while (j < s - 1 - i):
            tl = (i, j)
            tr = (j, s - i - 1)
            br = (s - i - 1, s - j - 1)
            bl = (s - j - 1, i)

            matrix[bl[0]][bl[1]], matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]], matrix[br[0]][br[1]
                                                                                            ] = matrix[br[0]][br[1]], matrix[bl[0]][bl[1]], matrix[tl[0]][tl[1]], matrix[tr[0]][tr[1]]
            j += 1

        i += 1
        j = i

    return matrix


# print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]))
