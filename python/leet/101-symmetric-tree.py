# Symmetric Tree
# https://leetcode.com/problems/symmetric-tree/
# easy
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def isSymmetric(root: TreeNode) -> bool:
    def isMirror(t1, t2):
        if t1 == None and t2 == None: return True
        if t1 == None or t2 == None: return False
        return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t2.left, t1.right)

    return isMirror(root, root)


#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
