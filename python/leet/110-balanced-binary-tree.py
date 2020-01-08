# Balanced Binary Tree
# https://leetcode.com/problems/balanced-binary-tree/
# easy
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# DFS

def isBalanced(root) -> bool:
    def dfs(node, depth):
        if not node:
            return depth

        rd = dfs(node.right, depth + 1)
        ld = dfs(node.left, depth + 1)

        if rd == False or ld == False or abs(rd - ld) > 1:
            return False

        return max(rd, ld)

    result = dfs(root, 1)

    return False if not result else True
