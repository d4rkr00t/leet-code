# Ways of transforming one string to other by removing 0 or more characters
# url: https://www.geeksforgeeks.org/ways-transforming-one-string-removing-0-characters/


# def ways_to_transform(s1, s2):
#     def transform(s1, s2, pos):
#         if s1 == s2:
#             return 1

#         if pos >= len(s1):
#             return 0

#         return transform(s1, s2, pos + 1) + transform(s1[:pos] + s1[pos+1:], s2, pos)

#     return transform(s1, s2, 0)


def ways_to_transform(s1, s2):
    dp = [[0] * (len(s1) + 1) for i in range(len(s2) + 1)]

    for j in range(len(s1) + 1):
        dp[0][j] = 1

    for i in range(1, len(s2) + 1):
        for j in range(1, len(s1) + 1):
            if (s1[j-1] == s2[i-1]):
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]

    return dp[len(s2)][len(s1)]


print(ways_to_transform("abcccdf", "abccdf"), 3)
print(ways_to_transform("aabba", "ab"), 4)
print(ways_to_transform("a", "a"), 1)
