# Add Two Numbers
# #url: https://leetcode.com/problems/add-two-numbers/
# #medium


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(l1, l2):  # 2,4,3 + 1
    carry = 0  # 0
    root = next_node = ListNode(None)  # -> 3 -> 4 -> 3

    while l1 or l2 or carry:  # 3 and None
        l1_val = l1.val if l1 else 0  # 3
        l2_val = l2.val if l2 else 0  # 0

        carry, val = divmod(l1_val + l2_val + carry, 10)

        next_node.next = ListNode(val)
        next_node = next_node.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return root.next


def create_list(list):
    root = ListNode(list.pop(0))
    next_node = root

    for i in list:
        new_root = ListNode(i)
        next_node.next = new_root
        next_node = new_root

    return root


print(addTwoNumbers(create_list([2, 4, 3]),
                    create_list([5, 6, 4])))  # 7 -> 0 -> 8
print(addTwoNumbers(create_list([2, 4, 3]), create_list([1])))
