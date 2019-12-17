# Count Numbers with Unique Digits
# https://leetcode.com/problems/count-numbers-with-unique-digits
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# 1. Math

def countNumbersWithUniqueDigits(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 10

    count = 9
    for i in range(0, n - 1):
        count *= (9 - i)

    return count + countNumbersWithUniqueDigits(n - 1)


print(countNumbersWithUniqueDigits(2), 91)
print(countNumbersWithUniqueDigits(5), 5275)
print(countNumbersWithUniqueDigits(7), 712891)

# x   = 10
# 10

# x x = 91
# 10 9

# x x x = 504
# 10 9 8
