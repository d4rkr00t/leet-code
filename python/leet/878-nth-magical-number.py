# Nth Magical Number
# https://leetcode.com/problems/nth-magical-number/
# hard
#
# Time:  target O(logn)
# Space: O(N)
#
# Constrains:
# 1 <= N <= 10^9
# 2 <= A <= 40000
# 2 <= B <= 40000
#
# Solution:
# :(

import math


def nthMagicalNumber(N: int, A: int, B: int):  # 5, 2, 4
    MOD = 10**9 + 7

    L = A // math.gcd(A, B) * B
    M = L // A + L // B - 1
    q, r = divmod(N, M)

    if r == 0:
        return q * L % MOD

    heads = [A, B]
    for _ in range(r - 1):
        if heads[0] <= heads[1]:
            heads[0] += A
        else:
            heads[1] += B

    return (q * L + min(heads)) % MOD


# 2
print(nthMagicalNumber(1, 2, 3), 2)

# 2, 3, 4, 6
print(nthMagicalNumber(4, 2, 3), 6)

# 2, 4, 6, 8, 10
print(nthMagicalNumber(5, 2, 4), 10)

# 4, 6, 8
print(nthMagicalNumber(3, 6, 4), 8)
