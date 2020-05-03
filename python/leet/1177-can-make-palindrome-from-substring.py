# Can Make Palindrome from Substring
# https://leetcode.com/problems/can-make-palindrome-from-substring/
# medium
#
# Time:  O(n*m) - where n is a number of queries, and m is a length of a longest query
# Space: O(m) - where m is a length of a longest query
#
# Solution:
# TBD

from collections import Counter

def canMakePaliQueries(s: str, queries: [[int]]) -> [bool]:
    ans = []
    dp = [Counter()]
    for i in range(1, len(s)+1):
        dp.append(dp[i-1] + Counter(s[i-1]))

    for l,r,k in queries:
        c = dp[r+1] - dp[l]
        need = sum(v % 2 for v in c.values()) // 2
        ans.append(need <= k)

    return ans

print(canMakePaliQueries(s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]), [True,False,False,True,True])

# "abcda"
#
# [3,3,0] d = True
# [1,2,0] bc = False
# [0,3,1] ab cd = False
# [0,3,2] abcd = True abba or dccd
# [0,4,1] abcda = True abcba or adcda
