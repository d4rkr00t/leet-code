# Remove Duplicates from Sorted List II
# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
# medium
#
# Time:  O(n)
# Space: O(1)

def deleteDuplicates(head: ListNode) -> ListNode:
    dummy = pre = ListNode(0)
    dummy.next = head
    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            head = head.next
            pre.next = head
        else:
            pre = pre.next
            head = head.next
    return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Input: 1
# Output: 1
#
# Input: 1->2
# Output: 1->2
#
#
# Input: 1->2->3->3->4->4->5
# Output: 1->2->5
#
# stack = [(1, False)]
# head = 1->2->5
# Input: 1->1->1->2->3
# Output: 2->3
#
# Input: 1->1->1->2->3->3
# Output: 2
