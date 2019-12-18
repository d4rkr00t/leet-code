# Jump Game
# https://leetcode.com/problems/jump-game/
# medium
#
# Time:  O(n)
# Space: O(1)

def canJump(nums: [int]) -> bool:
    furtherst = 0

    if not nums or len(nums) == 1:
        return True

    for i, n in enumerate(nums):
        if n == 0 and i == furtherst:
            return False

        furtherst = max(min(i + n, len(nums) - 1), furtherst)

        if furtherst == len(nums) - 1:
            break

    return True


# in:  2 3 1 1 4
# i:     ^
# f:           ^

print(canJump([2,3,1,1,4]))

# in: 3, 2, 1, 0, 4
# i:           ^
# f:           ^
#
print(canJump([3,2,1,0,4]))
