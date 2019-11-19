# Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution: Two pointers


def minSubArrayLen(s: int, nums: [int]) -> int:
    res = float("inf")
    start = sum = 0

    for i in range(0, len(nums)):
        sum += nums[i]

        while sum >= s:
            res = min(res, i + 1 - start)
            sum -= nums[start]
            start += 1

    return 0 if res == float("inf") else res


print(minSubArrayLen(s=7, nums=[2, 3, 1, 2, 4, 3]), 2)
print(minSubArrayLen(s=7, nums=[2, 3, 1, 2, 1, 3]), 4)
print(minSubArrayLen(s=11, nums=[1, 2, 3, 4, 5]), 3)
print(minSubArrayLen(s=6, nums=[10, 2, 3]), 1)
print(minSubArrayLen(s=6, nums=[]), 0)
print(minSubArrayLen(s=6, nums=[6]), 1)
