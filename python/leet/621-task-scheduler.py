# Task Scheduler
# https://leetcode.com/problems/task-scheduler/
# medium
#
# Time:  O(n*logn)
# Space: TBD
#
# Solution:
# 1. Sort
# 2. Build up a stack until can't satisfy anymore
# 3. Reset stack and add number of steps


def leastInterval(tasks: [str], n: int) -> int:
    frequencies = {}  # used to count frequencies
    output = 0

    if n == 0:
        return len(tasks)

    # build word frequency dictionary
    for k in tasks:
        frequencies[k] = frequencies.get(k, 0)+1

    # get the count of the most frequent occurring term
    max_value = max(frequencies.values())

    # check if any other values occurred this same number of times
    max_value_occurrences = 0
    for value in frequencies.values():
        if value == max_value:
            max_value_occurrences += 1

    return max((max_value-1)*(n+1)+max_value_occurrences, len(tasks))


print(leastInterval(["A", "A", "A", "C", "C", "C"], 3))

#
# [0, -1, 3, -1, -1, -1, ...]
#
