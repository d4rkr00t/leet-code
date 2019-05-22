# Reverse Integer
# #url: https://leetcode.com/problems/reverse-integer/
# #easy
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Solution:
#   1. Figure out if negative or positive
#   2. Convert to string and reverse
#   3. Convert to number and add sign


def reverse(x):
    s = str(abs(x))
    is_neg = x < 0
    rev = int(s[::-1])

    if rev > pow(2, 31):
        return 0

    return -rev if is_neg else rev


print(reverse(123))
print(reverse(-123))
print(reverse(120))
