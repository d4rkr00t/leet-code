# Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
# easy
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

def sortedSquares(A: [int]) -> [int]:
    s = 0
    e = len(A) - 1
    res = []

    while s <= e and s < len(A) and e >= 0:
        if abs(A[s]) > abs(A[e]):
            res.append(pow(A[s], 2))
            s += 1
        else:
            res.append(pow(A[e], 2))
            e -= 1

    res.reverse()

    return res

print(sortedSquares([-4,-1,0,3,10]), [0,1,9,16,100])
print(sortedSquares([-7,-3,2,3,11]), [4,9,9,49,121])

# [-4,-1,0,3,10]
# s = 2
# e = 1
# res = [100, 16, 9, 1, 0]
#
#
