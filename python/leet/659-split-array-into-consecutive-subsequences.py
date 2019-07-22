# Split Array into Consecutive Subsequences
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
# medium
import collections


def isPossible(nums):  # [1, 2, 3, 4, 4, 5]
    count = collections.Counter(nums)  # {1:0, 2:-1, 3:-1, 4:1, 5:1}
    tails = collections.Counter()  # { 4: 0, 5: 1 }
    for x in nums:  # 4
        if count[x] == 0:
            continue
        elif tails[x] > 0:
            tails[x] -= 1
            tails[x+1] += 1
        elif count[x+1] > 0 and count[x+2] > 0:
            count[x+1] -= 1
            count[x+2] -= 1
            tails[x+3] += 1
        else:
            return False
        count[x] -= 1
    return True


print(isPossible([1, 2, 3, 3, 4, 5]), True)
print(isPossible([1, 2, 3, 3, 4, 4, 5, 5]), True)
print(isPossible([1, 2, 3, 4, 4, 5]), False)
