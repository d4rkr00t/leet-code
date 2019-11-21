# Reorganize String
# https://leetcode.com/problems/reorganize-string/
# medium
#
# Time:  N lg N
# Space: O(1)
#
# Solution:
#

def reorganizeString(S: str) -> str:
    N = len(S)
    A = []
    for c, x in sorted((S.count(x), x) for x in set(S)):
        if c > (N+1)/2: return ""
        A.extend(c * x)

    ans = [None] * N
    ans[::2], ans[1::2] = A[N//2:], A[:N//2]
    return "".join(ans)


print(reorganizeString("aab"), "aba")
print(reorganizeString("aaab"), "")
print(reorganizeString("a"), "")
print(reorganizeString("abbbb"), "")
print(reorganizeString("vvvlo"), "")
