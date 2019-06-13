# Course Schedule
# url: https://leetcode.com/problems/course-schedule/
# medium


def canFinish(numCourses, prerequisites):
    graph = [[] for x in range(numCourses)]

    for edge in prerequisites:
        graph[edge[0]].append(edge[1])

    visited = [0] * numCourses

    def is_cycle(graph, v, visited):
        edges = graph[v]
        visited[v] = -1

        for e in edges:  # [2]
            if (visited[e] == -1):
                return True
            if (visited[e]):
                if (is_cycle(graph, e, visited)):
                    return True

        visited[v] = 1
        return False

    for v in range(numCourses):
        if (visited[v] != 0):
            continue

        if (is_cycle(graph, v, visited)):
            return False

    return True


print(canFinish(2, [[1, 0]]))
print(canFinish(2, [[1, 0], [0, 1]]))
print(canFinish(3, [[0, 1], [0, 2], [1, 2]]))


# 0 -> 1 -> 2
# 0 -> 2
