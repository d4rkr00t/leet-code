# Linked List Random Node
# url: https://leetcode.com/problems/linked-list-random-node/
# medium

import random


def get_random(root):
    if not root:
        return None

    random_node = root
    root = root.next
    i = 1

    while root:
        if random.randint(1, i + 1) == 1:
            random_node = root

        root = root.next
        i += 1

    return random_node
