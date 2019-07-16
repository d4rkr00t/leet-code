# Shortest Palindrome
# https://leetcode.com/problems/shortest-palindrome/
# medium


def is_palindrome(s):
    return s == s[::-1]


def shortestPalindrome(s):
    if not s or len(s) == 1 or is_palindrome(s):
        return s

    start = 0
    end = len(s) - 1

    while start < end and not is_palindrome(s):
        s = s[:start] + s[end] + s[start:]
        start += 1

    return s if is_palindrome(s) else False


print(shortestPalindrome("aacecaaa"), "aaacecaaa")
print(shortestPalindrome("abcd"), "dcbabcd")
