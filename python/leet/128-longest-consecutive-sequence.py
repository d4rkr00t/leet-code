# Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# hard
#
# Time:  O(n)
# Space: O(n)


def longestConsecutive(nums: [int]) -> int: # 100, 4, 200, 1, 3, 2
    longest_streak = 0
    num_set = set(nums)

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)

    return longest_streak


print(longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
print(longestConsecutive([1, 2, 3, 4]), 4)
print(longestConsecutive([]), 0)
print(longestConsecutive([1]), 1)
print(longestConsecutive([4, 3, 2, 1]), 4)
print(longestConsecutive([0,0,-1]), 2)
print(longestConsecutive([-1,1,2,0]), 4)

#
# -1, 1, -2, 2, 0
#
# uf:   { -1: (-2, 2), 1: (0, 2), -2: (None, 5), 2: (0, 3), 0: (-2, 5) }
# max:  3
# item: 0
#
