# Two Sum
# #url: https://leetcode.com/problems/two-sum/
# #easy


def twoSum(nums, target):
    rec = {}  # { 2: 0 }

    for x, num in enumerate(nums):  # x=1
        diff = target - num  # 9 - 7 = 2
        if diff in rec:  # True
            return [rec[diff], x]
        else:
            rec[num] = x

    return []


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([-3, 4, 3, 90], 0))
