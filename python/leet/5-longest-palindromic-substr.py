# Longest palindromic substr
# #url: https://leetcode.com/problems/longest-palindromic-substring/
# #medium


def longestPalindrome(s):  # cbbd
    ans = (0, 0)

    def expand(str, start, end):  # 1 2
        while start >= 0 and end < len(s) and str[start] == str[end]:
            start -= 1
            end += 1

        return s[start+1:end]

    for i in range(len(s)):  # 3
        range1 = expand(s, i, i)
        range2 = expand(s, i, i+1)

        tmp = range1 if len(range1) > len(range2) else range2
        ans = ans if len(ans) > len(tmp) else tmp  # (0, 3)

    return ans


print(longestPalindrome("babad"), "bab")
print(longestPalindrome("cbbd"), "bb")

# babad
#
