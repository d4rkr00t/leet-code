# Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# easy
#
# Time:  O(n) – where n – is a length of a longest list
# Space: O(1)


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    head = ListNode(None)
    next = head

    while l1 or l2:
        if (l1 and not l2) or (l1 and l1.val <= l2.val):
            next.next = l1
            l1 = l1.next
        elif (l2 and not l1) or (l2 and l2.val <= l1.val):
            next.next = l2
            l2 = l2.next

        next = next.next

    return head.next


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
