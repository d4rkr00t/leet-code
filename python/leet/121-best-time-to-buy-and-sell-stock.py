# Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# easy
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# Two pointers

def maxProfit(prices: [int]) -> int:
    if not prices or len(prices) == 1:
        return 0

    low, m = prices[0], 0
    for i in range(1, len(prices)):
        high = prices[i]
        if low < high:
            m = max(high-low, m)
        else:
            low = high

    return max(m, 0)

print(maxProfit([7,1,5,3,6,4]), 5)
print(maxProfit([7,6,4,3,1]), 0)

#
#   |       |
# 7,1,5,3,6,4
