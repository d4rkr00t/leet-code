# Word Search
# https://leetcode.com/problems/word-search/
# medium


def exist(board, word):
    found = False

    def dfs(i, j, offset):
        nonlocal found
        if found:
            return True

        if offset == len(word):
            found = True
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False

        if board[i][j] != word[offset]:
            return False

        ch = board[i][j]
        board[i][j] = '#'

        res = any([
            dfs(i-1, j, offset+1),
            dfs(i+1, j, offset+1),
            dfs(i, j-1, offset+1),
            dfs(i, j+1, offset+1),
        ])

        board[i][j] = ch

        return res

    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(i, j, 0):
                return True

    return False


print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCCED"))

print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "SEE"))

print(exist([
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
], "ABCB"))
