# Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Stack

def minRemoveToMakeValid(s: str) -> str:
    stack = []

    for i,ch in enumerate(s):
        if ch == "(":
            stack.append((i, ch))
        elif ch == ")":
            if stack and stack[-1][1] == "(":
                stack.pop()
            else:
                stack.append((i, ch))

    pos = set([i for i,ch in stack])

    res = ""
    for i,ch in enumerate(s):
        res += ch if not i in pos else ""

    return res

#
# i = 3, ch = (
# stack = [(0, ")"), (1, ")"), (2, "("), (3, "(")]
# ans = "))(("
#
print(minRemoveToMakeValid("))(("))
print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("(a(b(c)d)"))
