# Min Cost Climbing Stairs
# https://leetcode.com/problems/min-cost-climbing-stairs/
# easy
#
# Time:  O(n) where n is length of cost
# Space: O(1) where n is length of cost
#
# Solution:
# DP

def minCostClimbingStairs(cost: [int]) -> int:
    m1 = m2 = 0

    for x in cost:
        m1, m2 = x + min(m1, m2), m1

    return min(m1, m2)

# [10, 15, 20]
# [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
