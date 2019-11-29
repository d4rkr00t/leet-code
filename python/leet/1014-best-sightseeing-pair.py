# Best Sightseeing Pair
# https://leetcode.com/problems/best-sightseeing-pair/
# medium
#
# Time:  O(n)
# Space: TBD
#
# Solution:
#

def maxScoreSightseeingPair(A: [int]) -> int:
    # (A[i] + A[j] + i - j)
    max_pos = -1
    max_num = -1
    sum = -1

    for j in range(len(A)):
        num = A[j]

        cur_sum = max_num + num + max_pos - j

        if cur_sum > sum:
            sum = cur_sum

        if max_num + max_pos < num + j:
            max_pos = j
            max_num = num

    return sum

print(maxScoreSightseeingPair([8,1,5,2,6]), 11)

# 8 1 5 2 6
#         ^
# 8
# 0
# 11

# max_pos = 4
# max_num = 10
# sum     = 11
#
# j       = 4
# num     = 6
# cur_sum = 10
