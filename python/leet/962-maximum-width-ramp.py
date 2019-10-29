# Maximum Width Ramp
# https://leetcode.com/problems/maximum-width-ramp/
# medium
#
# Time:  O(n logn) ->  – is number of items
# Space: O(n)


def maxWidthRamp(A: [int]) -> int:  # [6, 0, 8, 2, 1, 5]
    ans = 0
    m = float('inf')
    for i in sorted(range(len(A)), key=A.__getitem__):
        ans = max(ans, i - m)
        m = min(m, i)
    return ans


# The maximum width ramp is achieved at (i, j) = (1, 5): A[1] = 0 and A[5] = 5.
print(maxWidthRamp([6, 0, 8, 2, 1, 5]), 4)
#                      ^           ^

# The maximum width ramp is achieved at (i, j) = (2, 9): A[2] = 1 and A[9] = 1.
print(maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]), 7)
#                         ^                    ^

print(maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 10, 1]), 8)
