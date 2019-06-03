# Number of recycled pairs in an array
# url: https://www.geeksforgeeks.org/number-recycled-pairs-array/

import math


def number_of_pairs(arr):
    res = 0  # 2

    arr.sort()  # 5 5 9 13 23 31 32 42
    uniq = []  # 5 9 13 23 31 32 42

    for (idx, i) in enumerate(arr):
        if (idx + 1 == len(arr) or i != arr[idx + 1]):
            uniq.append(i)

    def b_search(arr, target, start, end):
        if (start >= end):
            return -1

        middle = (end + start) // 2  # 5 == 32

        if (arr[middle] == target):
            return middle
        elif (arr[middle] > target):
            return b_search(arr, target, start, middle)
        else:
            return b_search(arr, target, middle + 1, end)

    for (idx, i) in enumerate(uniq):
        digits = math.floor(math.log10(i) + 1)  # 2
        pow_ten = int(math.pow(10, digits - 1))  # 10

        new_i = i
        for j in range(1, digits):
            (q, r) = divmod(new_i, 10)

            # rotate number
            new_i = r * pow_ten + q  # 13

            if (b_search(uniq, new_i, idx + 1, len(uniq)) != -1):
                res += 1

    return res  # 2


print(number_of_pairs([32, 42, 13, 23, 9, 5, 5, 31]))
print(number_of_pairs([1212, 2121]))
