# 3Sum
# #url: https://leetcode.com/problems/3sum/
# #medium


def threeSum(nums):
    if len(nums) < 3:
        return []

    ans = {}

    for i in range(len(nums) - 1):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        table = set()  # { 0, 1, 2 }
        for j in range(i + 1, len(nums)):
            t = 0 - (nums[i] + nums[j])  # nums[i] = -1, nums[j] = 1
            if t in table:
                l = sorted([nums[i], nums[j], t])
                if str(l) not in ans:
                    ans[str(l)] = l

            table.add(nums[j])

    return list(ans.values())


print(threeSum([-1, 0, 1, 2, -1, -4]))
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
