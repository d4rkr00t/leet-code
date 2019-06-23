# Evaluate Division
# url: https://leetcode.com/problems/evaluate-division/
# medium


def calcEquation(equations, values, queries):
    graph = {}

    def find_path_cost(start, end):
        queue = [(start, 1.0)]
        seen = set()
        for v, w in queue:
            if not v in graph:
                return -1

            if (v == end):
                return w

            seen.add(v)

            for y, k in graph[v]:
                if not y in seen:
                    queue.append((y, k*w))

        return -1

    for (a, b), v in zip(equations, values):
        if not a in graph:
            graph[a] = []

        if not b in graph:
            graph[b] = []

        graph[a].append((b, v))
        graph[b].append((a, 1.0 / v))

    return [find_path_cost(s, e) for s, e in queries]


print(calcEquation([["a", "b"], ["b", "c"]],
                   [2.0, 3.0],
                   [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]))
