# Trim a Binary Search Tree
# https://leetcode.com/problems/trim-a-binary-search-tree/
# easy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def trimBST(root, L, R):
    def trim(node):
        if not node:
            return None
        elif node.val > R:
            return trim(node.left)
        elif node.val < L:
            return trim(node.right)
        else:
            node.left = trim(node.left)
            node.right = trim(node.right)
            return node

    return trim(root)
