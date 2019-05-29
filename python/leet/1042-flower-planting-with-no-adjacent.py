# Flower Planting With No Adjacent
# #url: https://leetcode.com/problems/flower-planting-with-no-adjacent/
# #easy


def gardenNoAdj(N, paths):
    adj_m = [[] for x in range(N)]
    plants = [0] * N

    for p in paths:
        adj_m[p[0] - 1].append(p[1] - 1)
        adj_m[p[1] - 1].append(p[0] - 1)

    for i in range(N):
        plants[i] = ({1, 2, 3, 4} - {plants[j] for j in adj_m[i]}).pop()

    return plants


print(gardenNoAdj(3, [[1, 2], [2, 3], [3, 1]]), [1, 2, 3])
print(gardenNoAdj(4, [[1, 2], [3, 4]]), [1, 2, 1, 2])
print(gardenNoAdj(4, [[1, 2], [2, 3], [3, 4],
                      [4, 1], [1, 3], [2, 4]]), [1, 2, 3, 4])
