# Find the Town Judge
# #url: https://leetcode.com/problems/3sum/
# #medium


def findJudge(N, trust):
    people = [(0, 0)] * N

    for t in trust:
        t_from = t[0] - 1
        t_to = t[1] - 1

        people[t_from] = (people[t_from][0] + 1, people[t_from][1])
        people[t_to] = (people[t_to][0], people[t_to][1] + 1)

    try:
        return people.index((0, N-1)) + 1
    except:
        return -1


print(findJudge(2, [[1, 2]]), 2)
print(findJudge(3, [[1, 3], [2, 3]]), 3)
print(findJudge(3, [[1, 3], [2, 3], [3, 1]]), -1)
