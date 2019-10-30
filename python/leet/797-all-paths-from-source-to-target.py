# All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/
# medium
#
# Time:  O(2^N N^2)
# Space: O(2^N N)
#
# Solution:
#   Important:
#    - acyclic graph
#
# DFS


def allPathsSourceTarget(graph: [[int]]) -> [[int]]:
    if not graph:
        return []

    result = []

    def dfs(graph, start, target, path, result):
        path.append(start)

        for x in graph[start]:
            p = path.copy()
            if x == target:
                p.append(x)
                result.append(p)
            else:
                dfs(graph, x, target, p, result)

    dfs(graph, 0, len(graph)-1, [], result)

    return result


print(allPathsSourceTarget([[1, 2], [3], [3], []]), [[0, 1, 3], [0, 2, 3]])
print(allPathsSourceTarget(
    [[4, 3, 1], [3, 2, 4], [3], [4], []]))

#      0 -->1 -> 2
#      | \/ |  /
#      | /\ | /
#      4 -- 3
#
