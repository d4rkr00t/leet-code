# Dungeon Game
# https://leetcode.com/problems/dungeon-game/
# hard

import heapq


def calc_min_hp(dungeon):
    start = (0, 0)
    end = (len(dungeon) - 1, len(dungeon[0]) - 1)
    path = {(0, 0): (0, (0, 0))}
    heap = [(0, (0, 0))]
    dir = [(1, 0), (0, 1)]

    while True:
        cost, cur = heapq.heappop(heap)

        if cur == end:
            break

        for d in dir:
            x = d[0] + cur[0]
            y = d[1] + cur[1]

            if x >= len(dungeon) or y >= len(dungeon[0]):
                continue

            child_cost = cost + (-dungeon[x][y])

            if (x, y) not in path or path[(x, y)][0] > child_cost:
                path[(x, y)] = (child_cost, cur)
                heapq.heappush(heap, (child_cost, (x, y)))

    r_path = []
    while end != start:
        r_path.append(dungeon[end[0]][end[1]])
        _, end = path[end]

    r_path.append(dungeon[end[0]][end[1]])
    r_path.reverse()

    min_health = 1
    total = 0
    for i in r_path:
        total += i

        if min_health + total <= 0:
            min_health = abs(total) + 1

    return min_health


print(calc_min_hp([
    [-2, -3, 3],
    [-5, -10, 1],
    [10, 30, -5],
]), 7)
