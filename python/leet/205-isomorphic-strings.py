# Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/
# easy
#
# Time:  O(n+m)
# Space: O(k)
#
# Solution:
# 1. Replace chars with first index where we saw them
# 2. Compare resulting numbers

def isIsomorphic(s: str, t: str) -> bool:
    def process_str(s: str):
        d, res = {}, ""
        for i in range(len(s)):
            if not s[i] in d: d[s[i]] = str(i + 1)
            res += d[s[i]]

        return int(res)

    return process_str(s) == process_str(t)

print(isIsomorphic(s = "egg", t = "add"), True)
print(isIsomorphic(s = "foo", t = "bar"), False)
print(isIsomorphic(s = "paper", t = "title"), True)
