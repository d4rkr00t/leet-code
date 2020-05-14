# Reveal Cards In Increasing Order
# https://leetcode.com/problems/reveal-cards-in-increasing-order/
# medium

import collections

def deckRevealedIncreasing(deck: [int]) -> [int]:
    N = len(deck)
    index = collections.deque(range(N))
    ans = [None] * N

    for card in sorted(deck):
        ans[index.popleft()] = card
        print()
        if index:
            index.append(index.popleft())

    return ans

print(deckRevealedIncreasing([17,13,11,2,3,5,7]), [2,13,3,11,5,17,7])

# [17,13,11,2,3,5,7]
#
# 0 1 2 3 4 5 6
# 2 3 4 5 6 1
# 4 5 6 1 3
# 6 1 3 5
# 3 5 1
# 1 5
# 5
