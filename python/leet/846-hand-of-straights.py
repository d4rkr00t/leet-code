# Hand of Straights
# https://leetcode.com/problems/hand-of-straights/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

import collections


def isNStraightHand(hand, W):
    if len(hand) % W != 0:
        return False

    count = collections.Counter(hand)

    while count:
        m = min(count.keys())
        num = count[m]
        for k in range(m, m+W):
            v = count[k]
            if v < num:
                return False
            if v == num:
                del count[k]
            else:
                count[k] = v - num

    return True


print(isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))

# [1, 2, 3, 6, 2, 3, 4, 7, 8]
#
# [1, 2, 2, 3, 3, 4, 6, 7, 8]
#
# [1, 2, 3]
# [2, 3, 4]
# [6, 7, 8]
