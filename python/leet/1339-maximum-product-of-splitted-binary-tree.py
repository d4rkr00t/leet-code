# Maximum Product of Splitted Binary Tree
# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
# medium
#
# Time:  O(n) where n is a number of nodes
# Space: O(n) where n is a number of nodes
#
# Solution:
# 1. Pre-calculate sum of all subtrees O(n) and total
# 2. Find max((total - curItem) * curItem)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxProduct(root: TreeNode) -> int:
    s = []
    def sums(node, s):
        if not node: return 0
        s.append(node.val + sums(node.left, s) + sums(node.right, s))
        return s[-1]

    total = sums(root, s)
    return max((x * (total - x) for x in s)) % (10 ** 9 + 7)

maxProduct(TreeNode(0, None, None))
