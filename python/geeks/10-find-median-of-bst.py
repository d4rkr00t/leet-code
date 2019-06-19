# Find median of BST in O(n) time and O(1) space
# url: https://www.geeksforgeeks.org/find-median-bst-time-o1-space/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_median_bst(root):
    def inorder(root, stop=None):
        stack = []
        count = 0

        while (stack or root):
            while(root):
                stack.append(root)
                count += 1

                if (stop == count):
                    return (count, root)

                root = root.left

            root = stack.pop().right

        return (count, TreeNode(None))

    n = inorder(root)[0]
    median = (n // 2 + (n + 1) // 2) // 2 if n % 2 == 0 else (n + 1) / 2
    return inorder(root, median)[1].val


tree = TreeNode(20)
tree.left = TreeNode(8)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(12)
tree.left.right.left = TreeNode(10)
tree.left.right.right = TreeNode(14)
tree.right = TreeNode(22)

print(find_median_bst(tree), 12)
print(find_median_bst(None), None)
print(find_median_bst(TreeNode(1)), 1)
