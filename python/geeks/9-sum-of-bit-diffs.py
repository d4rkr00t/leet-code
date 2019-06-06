def bit_diff_sum(arr):
    sum = 0

    for i in range(0, 32):
        count = 0
        for j in arr:
            if (j & (1 << i)):
                count += 1

        sum += (count * (len(arr) - count) * 2)

    return sum


print(bit_diff_sum([1, 3, 5]), 8)
