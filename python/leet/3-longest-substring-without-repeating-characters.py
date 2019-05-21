# Longest Substring Without Repeating Characters
# #url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# #medium
#
# Example:
#   Input: "abcabcbb"
#   Output: 3
#   Explanation: The answer is "abc", with the length of 3.


def lengthOfLongestSubstring(s):  # bbtablud
    ps = 0
    ans = 0  # 3
    table = {}  # { b:0, }

    for pe in range(len(s)):  # 0
        if s[pe] in table and table[s[pe]] >= ps:  # True
            ps = table[s[pe]] + 1
        else:
            ans = max(ans, pe - ps + 1)

        table[s[pe]] = pe

    return ans


print(lengthOfLongestSubstring("abcabcbb"), 3)
print(lengthOfLongestSubstring("bbbbb"), 1)
print(lengthOfLongestSubstring("pwwkew"), 3)
