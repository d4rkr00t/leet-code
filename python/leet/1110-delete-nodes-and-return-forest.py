# Delete Nodes And Return Forest
# https://leetcode.com/problems/delete-nodes-and-return-forest/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# DFS

def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
    def dfs(parent, node, to_delete, res):
        if not node:
            return res

        if node.val in to_delete:
            if parent:
                if parent.left == node:
                    parent.left = None
                else:
                    parent.right = None

            dfs(None, node.left, to_delete, res)
            dfs(None, node.left, to_delete, res)

            return res

        if not parent:
            group.append(node)

        dfs(node, node.left, to_delete, res)
        dfs(node, node.right, to_delete, res)

        return res

    return dfs(None, root, to_delete, res)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
