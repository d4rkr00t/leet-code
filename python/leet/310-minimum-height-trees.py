# Minimum Height Trees
# https://leetcode.com/problems/minimum-height-trees/
# medium

import sys


def find_mht(n, edges):  # 4, [[1, 0], [1, 2], [1, 3]]
    if n == 1:
        return [0]

    graph = [set() for x in range(n)]  # [[1], [0, 2, 3], [1], [1]]

    for f, t in edges:
        graph[f].add(t)
        graph[t].add(f)

    leaves = [i for i in range(n) if len(graph[i]) == 1]

    while n > 2:
        n -= len(leaves)
        newLeaves = []
        for i in leaves:
            j = graph[i].pop()
            graph[j].remove(i)
            if (len(graph[j]) == 1):
                newLeaves.append(j)

        leaves = newLeaves

    return leaves


print(find_mht(4, [[1, 0], [1, 2], [1, 3]]), [1])
print(find_mht(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]), [3, 4])
