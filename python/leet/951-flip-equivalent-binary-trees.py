# Flip Equivalent Binary Trees
# https://leetcode.com/problems/flip-equivalent-binary-trees/
# medium
#
# Time: O(n) – as we need to compare all nodes
# Memory: O(n) – memory needed to keep stack
#
# 1. For current parent check if it's a flip or not
# 2. IF a flip:
#    2.1. recur(a.left, b.right) and recur(a.right, b.left)
# 3. IF not a flip:
#    3.1. recur(a.left, b.left) and recur(a.right, b.right)


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def flipEquiv(root1: TreeNode, root2: TreeNode) -> bool:
    def getValue(node: TreeNode):
        if not node:
            return None
        else:
            return node.val

    def recur(r1, r2):
        if not r1 and not r2:
            return True

        if getValue(r1) != getValue(r2):
            return False

        if getValue(r1.left) == getValue(r2.right) and getValue(r2.left) == getValue(r1.right):
            # flip
            return recur(r1.left, r2.right) and recur(r2.left, r1.right)
        else:
            # no flip
            return recur(r1.right, r2.right) and recur(r2.left, r1.left)

    return recur(root1, root2)

# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8],
#        root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
