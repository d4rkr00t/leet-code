# Populating Next Right Pointers in Each Node II
# url: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# medium


def connect(root):
    level = [root]

    while (len(level)):
        new_level = []

        for (i, node) in enumerate(level):
            node.next = None if i + 1 >= len(level) else level[i + 1]

            if (node.left):
                new_level.append(node.left)
            if (node.right):
                new_level.append(node.right)

        level = new_level
