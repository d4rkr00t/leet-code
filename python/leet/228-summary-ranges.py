# Summary Ranges
# https://leetcode.com/problems/summary-ranges/
# medium


def summaryRanges(nums: [int]) -> [str]:
    prev = None  # 8
    output = []  # ["0", "2->4", "6", "8->9"]

    if not nums:
        return output

    for n in nums:  # 9
        if prev == None:
            output.append(str(n))
        elif prev != n - 1:
            if output[-1] != str(prev):
                output[-1] = output[-1] + "->" + str(prev)

            output.append(str(n))

        prev = n

    if output[-1] != str(prev):
        output[-1] = output[-1] + "->" + str(prev)

    return output


print(summaryRanges([0, 1, 2, 4, 5, 7]))
print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
