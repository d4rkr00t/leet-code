# Regular Expression Matching
# #url: https://leetcode.com/problems/regular-expression-matching/
# #hard #recursion #dynamic programming
#
# Given an input string (s) and a pattern (p),
# implement regular expression matching with support for '.' and '*'.
#
# Conditions:
#   – s could be empty and contains only lowercase letters a-z.
#   – p could be empty and contains only lowercase letters a-z, and characters like . or *.
#


def isMatch(s, p):
    table = [[False for i in range(len(p) + 1)] for j in range(len(s) + 2)]
    table[len(s)][len(p)] = True

    for i in range(len(s), -1, -1):  # 2
        for j in range(len(p) - 1, -1, -1):  # 0
            is_first_match = (
                i < len(s) and s[i] == p[j]) or p[j] == '.'  # false

            if j + 1 < len(p) and p[j + 1] == '*':  # true
                table[i][j] = table[i][j +
                                       2] or (is_first_match and table[i+1][j])
            else:
                table[i][j] = is_first_match and table[i+1][j+1]  # 1

    return table[0][0]


print(isMatch("ab", "ab"), True)
print(isMatch("aa", "a*"), True)
print(isMatch("aa", "a"), False)
print(isMatch("aab", "c*a*b"), True)
print(isMatch("mississippi", "mis*is*p*."), False)
print(isMatch("aaa", "aaaa"), False)
print(isMatch("aaaab", "a*aab"), True)
print(isMatch("aaa", "ab*a*c*a"), True)

# console.log(isMatch("ab", ".*c"), false);
# console.log(isMatch("aab", "c*a*b"), true);
# console.log(isMatch("aa", "a"), false);
# console.log(isMatch("mississippi", "mis*is*p*."), false);
# console.log(isMatch("aaa", "aaaa"), false);
# console.log(isMatch("aaaab", "a*aab"), true);
# console.log(isMatch("aaa", "ab*a*c*a"), true);
