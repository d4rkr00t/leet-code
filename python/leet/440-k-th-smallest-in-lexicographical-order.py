# K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import heapq

def findKthNumber(n: int, k: int) -> int:
    k -= 1
    cur = 1
    while k > 0:
        step, first, last = 0, cur, cur + 1
        while first <= n:
            step += min(n + 1, last) - first
            first *= 10
            last *= 10
        if step <= k:
            cur += 1
            k -= step
        else:
            cur *= 10
            k -= 1
    return cur


# print(findKthNumber(13, 2), 10)
# print(findKthNumber(100, 100), 99)
# print(findKthNumber(100, 20), 26)
# print(findKthNumber(130, 20), 116)
# print(findKthNumber(10000, 20), 1014)
# print(findKthNumber(1000000, 20), 100012)
print(findKthNumber(7747794, 5857460), 100012)

#
# 1 10 11 12 13 2 3 4 5 6 7 8 9
#
# 1 10 100 11 12 13 14 15 16 17 18 19 2 20 21 22 23 24 25 28
#
# 1 10 100 101 102 103 104 105 106 107 108 109 11 110 111 112 113 114 115 116
#

#
# [2, 110]
# 1 -> 2
#   -> 10 -> 11
#         -> 100 -> 109 -> 110
#         -> 2          -> 11  ->
