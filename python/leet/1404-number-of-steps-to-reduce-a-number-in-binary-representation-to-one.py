# Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def numSteps(s: str) -> int:
    a = list(s)
    steps = 0
    while len(a) > 1:
        if a[-1] == "1":
            carry = 1
            i = len(a) - 1
            while i >= 0 and carry:
                a[i], carry = ("1", 0) if a[i] == "0" else ("0", 1)
                i -= 1

            if carry:
                a.insert(0, "1")
        else:
            # if last is zero we divide by 2 e.g. num >> 1
            a.pop()

        steps += 1

    return steps

# "1"
print(numSteps("1101"), 6)
print(numSteps("10"), 1)
print(numSteps("1"), 0)
