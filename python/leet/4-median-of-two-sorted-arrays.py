# Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/
# hard
#
# Time:  O(log (m+n))
#
# Solution:
# Binary Search

def findMedianSortedArrays(nums1: [int], nums2: [int]) -> float:
    posn1 = posn2 = cur = prev = 0
    mid = (len(nums1) + len(nums2)) / 2.0

    while mid >= 0.0:
        item1 = nums1[posn1] if posn1 < len(nums1) else float("inf")
        item2 = nums2[posn2] if posn2 < len(nums2) else float("inf")

        prev = cur
        mid -= 1.0

        if item1 <= item2:
            cur = posn1
            posn1 += 1
        else:
            cur = posn2 + len(nums1)
            posn2 += 1

    item1 = nums2[cur-len(nums1)] if cur >= len(nums1) else nums1[cur]
    item2 = nums2[prev-len(nums1)] if prev >= len(nums1) else nums1[prev]
    return (item1 + item2) / 2.0 if (len(nums1) + len(nums2)) % 2.0 == 0 else float(item1)


print(findMedianSortedArrays([1,3], [2]), 2.0)
print(findMedianSortedArrays([1,2], [3,4]), 2.5)
print(findMedianSortedArrays([1,3], [2,4]), 2.5)
print(findMedianSortedArrays([1,5], [2,10]), 3.5)
print(findMedianSortedArrays([1], []), 1.0)
print(findMedianSortedArrays([], [2]), 2.0)

#
# 1,    3
#    2,
# mid = 2
# cur = 2
# i0 = 0
# i1 = 0

# [1,2] [3,4]
#      ^ ^
# posn1 = 0   | 1   | 2   | 2     | | | | | | | | | | |
# posn2 = 0   | 0   | 0   | 1     | | | | | | | | | | |
# mid   = 2.0 | 1.0 | 0.0 | -1.0  | | | | | | | | | | |
# cur   = 0   | 0   | 1   | 2     | | | | | | | | | | |
# prev  = 0   | 0   | 0   | 1     | | | | | | | | | | |
