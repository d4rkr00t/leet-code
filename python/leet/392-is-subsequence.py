# Is Subsequence
# https://leetcode.com/problems/is-subsequence/
# easy
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isSubsequence(s: str, t: str) -> bool:
    if s == t or not s: return True

    s_pos = 0
    for c in t:
        if s_pos == len(s): break
        if c == s[s_pos]: s_pos += 1

    return s_pos == len(s)

print(isSubsequence(s = "abc", t = "ahbgdc"), True)
print(isSubsequence(s = "axc", t = "ahbgdc"), False)
print(isSubsequence(s = "aec", t = "abcde"), False)
print(isSubsequence(s = "", t = ""), True)
print(isSubsequence(s = "", t = "anything"), True)
