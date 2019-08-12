# Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/
# medium


import math


def get_permutation(n, k):
    numbers = list(range(1, n+1))
    permutation = ''
    k -= 1
    while n > 0:
        n -= 1
        # get the index of current digit
        index, k = divmod(k, math.factorial(n))
        permutation += str(numbers[index])
        # remove handled number
        numbers.remove(numbers[index])

    return permutation


print(get_permutation(3, 3), "213")
print(get_permutation(4, 9), "2314")
