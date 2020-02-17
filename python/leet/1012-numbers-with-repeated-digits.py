#
# Numbers With Repeated Digits
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# DP + Math

# given number n, see whether n has repeated number
def has_repeated(n):
    str_n = str(n)
    return len(set(str_n)) != len(str_n)

def permutation(n, k):
    prod = 1
    for i in range(k):
        prod *= (n-i)
    return prod

def n_digit_no_repeat(n):
    if n == 1:
        return 9
    else:
        return  9 * permutation(9, n-1)

def numDupDigitsAtMostN(N: int) -> int:
    """
    :type N: int
    :rtype: int
    """
    N_str = str(N)
    n_digit = len(N_str)
    digits = list(map(int, N_str))
    result = N - 1
    prefix = 0
    for i in range(1, n_digit):
        result -= n_digit_no_repeat(i)
    for i in range(n_digit):
        # when we fix the most significant digit, it
        # can't be zero
        start = 0 if i else 1
        for j in range(start, digits[i]):
            if has_repeated(prefix * 10 + j):
                continue
            if i != n_digit-1:
                result -= permutation(10-i-1, n_digit-1-i)
            else:
                # optmized from `result -= has_repeated(prefix*10+j)`
                result -= 1
        prefix = prefix*10 + digits[i]
    return result + has_repeated(N)


# 20
# 10^1 = 10
# 10^2 = 100
#

print(numDupDigitsAtMostN(0), 0)
print(numDupDigitsAtMostN(20), 1)
print(numDupDigitsAtMostN(100), 10)
print(numDupDigitsAtMostN(200), 38) # +28
print(numDupDigitsAtMostN(300), 66) # +28
print(numDupDigitsAtMostN(400), 94) # +28
print(numDupDigitsAtMostN(1000), 262)
print(numDupDigitsAtMostN(2000), 758) # +496
print(numDupDigitsAtMostN(3000), 1254) # +496
