# Number of Paths with Max Score
# https://leetcode.com/problems/number-of-paths-with-max-score/
# hard
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def pathsWithMaxScore(board: [str]) -> [int]:
    def get_val(row, col):
        nonlocal board

        if row >= len(board) or col >= len(board[0]):
            return None

        val = board[row][col]

        if val == "X" or val == None:
            return None

        if val == "S" or val == "E":
            return 0

        return int(val)

    for i in range(len(board)):
        board[i] = list(board[i])
        board[i].append(None)

    board.append([None] * len(board[0]))
    board[-1][-1] = 0

    path = [[0] * len(board) for _ in board[0]]
    path[-1][-1] = 1

    for r in range(len(board) - 2, -1, -1):
        for c in range(len(board[0]) - 2, -1, -1):
            if (board[r][c] == "X"):
                board[r][c] = None
                continue

            dirs = [[r,c+1], [r+1, c+1], [r+1, c]]
            vals = []
            cur = -1

            for d in dirs:
                val = get_val(d[0], d[1])

                if val == None:
                    continue

                if val > cur:
                    cur = val
                    vals = [(d, val)]
                elif val == cur:
                    vals.append((d, val))

            if vals:
                board[r][c] = get_val(r, c) + vals[0][1]
                local_path = 0
                for v in vals:
                    local_path += path[v[0][0]][v[0][1]]

                path[r][c] = local_path
                continue

            board[r][c] = None

    # print(board)
    # print(path)
    max_sum = board[0][0] if board[0][0] != None else 0

    return [max_sum, path[0][0] % (pow(10, 9) + 7)]

print(pathsWithMaxScore(["E23","2X2","12S"]), [7,1])
print(pathsWithMaxScore(["E12","1X1","21S"]), [4,2])
print(pathsWithMaxScore(["E11","XXX","11S"]), [0,0])
print(pathsWithMaxScore(["EX","XS"]), [0,1])


# [
#   "E23"
#   "2X2"
#   "12S"
# ]
#
# 7 7 5
# 5 X 2
# 3 2 0
#

# [
#   "E1123"
#   "11X11"
#   "3211S"
# ]
#
# E 8 7 6 4
# 8 5 X 2 1
# 7 4 2 1 0
#
