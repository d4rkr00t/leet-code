# Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# medium
#
# Time:  O(n) – where n is a string lingth
# Space: O(n) – where n is a string lingth
#
# Solution:
# 1. Create a stack to keep track of parentheses
# 2. If stack top === ( and current === ) pop
# 3. Return stack length


def minAddToMakeValid(S: str) -> int:  # ()))((
    stack = []

    for c in S:
        if stack and stack[-1] == '(' and c == ')':
            stack.pop()
        else:
            stack.append(c)

    return len(stack)


print(minAddToMakeValid(")("), 2)
print(minAddToMakeValid("())"), 1)
print(minAddToMakeValid("((("), 3)
print(minAddToMakeValid("()"), 0)
print(minAddToMakeValid("()))(("), 4)
