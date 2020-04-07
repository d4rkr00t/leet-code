# Maximum Sum of Two Non-Overlapping Subarrays
# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/
# medium
#
# Time:  TBD
# Space: TBD
#
# Solution:
# TBD

def maxSumTwoNoOverlap(A: [int], L: int, M: int) -> int:
    l_list = [0] * len(A)
    m_list = [0] * len(A)
    for i in range(1, len(A)+1):
        l_list[i-1] = sum(A[max(i - L, 0):i])
        m_list[i-1] = sum(A[max(i - M, 0):i])

    max_sum = 0

    for i in range(len(l_list)):
        l = l_list[i]

        for j in range(len(m_list)):
            m = m_list[j]
            if (j - M) + 1 > i or j < i - L:
                max_sum = max(max_sum, l + m)

    return max_sum

print(maxSumTwoNoOverlap(A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2), 20)
print(maxSumTwoNoOverlap(A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2), 29)
print(maxSumTwoNoOverlap(A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3), 31)
print(maxSumTwoNoOverlap(A = [1,0,3], L = 1, M = 2), 4)
print(maxSumTwoNoOverlap(A = [12,8,12,18,19,10,17,20,6,8,13,1,19,11,5], L = 3, M = 6), 131)

# 1 and 2
# [0,6,5,2,2,5,1,9,4]
# [0,6,11,7,4,7,6,10,13]
#
