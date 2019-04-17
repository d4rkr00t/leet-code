// Best Time to Buy and Sell Stock II
// #url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// #easy
//
// Input: [7,1,5,3,6,4]
// Output: 7
// Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
//              Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

/**
 * @param {number[]} prices
 * @return {number}
 */
let maxProfit = function(prices) {
  let profit = 0;
  for (let i = 1; i < prices.length; i++) {
    if (prices[i] > prices[i - 1]) {
      profit += prices[i] - prices[i - 1];
    }
  }
  return profit;
};

console.log(maxProfit([7, 1, 5, 3, 6, 4]), 7);
console.log(maxProfit([7, 1, 5, 3, 6, 4]), 7);
console.log(maxProfit([1, 2, 3, 4, 5]), 4);
console.log(maxProfit([7, 6, 4, 3, 1]), 0);
console.log(maxProfit([2, 1, 2, 0, 1]), 2);
