# Remove Invalid Parentheses
# url: https://leetcode.com/problems/remove-invalid-parentheses/
# hard

import sys


def removeInvalidParentheses(s):  # ()())()
    ans = set()  # []
    min_removed = sys.maxsize

    def is_solution_possible(length, pos, open, close):  # 7, 4, 2, 3
        return open >= close and length > pos + (open - close)

    def recur(s, pos, open, close, cur, removed):  # 5, 2, 2, '()()', 1
        nonlocal ans, min_removed

        if (pos == len(s)):  # 7
            if (removed <= min_removed and is_solution_possible(len(s), pos - 1, open, close)):
                ans.add(cur)
                min_removed = removed
            return

        char = s[pos]  # (

        if (char != '(' and char != ')'):
            return recur(s, pos + 1, open, close, cur + char, removed)

        updated_open = open + 1 if char == '(' else open
        updated_close = close + 1 if char == ')' else close

        # take cur char
        if (is_solution_possible(len(s), pos, updated_open, updated_close)):
            recur(s, pos + 1, updated_open, updated_close, cur + char, removed)

        # skip cur char
        if (is_solution_possible(len(s), pos + 1, open, close)):
            recur(s, pos + 1, open, close, cur, removed + 1)

    recur(s, 0, 0, 0, '', 0)

    return list(ans)


print(removeInvalidParentheses("()())()"))
print(removeInvalidParentheses("(a)())()"))
print(removeInvalidParentheses(")("))
print(removeInvalidParentheses(")(f"))
