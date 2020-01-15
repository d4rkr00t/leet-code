# Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def maxChunksToSorted(arr: [int]) -> int:
    mx, res = -1, 0
    for i, v in enumerate(arr):
        mx = max(mx, v)
        res += mx == i
    return res

print(maxChunksToSorted([4,3,2,1,0]), 1)
print(maxChunksToSorted([4,2,1,3,0]), 1)
print(maxChunksToSorted([1,0,2,3,4]), 4)
print(maxChunksToSorted([2,1,0,4,3,5]), 3)
print(maxChunksToSorted([1,0,4,3,2,5]), 3)

