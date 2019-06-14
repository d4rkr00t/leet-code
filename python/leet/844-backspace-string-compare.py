# Backspace String Compare
# url: https://leetcode.com/problems/backspace-string-compare/
# easy


def backspaceCompare(S, T):  # "ab##", "c#d#"
    stack_s = []
    stack_t = []

    for c in S:
        if (c == '#' and stack_s):
            stack_s.pop()
        elif (c!='#'):
            stack_s.append(c)

    for c in T:
        if (c == '#' and stack_t):
            stack_t.pop()
        elif (c!='#'):
            stack_t.append(c)

    return stack_s == stack_t


print(backspaceCompare("a##c", "#a#c"))
print(backspaceCompare("ab#c", "ad#c"))
print(backspaceCompare("ab##", "c#d#"))
print(backspaceCompare("a##c", "t"))
print(backspaceCompare("xywrrmp", "xywrrmu#p"))
print(backspaceCompare("nzp#o#g", "b#nzp#o#g"))
