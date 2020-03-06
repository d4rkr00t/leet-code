# Closest Divisors
# https://leetcode.com/problems/closest-divisors/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

from math import sqrt, ceil

def closestDivisors(num: int) -> [int]:
    def find_divisor(num): # 9
        top = ceil(sqrt(num)) # 3
        pair = [1, num] # 1, 9
        diff = num - 1 # 8

        for i in range(2, top + 1): # i = 3
            if num % i == 0:
                new_diff = abs(i - num // i)
                if new_diff < diff:
                    diff = new_diff
                    pair = [i, num // i]

        return pair

    div1 = find_divisor(num + 1)
    div2 = find_divisor(num + 2)
    diff1 = abs(div1[0] - div1[1])
    diff2 = abs(div2[0] - div2[1])

    return div1 if diff1 <= diff2 else div2


print(closestDivisors(8), [3, 3])
print(closestDivisors(123), [5, 25])
print(closestDivisors(999), [40, 25])
