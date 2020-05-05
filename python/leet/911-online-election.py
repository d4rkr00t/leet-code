# Online Election
# https://leetcode.com/problems/online-election/
# medium
#
# Time:  O(n) for construction + O(log n) for query, where n is a length of times
# Space: O(n)
#
# Solution:
# Binary Search + Pre calc sums

import bisect
from collections import defaultdict

class TopVotedCandidate:

    def __init__(self, persons: [int], times: [int]):
        self.times = times;
        self.votes = []

        cur_leader = 0
        cur_votes = defaultdict(int)

        for i in range(len(persons)):

            person = persons[i]
            time = times[i]
            cur_votes[person] += 1

            if cur_votes[cur_leader] <= cur_votes[person]:
                cur_leader = person
                self.votes.append(person)
            else:
                self.votes.append(cur_leader)

    def q(self, t: int) -> int:
        return self.votes[bisect.bisect(self.times, t) - 1]

obj = TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0,5,10,15,20,25,30])
print(3, obj.q(3), 0)
print(12, obj.q(12), 1)
print(25, obj.q(25), 1)
print(15, obj.q(15), 0)
print(24, obj.q(24), 0)
print(8, obj.q(8), 1)
print(32, obj.q(32), 0)
print(0, obj.q(0), 0)

