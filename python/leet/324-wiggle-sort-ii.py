# Wiggle Sort II
# https://leetcode.com/problems/wiggle-sort-ii/
# medium
#
# Time:  O(nlogn)
# Space: O(n)
#
# Solution:
# Fast and Slow pointer

def wiggleSort(nums: [int]) -> None:
    if not nums or len(nums) < 2: return

    arr = sorted(nums)
    for i in range(1, len(nums), 2): nums[i] = arr.pop()
    for i in range(0, len(nums), 2): nums[i] = arr.pop()

    return nums

print(wiggleSort([1, 5, 1, 1, 6, 4]))
print(wiggleSort([1, 3, 2, 2, 3, 1]))
print(wiggleSort([1, 5, 1, 1, 1, 6, 4, 3]))
print(wiggleSort([1, 7, 1, 6, 4, 5, 1]))
print(wiggleSort([4,5,5,6]))
