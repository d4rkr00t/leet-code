# Custom Sort String
# url: https://leetcode.com/problems/custom-sort-string/
# medium
import sys


def customSortString(S, T):
    weight = [sys.maxsize] * 26

    for i in range(len(S)):
        weight[ord(S[i]) - 97] = i

    return "".join(sorted(list(T), key=lambda x: weight[ord(x) - 97]))


print(customSortString("cba", "abcd"), "cbad")
