# Wiggle Subsequence
# https://leetcode.com/problems/wiggle-subsequence/
# medium
#
# Time:  O(n)
# Space: O(1)


def wiggleMaxLength(nums: [int]) -> int:
    if len(nums) < 2:
        return len(nums)

    # init table
    prevdiff = nums[1] - nums[0]
    count = 2 if prevdiff != 0 else 1

    for i in range(2, len(nums)):
        diff = nums[i] - nums[i-1]

        if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
            count += 1
            prevdiff = diff

    return count


print(wiggleMaxLength([1, 7, 4, 9, 2, 5]), 6)
print(wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]), 7)
print(wiggleMaxLength([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2)
