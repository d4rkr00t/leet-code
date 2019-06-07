# Same Tree
# url: https://leetcode.com/problems/same-tree/
# easy


def isSameTree(p, q):
    p_stack = [p]  # 2 1
    q_stack = [q]  # 1 2

    while (len(p_stack) or len(q_stack)):
        if (len(p_stack) != len(q_stack)):
            return False

        pcur = p_stack.pop(0)  # 1
        qcur = q_stack.pop(0)  # 1

        if (not pcur and not qcur):
            continue
        if (pcur and qcur and pcur.val == qcur.val):
            p_stack.extend([pcur.left, pcur.right])
            q_stack.extend([qcur.left, qcur.right])
        else:
            return False

    return True

# Input:     1         1
#           / \       / \
#          2   3     2   3

# Input:     1         1
#           /           \
#          2             2

# Input:     1         1
#           / \       / \
#          2   1     1   2
