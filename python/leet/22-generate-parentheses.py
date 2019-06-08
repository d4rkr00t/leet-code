# Generate Parentheses
# url: https://leetcode.com/problems/generate-parentheses/
# medium


def generateParenthesis(n):
    ans = set()

    def recur(cur, nl, nr):
        nonlocal ans

        if (nl == n and nr == n):
            ans.add(cur)
            return

        # can insert left
        if (nl < n):
            recur(cur + '(', nl + 1, nr)

        # can insert right
        if (nl > nr):
            recur(cur + ')', nl, nr + 1)

    if (n > 0):
        recur('(', 1, 0)

    return list(ans)


print(generateParenthesis(3))
print(generateParenthesis(1))
print(generateParenthesis(0))
