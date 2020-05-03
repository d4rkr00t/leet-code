# Minimum Moves to Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
# medium
#
# Time:  O(n)
# Space: O(n)

def minMoves2(nums: [int]) -> int:
    nums.sort()
    init_guess = nums[len(nums)//2]
    diff = [x - init_guess for x in nums]
    new_moves = sum([abs(d) for d in diff])
    return new_moves


print(minMoves2([1,2,3]), 2)
print(minMoves2([4,2,4,1]), 5)
print(minMoves2([1, 1, 4, 4, 4, 4, 4, 10]), 12)
