# All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def allPossibleFBT(N: int) -> [TreeNode]:
    dp = {
        0: [],
        1: [TreeNode(0)]
    }

    def recur(N):
        nonlocal dp
        if N in dp: return dp[N]
        ans = []

        for x in range(N):
            y = N - 1 - x
            for left in recur(x):
                for right in recur(y):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right

                    ans.append(root)

        dp[N] = ans
        return ans

    recur(N)
    return dp[N]



# N = 3
#
#    0
#  /   \
# 0     0
#
# N = 5
#
#       0
#     /   \
#    0     0
#  /  \
# 0    0
#
#       0
#     /   \
#    0     0
#         /  \
#        0    0
#
#
# N = 7
#
#         0
#     /       \
#    0         0
#  /   \     /   \
# 0     0   0     0
#


