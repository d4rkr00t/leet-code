# Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# BFS Leveled

def largestValues(self, root: TreeNode) -> List[int]:
    if not root:
        return []

    level = [root]
    ans = []

    while level:
        m = float("-inf")
        next_level = []
        for cur in level:
            m = max(m, cur.val)

            if cur.left:
                next_level.append(cur.left)

            if cur.right:
                next_level.append(cur.right)

        ans.append(m)
        level = next_level

    return ans

