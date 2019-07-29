# Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# medium


def remove_duplciates(nums):
    i = 0
    for n in nums:
        if i < 2 or n > nums[i-2]:
            nums[i] = n
            i += 1
    return i


print(remove_duplciates([0, 0, 1, 1, 1, 1, 2, 2, 2, 3, 3]), 8)
print(remove_duplciates([1, 1, 1, 2, 2, 3]), 5)
print(remove_duplciates([1, 2, 3, 4, 5]), 5)
print(remove_duplciates([1]), 1)

# count = 2
# cur = 2
#                          s
#                                  e
# [0, 0, 1, 1, 2, 2, 3, 3, N, N, N]
