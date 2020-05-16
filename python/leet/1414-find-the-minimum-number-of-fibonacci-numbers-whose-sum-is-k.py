# Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
# https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/
# medium
#
# Time:  O(k)
# Space: O(k)
#
# Solution:
# 1. Gen fib numbers until > k

import bisect

def findMinFibonacciNumbers(k: int, cache = {}) -> int:
    if k < 2: return k
    a, b = 1, 1
    while b <= k:
        a, b = b, a + b
    return findMinFibonacciNumbers(k - a) + 1

# 1 1 2 3 5
# print(findMinFibonacciNumbers(7), 2)

# 1 1 2 3 5 8
# print(findMinFibonacciNumbers(10), 2)

# 1 1 2 3 5 8 13
# print(findMinFibonacciNumbers(19), 3)

# 1 1 2 3 5 8 13
# print(findMinFibonacciNumbers(20), 3)

# 1 1 2 3 5 8 13 21
# print(findMinFibonacciNumbers(30), 3)

# 1 1 2 3 5 8 13 21 44
# print(findMinFibonacciNumbers(59), 3)

# 1 1 2 3 5 8 13 21 44
# print(findMinFibonacciNumbers(513314), 11)

print(findMinFibonacciNumbers(9083494), 10)
