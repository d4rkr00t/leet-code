# Super Ugly Number
# https://leetcode.com/problems/super-ugly-number/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import heapq

def nthSuperUglyNumber(n: int, primes: [int]) -> int:
    cand = [(p, p, 1) for p in primes]
    ugly = [1]

    for _ in range(n-1):
        ugly.append(cand[0][0])
        while cand[0][0] == ugly[-1]:
            x, p, i = heapq.heappop(cand)
            heapq.heappush(cand, (p*ugly[i], p, i+1))

    return ugly[-1]

print(nthSuperUglyNumber(n = 12, primes = [2,7,13,19]))
