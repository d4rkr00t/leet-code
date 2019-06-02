# Minimum number of swaps required for arranging pairs adjacent to each other
# url: https://www.geeksforgeeks.org/minimum-number-of-swaps-required-for-arranging-pairs-adjacent-to-each-other/


def number_of_swaps(arr, pairs):
    cur = 0
    swaps = 0
    indexes = {}

    for (idx, i) in enumerate(arr):
        indexes[i] = idx

    if (not len(pairs)):
        return swaps

    while (cur < len(arr) - 1):
        e1 = arr[cur]
        e2 = arr[cur + 1]

        if (pairs[e1] != e2):
            pair_idx = indexes[pairs[e1]]

            arr[cur + 1], arr[pair_idx] = arr[pair_idx], arr[cur + 1]

            swaps += 1

        cur += 2

    return swaps


# {1->3, 2->6, 4->5}
print(number_of_swaps([3, 5, 6, 4, 1, 2], [0, 3, 6, 1, 5, 4, 2]))

# {3->7, 5->8, 2->4, 6->1} -> [3,7,6,1,4,2,5,8]
print(number_of_swaps([3, 5, 6, 4, 1, 2, 7, 8], [0, 6, 4, 7, 2, 8, 1, 3, 5]))
