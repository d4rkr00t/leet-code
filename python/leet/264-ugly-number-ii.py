# Ugly Number II
# https://leetcode.com/problems/ugly-number-ii/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def nthUglyNumber(n: int) -> int:
    ugly = [1]
    i2 = i3 = i5 = 0
    while len(ugly) < n:
        while ugly[i2] * 2 <= ugly[-1]: i2 += 1
        while ugly[i3] * 3 <= ugly[-1]: i3 += 1
        while ugly[i5] * 5 <= ugly[-1]: i5 += 1
        ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))
    return ugly[-1]


print(nthUglyNumber(10), 12)
print(nthUglyNumber(50), 243)
