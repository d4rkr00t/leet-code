# Letter Case Permutation
# https://leetcode.com/problems/letter-case-permutation/
# easy
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Recursion


def letterCasePermutation(S: str) -> [str]:
    res = [S]

    def recur(str, pos):
        res = []

        if pos >= len(str):
            return res

        res.append(str);

        if str[pos].isdigit():
            return res + recur(str, pos + 1)

        res.append(str[0:pos] + str[pos].swapcase() + str[pos + 1:])

        return res + recur(str, pos + 1) + recur(str[0:pos] + str[pos].swapcase() + str[pos + 1:], pos + 1)

    return list(set(recur(S, 0)))

print(letterCasePermutation("a1b2"), ["a1b2", "a1B2", "A1b2", "A1B2"])
print(letterCasePermutation("3z4"), ["3z4", "3Z4"])
print(letterCasePermutation("12345"), ["12345"])
print(letterCasePermutation(""), [])
print(letterCasePermutation("C"), ["c", "C"])
