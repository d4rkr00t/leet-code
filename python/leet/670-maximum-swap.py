# Maximum Swap
# https://leetcode.com/problems/maximum-swap/
# medium
#
# Time:  O(num)
# Space: O(1)
#
# Solution:
# Two-pointers

def maximumSwap(num: int) -> int:
    if num < 10: return num

    num_arr = list(str(num))

    h = len(num_arr) - 1
    l = h - 1
    swap = (h,h) # low, high

    while l >= 0 and h >= 0:
        if num_arr[h] > num_arr[l]:
            swap = (l, h)
            l -= 1
        elif num_arr[h] == num_arr[l]:
            l -= 1
        else:
            h = l
            l -= 1

    num_arr[swap[0]], num_arr[swap[1]] = num_arr[swap[1]], num_arr[swap[0]]

    return int(''.join(num_arr))

# (3,3)
# 1993
#   h
#  l
#
# 98368
#
