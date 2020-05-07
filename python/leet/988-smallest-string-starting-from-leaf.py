# Smallest String Starting From Leaf
# https://leetcode.com/problems/smallest-string-starting-from-leaf/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# DFS

def smallestFromLeaf(root: TreeNode) -> str:
    if not root: return None

    def dfs(node, s):
        if not node: return None

        new_str = chr(node.val + 97) + s

        if not node.left and not node.right: return new_str

        left = dfs(node.left, new_str)
        right = dfs(node.right, new_str)

        if left and right: return min(left, right)
        return right if right else left

    return dfs(root, "")
