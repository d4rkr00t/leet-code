# Binary Tree Maximum Path Sum
# url: https://leetcode.com/problems/binary-tree-maximum-path-sum/
# hard

import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root


def maxPathSum(root):
    ans = -sys.maxsize

    def dfs(sub_root):
        nonlocal ans

        if (not sub_root):
            return 0

        left_sum = max(0, dfs(sub_root.left))
        right_sum = max(0, dfs(sub_root.right))

        ans = max(ans, left_sum+right_sum+sub_root.val)

        return max(left_sum, right_sum) + sub_root.val

    dfs(root)

    return ans


# [-10,9,20,null,null,15,7]
tree = TreeNode(-10)
tree.left = TreeNode(9)
tree.right = TreeNode(20)
tree.right.left = TreeNode(15)
tree.right.right = TreeNode(7)

print(maxPathSum(tree))
print(maxPathSum(TreeNode(-3)))
print(maxPathSum(stringToTreeNode(
    '[5,4,8,11,null,13,4,7,2,null,null,null,1]')))


#            5,
#           4,8,
# 11,null,13,4,
# 7,2,null,null,null,1
