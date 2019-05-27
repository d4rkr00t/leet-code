# Find the two non-repeating elements in an array of repeating elements
# url: https://www.geeksforgeeks.org/find-two-non-repeating-elements-in-an-array-of-repeating-elements/


def get_2_non_rep_nums(arr):
    xor = arr[0]
    set_bit = 0

    for i in range(1, len(arr)):
        xor = xor ^ arr[i]

    set_bit = xor & ~(xor-1)

    x = y = 0

    for i in arr:
        if i & set_bit:
            x ^= i
        else:
            y ^= i

    return sorted([x, y])


print(get_2_non_rep_nums([2, 3, 7, 9, 11, 2, 3, 11]))
