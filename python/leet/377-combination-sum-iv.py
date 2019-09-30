# Combination Sum IV
# https://leetcode.com/problems/combination-sum-iv/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# [dp]


def combinationSum4(nums: [int], target: int) -> int:
    dp = [0 for _ in range(0, target + 1)]
    for sub_target in range(1, target + 1):
        for num in nums:
            # then look for the num ways to make sum of (sub_target - num)
            if sub_target - num > 0:
                dp[sub_target] += dp[sub_target - num]
            elif sub_target - num == 0:
                dp[sub_target] += 1
    return dp[target]


print(combinationSum4([1, 2, 3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([0, 1, 2, 3], 3))

print(combinationSum4([3, 4, 5, 6, 7, 8, 9, 10, 11], 10))
