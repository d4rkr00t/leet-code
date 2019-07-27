# Kth Smallest Element in a Sorted Matrix
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
# medium

import heapq


def kthSmallest(matrix, k):
    heap = []

    for row in matrix:
        for i in row:
            heapq.heappush(heap, i)

    min = 0
    for i in range(k):
        min = heapq.heappop(heap)

    return min


print(kthSmallest([
    [1,  5,  9],
    [10, 11, 13],
    [12, 13, 15]
], 8), 13)
