# Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/
# easy
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# DFS

def findMode(root: TreeNode) -> List[int]:
    m = []
    def dfs(node, counts):
        nonlocal m

        if not node: return

        cur_m = counts[m[-1]] if m else 0
        counts[node.val] = counts.get(node.val, 0) + 1

        if cur_m == counts[node.val]: m.append(node.val)
        elif cur_m < counts[node.val]: m = []

        l = dfs(node.left, counts)
        r = dfs(node.right, counts)

    dfs(root, {})

    return m

