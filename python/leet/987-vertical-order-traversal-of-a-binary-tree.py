# Vertical Order Traversal of a Binary Tree
# url: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/
# medium


def verticalTraversal(root):  # [1,2,3,4,5,6,7]
    if (not root):
        return []

    tmp = {}

    def dfs(node, x=0, y=0):
        if (node):
            if (not x in tmp):
                tmp[x] = {}

            if (not y in tmp[x]):
                tmp[x][y] = []

            tmp[x][y].append(node.val)

            dfs(node.left, x-1, y+1)
            dfs(node.right, x+1, y+1)

    dfs(root)

    res = []

    for x in sorted(tmp):
        rep = []
        for y in sorted(tmp[y]):
            rep.extend(sorted(tmp[x][y]))

        res.append(rep)

    return res
