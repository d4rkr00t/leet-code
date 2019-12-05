# Number of Atoms
# https://leetcode.com/problems/number-of-atoms/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# – Stack

def countOfAtoms(formula: str) -> str:
    atoms = {}

    if not str:
        return ""

    def update(atoms, stack):
        pass


    stack = []
    for char in formula:
        prev = stack[-1] if stack else None
        is_digit = char.isdigit()

        # first or ( or )
        if not prev or char == '(' or char == ')':
            if prev and prev.isalpha():
                stack.append("1")
            stack.append(char)

        # digit and prev is a digit
        elif is_digit and prev and prev.isnumeric():
            stack[-1] = stack[-1] + char

        # digit and prev is not a digit
        elif is_digit and prev and prev.isalpha():
            stack.append(char)

        # digit and prev is a )
        elif is_digit and prev and prev == ')':
            stack.append(char)

        # letter and prev is a digit
        elif not is_digit and prev and prev.isnumeric():
            stack.append(char)

        # lowercase letter
        elif not is_digit and char.islower():
            stack[-1] += char

        # letter and prev is an upper case letter
        elif not is_digit and prev and prev.isupper():
            stack.append("1")
            stack.append(char)

        # letter and prev is an lowercase case letter
        elif not is_digit and char.isupper() and prev and prev != '(':
            stack.append("1")
            stack.append(char)

        # letter and prev is a )
        elif not is_digit and prev and prev == ')':
            stack.append(char)

        # letter and prev is a (
        elif not is_digit and prev and prev == '(':
            stack.append(char)

    if stack and stack[-1].isalpha():
        stack.append("1")

    i = 0
    while i < len(stack):
        if stack[i] == ')' and i + 1 < len(stack) and stack[i+1].isnumeric():
            stack[i] = ''
            mult = int(stack[i+1])
            stack[i + 1] = ''
            j = i-1

            while j >= 0 and stack[j] != '(':
                if stack[j].isnumeric():
                    stack[j] = str(int(stack[j]) * mult)

                j -= 1

            if j >= 0 and stack[j] == '(':
                stack[j] = ''

        i += 1

    i = 0
    while i < len(stack):
        if stack[i].isnumeric():
            atoms[stack[i-1]] = int(stack[i]) + ( int(atoms[stack[i-1]]) if stack[i-1] in atoms else 0)

        i += 1

    res = ""
    for key in sorted(atoms.keys()):
        val = atoms[key]

        if val > 1:
            res += key + str(val)
        else:
            res += key

    return res



print(countOfAtoms(''), '')
print()
print(countOfAtoms('H'), 'H')
print()
print(countOfAtoms('HO'), 'HO')
print()
print(countOfAtoms('H2O'), 'H2O')
print()
print(countOfAtoms('H200O'), 'H200O')
print()
print(countOfAtoms('Mg(OH)2'), 'H2MgO2')
print()
print(countOfAtoms('K4(ON(SO3)2)2'), 'K4N2O14S4')
print()
print(countOfAtoms("(B2O39He17BeBe49)39"), "B78Be1950He663O1521")
