# Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# medium


class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

    def __str__(self):
        return "(" + str(self.val) + "," + str(self.next) + "," + (str(self.random.val if self.random else "None")) + ")"


def copyRandomList(head):
    newRefs = {}
    newHead = None  # (1, $2, $2) -> (2, None, $2)
    newHeadNext = None  # (2, None, None)

    while head:  # None
        if not head in newRefs:
            node = Node(head.val, None, None)  # (2, None, $2)
        else:
            node = newRefs[head]

        newRefs[head] = node

        if not newHead:
            newHead = node
            newHeadNext = node
        else:
            newHeadNext.next = node
            newHeadNext = node

        if head.random:
            if head.random in newRefs:
                node.random = newRefs[head.random]
            else:
                random = Node(head.random.val, None, None)
                node.random = random
                newRefs[head.random] = random

        head = head.next

    return newHead


node5 = Node(4, None, None)
node4 = Node(-3, None, None)
node3 = Node(7, None, None)
node2 = Node(8, None, None)
node1 = Node(-1, None, None)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node1.random = node5
node2.random = node4
node3.random = None
node4.random = None
node5.random = node1

print(copyRandomList(node1))
