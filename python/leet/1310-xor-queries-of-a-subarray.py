# XOR Queries of a Subarray
# https://leetcode.com/problems/xor-queries-of-a-subarray/
# medium
#
# Time:  O(n + m)
# Space: O(1)
#
# Solution:
# Prefix sum (?)

def xorQueries(arr: [int], queries: [[int]]) -> [int]:
    for i in range(1, len(arr)):
        arr[i] = arr[i-1] ^ arr[i]

    return [arr[j] ^ arr[i-1] if i else arr[j] for i,j in queries]


print(xorQueries([1,3,4,8], [[0,1],[1,2],[0,3],[3,3]]), [2,7,14,8])
print(xorQueries([4,8,2,10], [[2,3],[1,3],[0,0],[0,3]]), [8,0,4,4])

# i: 0     1     2     3
# o: 0001, 0011, 0100, 1000
# x: 0001, 0010, 0110, 1110
#
# 0:1 = 0010
# 1:2 = 0111 = 0110 xor 0001 = 0111
# 0:3 = 1110 = 1110
# 3:3 = 1000 = 1110 xor 0110 = 1000
