# Verify Preorder Serialization of a Binary Tree
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/
# medium
#
# Time:  O(n)
# Space: O(n)
#
# Solution:
# Stack

def isValidSerialization(preorder: str) -> bool:
    sliced = preorder.split(",")
    stack = []

    for n in sliced:
        stack.append(n)

        while len(stack) >= 3 and stack[-1] == "#" and stack[-2] == "#":
            stack.pop()
            stack.pop()

            if stack[-1] == "#":
                return False

            stack[-1] = "#"

    return True if stack[-1] == "#" and len(stack) == 1 else False


print(isValidSerialization("9,3,4,#,#,1,#,#,2,#,6,#,#"), True)
print(isValidSerialization("1,#"), False)
print(isValidSerialization("9,#,#,1"), False)
print(isValidSerialization("1,#,#,#,#"), False)

