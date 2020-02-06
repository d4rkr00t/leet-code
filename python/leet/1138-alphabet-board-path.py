# Alphabet Board Path
# https://leetcode.com/problems/alphabet-board-path/
# medium
#
# Time:  O(N)
# Space: O(1)
#
# Solution:
# Math

def alphabetBoardPath(target: str) -> str:
    path = ""
    prev = (0, 0)

    for c in target:
        index = ord(c) - 97
        (row, col) = divmod(index, 5)

        # LEFT
        if col < prev[1]: path += "L" * (prev[1] - col)
        # DOWN
        if row > prev[0]: path += "D" * (row - prev[0])
        # UP
        if row < prev[0]: path += "U" * (prev[0] - row)
        # RIGHT
        if col > prev[1]: path += "R" * (col - prev[1])

        path += "!"
        prev = (row, col)

    return path

# target = leet
# path   = "DDR!UURRR!"
# c      = "e"
# row, col = 0, 4
# index    = 101 - 97 = 4
# prev     = (2, 1)

print(alphabetBoardPath("leet"), "DDR!UURRR!!DDD!")
print(alphabetBoardPath("code"), "RR!DDRR!UUL!R!")
print(alphabetBoardPath(""), "")
print(alphabetBoardPath("leetz"), "DDR!UURRR!!DDD!LLLLDD!")
print(alphabetBoardPath("zoleetz"), "DDDDD!UUURRRR!LLL!UURRR!!DDD!LLLLDD!")
