# 3Sum Closest
# url: https://leetcode.com/problems/3sum-closest/
# medium


def threeSumClosest(nums, target):
    closest_sum = nums[0] + nums[1] + nums[2]
    nums.sort()  # -4, -1, 1, 2

    for i in range(len(nums) - 2):
        j, k = i+1, len(nums) - 1

        while j < k:
            s = nums[i] + nums[j] + nums[k]

            if s == target:
                return s

            if (abs(target - closest_sum) > abs(target - s)):
                closest_sum = s

            if s < target:
                j += 1
            elif s > target:
                k -= 1

    return closest_sum


print(threeSumClosest([-1, 2, 1, -4], 1))
print(threeSumClosest([1, 2, 4, 8, 16, 32, 64, 128], 82))
