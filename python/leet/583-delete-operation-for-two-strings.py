# Delete Operation for Two Strings
# https://leetcode.com/problems/delete-operation-for-two-strings/
# medium


def minDistance(word1, word2):
    dp = [[None] * (len(word1) + 1) for x in range(len(word2) + 1)]

    for i in range(len(word2) + 1):
        for j in range(len(word1) + 1):
            if i == 0 or j == 0:
                dp[i][j] = i + j
            elif word1[j - 1] == word2[i - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1])

    return dp[-1][-1]


print(minDistance("sea", "eat"))
