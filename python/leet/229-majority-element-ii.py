# Majority Element II
# https://leetcode.com/problems/majority-element-ii/
# medium
#
# Time:  O(n)
# Space: O(n)

def majorityElement(nums: [int]) -> [int]:
    hash_map = {}
    res = set()
    num = len(nums) // 3

    for x in nums:
        if x in hash_map:
            if hash_map[x] <= num:
                hash_map[x] += 1
        else:
            hash_map[x] = 1

        if hash_map[x] > num:
            res.add(x)

        if len(res) >= 3:
            break

    return list(res)

print(majorityElement([3,2,3]), [3])
print(majorityElement([1,1,1,3,3,2,2,2]), [1,2])
print(majorityElement([1]), [1])

# [1, 2, 3, 4, 1, 4, 4, 4, 4, 4, 4 3,]
