# Course Schedule II
# https://leetcode.com/problems/course-schedule-ii/
# medium


def find_order(count, edges):
    visited = [False] * count
    order = [None] * count
    pos = count - 1
    graph = [[] for x in range(count)]

    for t, f in edges:
        graph[f].append(t)

    def dfs(v, p, s):
        if visited[v]:
            return p

        visited[v] = True
        s.add(v)

        for e in graph[v]:
            if e in s:
                return False

            p = dfs(e, p, s)

            if p is False:
                return False

        s.discard(v)
        order[p] = v
        return p - 1

    for v in range(count):
        pos = dfs(v, pos, set())

        if pos is False:
            return []

    return order


print(find_order(2, [[1, 0]]), [0, 1])
print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]),
      '[0,1,2,3] or [0,2,1,3]')
