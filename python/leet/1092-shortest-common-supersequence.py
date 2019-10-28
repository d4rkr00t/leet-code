# Shortest Common Supersequence
# https://leetcode.com/problems/shortest-common-supersequence/
# hard
#
# Time:  O(n*m) -> n = len(str1); m = len(str2)
# Space: O(n*m) -> n = len(str1); m = len(str2)
#
# Solution:
# DP
#
# 1. Build dp table
#   1.1 dp[i] = min(dp[i-1]]j, dp[i][j-1]) + 1 if str1[i] != str2[j]
#   1.2 dp[i] = dp[i-1][j-1] + 1 if str1[i] == str2[j]
#
# 2. Calculate path back from dp[len][len]
#
#   _ c a b [2]
# _ 0 1 2 3
# a 1 2 2 3
# b 2 3 3 3
# a 3 4 4 4
# c 4 4 5 5
# [1]
#
#   c a b a c


# bacab and caba
#   _ c a b a [2]
# _ 0 1 2 3 4
# b 1 2 3 3 4
# a 2 3 3 4 4
# c 3 3 4 5 5
# a 4 4 4 5 6
# b 5 5 5 5 6
# [1]
#
#   b a c a b a
#

def build_dp_table(str1: str, str2: str):
    dp = [[0 for _ in range(0, len(str2) + 1)]
          for _ in range(0, len(str1) + 1)]

    for i in range(0, len(str2) + 1):
        dp[0][i] = i

    for i in range(0, len(str1) + 1):
        dp[i][0] = i

    return dp


def populate_dp_table(dp, str1, str2):
    for j in range(1, len(str2) + 1):
        for i in range(1, len(str1) + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + 1


def find_substr(dp, str1, str2):
    result = ""
    i = len(dp) - 1
    j = len(dp[0]) - 1

    while i > 0 or j > 0:
        if i == 0:
            result = str2[j-1] + result
            j -= 1
        elif j == 0:
            result = str1[i-1] + result
            i -= 1
        elif str1[i-1] == str2[j-1]:
            result = str1[i-1] + result
            i -= 1
            j -= 1
        else:
            if dp[i][j-1] < dp[i-1][j]:
                result = str2[j-1] + result
                j -= 1
            else:
                result = str1[i-1] + result
                i -= 1

    return result


def shortestCommonSupersequence(str1: str, str2: str) -> str:
    if not str1 and not str2:
        return ""
    elif not str1 and str2:
        return str2
    elif not str2 and str1:
        return str1

    dp = build_dp_table(str1, str2)
    populate_dp_table(dp, str1, str2)
    return find_substr(dp, str1, str2)


print(shortestCommonSupersequence("abac", "cab"), "cabac")
print(shortestCommonSupersequence("bacab", "caba"), "bacaba")
