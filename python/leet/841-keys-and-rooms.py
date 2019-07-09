# Keys and Rooms
# https://leetcode.com/problems/keys-and-rooms/
# medium


def canVisitAllRooms(rooms):
    visited = [False] * len(rooms)

    def dfs(root):
        visited[root] = True
        for edge in rooms[root]:
            if visited[edge] == False:
                dfs(edge)

    dfs(0)

    return all(visited)


print(canVisitAllRooms([[1], [2], [3], []]), True)
print(canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]), False)
