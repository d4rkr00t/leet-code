# Maximum Width of Binary Tree
# https://leetcode.com/problems/maximum-width-of-binary-tree/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# BFS

def widthOfBinaryTree(root: TreeNode) -> int:
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans


#           1
#         /   \
#        3     2
#       / \     \
#      5   3     9
#
#          1
#         /
#        3
#       / \
#      5   3
#
#          1
#         / \
#        3   2
#       /
#      5
#
#          1
#         / \
#        3   2
#       /     \
#      5       9
#     /         \
#    6           7
