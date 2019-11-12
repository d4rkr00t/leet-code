# Shortest Subarray with Sum at Least K
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
# hard
#
# Time:  O(n) – n is a length of A
# Space: O(n) – n is a length of A

import collections


def shortestSubarray(A: [int], K: int) -> int:
    N = len(A)
    P = [0]
    for x in A:
        P.append(P[-1] + x)

    # Want smallest y-x with Py - Px >= K
    ans = N+1  # N+1 is impossible
    monoq = collections.deque()  # opt(y) candidates, represented as indices of P
    for y, Py in enumerate(P):
        # Want opt(y) = largest x with Px <= Py - K
        while monoq and Py <= P[monoq[-1]]:
            monoq.pop()

        while monoq and Py - P[monoq[0]] >= K:
            ans = min(ans, y - monoq.popleft())

        monoq.append(y)

    return ans if ans < N+1 else -1


print(shortestSubarray([1], 1), 1)
print(shortestSubarray([1, 2], 4), -1)
print(shortestSubarray([2, -1, 2], 3), 3)
print(shortestSubarray([17, 85, 93, -45, -21], 150), 2)
print(shortestSubarray([84, -37, 32, 40, 95], 167), 3)
