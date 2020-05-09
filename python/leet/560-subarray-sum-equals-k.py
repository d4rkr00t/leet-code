# Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Hash map

def subarraySum(nums: [int], k: int) -> int:
    if not nums: return ans

    ans = sum = 0
    map = { 0: 1 }

    for n in nums:
        sum += n
        if sum - k in map:
            ans += map[sum - k]

        map[sum] = map[sum] + 1 if sum in map else 1

    return ans

print(subarraySum([1,1,1], 2), 2)
print(subarraySum([2,2,2], 1), 0)
print(subarraySum([1,2,3,4], 11), 0)
print(subarraySum([-1,-1,1], 0), 1)
print(subarraySum([28,54,7,-70,22,65,-6], 100), 1)


# [28,54,7,-70,22,65,-6]
#                     ^
# ans = 1
# sum = 28 + 54 + 7 - 70 + 22 + 65 - 6 = 100 - 100
# k   = 100
# map = { 0: 2, 28: 1, 82: 1, 89: 1, 19: 1, 41: 1, 106: 1 }
