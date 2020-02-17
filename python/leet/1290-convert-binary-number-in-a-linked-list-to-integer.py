# Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# easy
#
# Time:  O(n)
# Space: O(1)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getDecimalValue(head: ListNode) -> int:
    result = 0

    while head:
        result = result << 1 | head.val
        head = head.next

    return result

print(getDecimalValue([1,0,1]), 5)
print(getDecimalValue([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]), 18880)
print(getDecimalValue([0,0]), 0)
print(getDecimalValue([]), 0)
print(getDecimalValue([1]), 1)
print(getDecimalValue([0]), 0)

# 101
# 0 * 2 + 1 = 1
# 1 * 2 + 0 = 2
# 2 * 2 + 1 = 5
#
# or
#
# 101
# 0 << 1  | 1 = 1   = 1
# 1 << 1  | 0 = 10  = 2
# 10 << 1 | 1 = 101 = 5
