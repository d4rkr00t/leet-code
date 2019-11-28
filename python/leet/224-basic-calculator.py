# Basic Calculator
# https://leetcode.com/problems/basic-calculator/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# Stack

def calculate(s: str) -> int:
    op = []
    lit = []

    def apply_op(op, lit):
        while op and len(lit) > 1:
            if lit[-2] == '(' or lit[-1] == '(':
                break

            o = op.pop()
            l1 = lit.pop()
            l2 = lit.pop()

            if o == '-':
                lit.append(l2 - l1)
            else:
                lit.append(l2 + l1)

    i = -1
    while i < len(s) - 1:
        i += 1
        c = s[i]
        if c == '+' or c == '-':
            op.append(c)
        elif c == '(':
            lit.append(c)
        elif c == ')':
            apply_op(op, lit)
            num = lit.pop()
            lit.pop()
            lit.append(num)
            apply_op(op, lit)
        elif c.isnumeric():
            num = c
            while i+1 < len(s) and s[i+1].isnumeric():
                num += s[i+1]
                i+=1
            lit.append(int(num))

            apply_op(op, lit)

    apply_op(op, lit)

    return lit[-1] if lit else 0


print(calculate('1 + 1'), 2)
print(calculate('2 - 1 + 2 '), 3)
print(calculate('(1 + (4 + 5 + 2) - 3) + (6 + 8)'), 23)
print(calculate('2 - 1 + 2 - 1 - 2 '), 0)
print(calculate("2147483647"), 2147483647)
print(calculate("(1-(3-4))"), 2)
print(calculate("(7)-(0)+(4)"), 11)
