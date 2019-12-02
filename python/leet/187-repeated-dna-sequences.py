# Repeated DNA Sequences
# https://leetcode.com/problems/repeated-dna-sequences/
# medium
#
# Time:  O(N)
# Space: O(N^2)
#
# Solution:
# TBD

def findRepeatedDnaSequences(s: str) -> [str]:
    if len(s) < 10:
        return []

    prefixes = {}
    for i in range(0, len(s) - 9):
        substr = s[i:i+10]
        if substr in prefixes:
            prefixes[substr] += 1
        else:
            prefixes[substr] = 1

    res = []
    for key in prefixes.keys():
        if prefixes[key] > 1:
            res.append(key)

    return res


print(findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"), ["AAAAACCCCC", "CCCCCAAAAA"])
print(findRepeatedDnaSequences("AAAAAAAAAAA"), ["AAAAAAAAAAA"])
