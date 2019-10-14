# Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD


def fractionToDecimal(numerator: int, denominator: int) -> str:
    sign = '' if numerator * denominator >= 0 else '-'
    numerator, denominator = abs(numerator), abs(denominator)

    integer, remainder = divmod(numerator, denominator)

    decimal = ''
    seen = {}

    while remainder > 0:
        last_remainder = remainder
        digi, remainder = divmod(remainder * 10, denominator)
        seen[last_remainder] = len(decimal)
        decimal += str(digi)

        if remainder in seen:
            index = seen[remainder]
            decimal = decimal[:index] + '(' + decimal[index:] + ')'
            break

    ans = sign + str(integer)
    if decimal:
        ans += '.' + decimal
    return ans


print(fractionToDecimal(1, 2), "0.5")
print(fractionToDecimal(2, 1), "2")
print(fractionToDecimal(2, 3), "0.(6)")
print(fractionToDecimal(4, 3), "1.(3)")
print(fractionToDecimal(4, 9), "0.(4)")
print(fractionToDecimal(4, 33), "0.(12)")
print(fractionToDecimal(4, 333), "0.(012)")
print(fractionToDecimal(1, 6), "0.1(6)")
