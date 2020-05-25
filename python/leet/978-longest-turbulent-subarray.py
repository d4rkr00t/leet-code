# Longest Turbulent Subarray
# https://leetcode.com/problems/longest-turbulent-subarray/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Sliding window
# A[k] > A[k+1] when k is even, and A[k] < A[k+1] when k is odd.

def cmp(a, b):
    return (a > b) - (a < b)

def maxTurbulenceSize(A: [int]) -> int:
    if len(A) < 2: return 1

    size, s = 1, 0
    for i in range(1, len(A)):
        c = cmp(A[i-1], A[i])
        if c == 0:
            s = i
        elif i == len(A)-1 or c * cmp(A[i], A[i+1]) != -1:
            size = max(size, i - s + 1)
            s = i
    return size


print(maxTurbulenceSize([0,1,1,0,1,0,1,1,0,0]), 5)
print(maxTurbulenceSize([9,4,2,10,7,8,8,1,9]), 5)
print(maxTurbulenceSize([4,8,12,16]), 2)
print(maxTurbulenceSize([100]), 1)
