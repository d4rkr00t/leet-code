# Special Binary String
# https://leetcode.com/problems/special-binary-string/
# hard
#
# The number of 0's is equal to the number of 1's.
# Every prefix of the binary string has at least as many 1's as 0's.
# Choose two consecutive, non-empty, special substrings of S, and swap them.
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def makeLargestSpecial(S: str) -> str:
    count = i = 0
    res = []
    for j, v in enumerate(S):
        count = count + 1 if v=='1' else count - 1
        if count == 0:
            res.append('1' + makeLargestSpecial(S[i + 1:j]) + '0')
            i = j + 1
    return ''.join(sorted(res)[::-1])

print(makeLargestSpecial("11011000111000"), "11100100111000")

#               14
# 11100100111000
# stack = []
# regions = [(8,13)]
# start = 8
# end = 13

#
# "1010110010"
# "10" "10"
# "1010"
# ""
