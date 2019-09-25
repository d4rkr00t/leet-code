# Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/
# medium
#
# Time:  O(n^2), where n = bank size
# Space: O(n), where n = bank size
#
# Solution:
# 1. Build a undirected graph from bank array
# 2. Check if there is a path from start to end [DFS]


def minMutation(start: str, end: str, bank: [str]) -> int:
    def dist(n1, n2):
        diff = 0

        for i in range(len(n1)):
            if n1[i] != n2[i]:
                diff += 1

        return diff

    def buildGraph(graph, nodes):
        if not nodes:
            return

        node = nodes.pop()

        if not node in graph:
            graph[node] = []

        for (k, v) in enumerate(graph):
            if dist(v, node) == 1:
                graph[node].append(v)
                graph[v].append(node)

        buildGraph(graph, nodes)

    def isConnected(graph, start, end, step=1, visited={}):
        if not graph[start]:
            return -1

        visited[start] = True

        for v in graph[start]:
            if v == end:
                return step
            else:
                if v in visited:
                    continue
                res = isConnected(graph, v, end, step + 1, visited)
                if res != -1:
                    return res

        return -1

    if start == end:
        return 0

    graph = {}
    graph[start] = []

    buildGraph(graph, bank)

    return isConnected(graph, start, end)


print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]), 1)

print(minMutation("AACCGGTT", "AAACGGTA", [
      "AACCGGTA", "AACCGCTA", "AAACGGTA"]), 2)

print(minMutation("AAAAACCC", "AACCCCCC", [
      "AAAACCCC", "AAACCCCC", "AACCCCCC"]), 3)

print(minMutation("AAAAAAAA", "CCCCCCCC", [
    "AAAAAAAA", "AAAAAAAC", "AAAAAACC", "AAAAACCC", "AAAACCCC", "AACACCCC", "ACCACCCC", "ACCCCCCC", "CCCCCCCA"]), -1)
