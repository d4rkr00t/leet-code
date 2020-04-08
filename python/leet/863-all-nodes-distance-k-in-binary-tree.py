# All Nodes Distance K in Binary Tree
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# 1. Find target and it's distance from root
# 2. BFS tree and calculate distance
#   2.1. If target is a parent
#      Just the distance between them, early exit branch if no reason to look deeper
#   2.2. If root is a parent
#      Sum 2 distances, early exit branch if no reason to look deeper

def distanceK(root: TreeNode, target: TreeNode, K: int) -> [int]:
    def dfs(node, par = None):
        if not node:
            return

        node.par = par
        dfs(node.left, node)
        dfs(node.right, node)

    dfs(root, None)

    queue = [(target, 0)]
    seen = set()
    seen.add(target)
    ans = []

    while queue:
        cur = queue.pop(0)
        if cur[1] == K:
            ans.append(cur[0].val)

        for n in [cur[0].left, cur[0].right, cur[0].par]:
            if not n or n in seen:
                continue

            queue.append((n, cur[1] + 1))
            seen.add(n)

    return ans

print(distanceK(root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2), [7,4,1])


#
#       3
#  [5]      (1)
# 6   2    0  8
#   (7) (4)
#

#
# target idx = 1
# 2
# K = 1
   0
 1   null
3 [2]
