# Reverse Pairs
# https://leetcode.com/problems/reverse-pairs/
# hard


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.count = 1
        self.count_smaller = 0


def find_smaller(root, target):  # 4, 3
    res = 0
    if not root:
        return res

    if root.val < target:
        res += root.count_smaller + root.count  # 1
        res += find_smaller(root.right, target)
    elif root.val == target:
        res += root.count_smaller
    else:
        res += find_smaller(root.left, target)

    return res  # 0


def insert(root, target):  # 6, 6
    # bigger
    if root.val < target:
        if root.right:
            insert(root.right, target)
        else:
            root.right = Node(target)
    # equal
    elif root.val == target:
        root.count += 1
    # smaller
    else:
        root.count_smaller += 1
        if root.left:
            insert(root.left, target)
        else:
            root.left = Node(target)

#
#   (2, 1, 0)
#        \
#        (6, 2, 1)
#       /
#   (4, 1, 0)


def reverse_pairs(nums):  # [1, 3, 2, 3, 1]
    res = 0

    if not nums or len(nums) == 1:
        return res

    root = Node(nums[-1] * 2)

    for i in range(len(nums) - 2, -1, -1):  # 0
        res += find_smaller(root, nums[i])  # 2, 1 = 1
        insert(root, nums[i] * 2)  # 2, 2

    return res  # 2


print(reverse_pairs([1, 3, 2, 3, 1]), 2)
print(reverse_pairs([2, 4, 3, 5, 1]), 3)
