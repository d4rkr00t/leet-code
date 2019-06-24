# Redundant Connection
# https://leetcode.com/problems/redundant-connection/
# medium
import collections


def find_redundant(edges):
    graph = [[] for x in range(len(edges))]

    def dfs(source, target, seen):
        if source not in seen:
            seen.add(source)
            if source == target:
                return True

            return any(dfs(nei, target, seen) for nei in graph[source])

    for u, v in edges:
        seen = set()

        if graph[u-1] and graph[v-1] and dfs(u - 1, v - 1, seen):
            return [u, v]

        graph[u-1].append(v - 1)
        graph[v-1].append(u - 1)


print(find_redundant([[1, 2], [1, 3], [2, 3]]), [2, 3])
print(find_redundant([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]), [1, 4])
print(find_redundant([[9, 10], [5, 8], [2, 6], [1, 5], [3, 8], [
      4, 9], [8, 10], [4, 10], [6, 8], [7, 9]]), [4, 10])
