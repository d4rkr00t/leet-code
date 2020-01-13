# Best Time to Buy and Sell Stock with Transaction Fee
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
# medium
#
# Time:  O(n)
# Space: O(1)
#
# Solution:
# DP

def maxProfit(prices: [int], fee: int) -> int:
    if not prices:
        return

    hold = -prices[0]
    cash = 0

    for i in range(1, len(prices)):
        cur = prices[i]
        hold = max(hold, cash - cur)
        cash = max(cash, cur + hold - fee)

    return cash



print(maxProfit(prices = [1, 3, 2, 8, 4, 9], fee = 2), 8)

#
#       1  3  2  8  4  9
#    Y -1 -1 -1 -1  1  1
#    N  0  0  0  5  5  8
