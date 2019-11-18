# Construct Binary Tree from Preorder and Postorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
#        1
#     /     \
#    2       3
#   / \     / \
#  4   5   6   7
#
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        res = str(self.val)

        if self.left:
            res += " " + str(self.left)

        if self.right:
            res += " " + str(self.right)

        return res


def constructFromPrePost(pre: [int], post: [int]) -> TreeNode:
    if not pre:
        return None
    root = TreeNode(pre[0])
    if len(pre) == 1:
        return root

    L = post.index(pre[1]) + 1
    root.left = constructFromPrePost(pre[1:L+1], post[:L])
    root.right = constructFromPrePost(pre[L+1:], post[L:-1])

    return root


print(constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]))
print(constructFromPrePost([1, 2, 4, 8, 9, 5, 10, 11,
                            3, 6, 12, 13, 7, 14, 15], [8, 9, 4, 10, 11, 5, 2, 12, 13, 6, 14, 15, 7, 3, 1]))

print(constructFromPrePost([1, 3, 2, 4], [3, 4, 2, 1]))
