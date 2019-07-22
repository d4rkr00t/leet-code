# Boats to Save People
# https://leetcode.com/problems/boats-to-save-people/
# medium


def numRescueBoats(people, limit):
    people.sort()
    s = 0
    e = len(people) - 1
    boats = 0

    while s <= e:
        boats += 1

        if people[s] + people[e] <= limit:
            s += 1

        e -= 1

    return boats
