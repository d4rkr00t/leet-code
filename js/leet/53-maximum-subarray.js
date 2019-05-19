// Counting Bits
// #url: https://leetcode.com/problems/maximum-subarray/
// #easy

/**
 * @param {number[]} nums
 * @return {number}
 */
let maxSubArray = function(nums) {
  let res = 0;
  let max = nums[0]; // -1

  for (let i = 0; i < nums.length; i++) {
    let n = nums[i]; // -1
    max = Math.max(n, max);
    if (res + n > 0) {
      res += n;
      max = Math.max(res, max);
    } else {
      res = 0;
    }
  }

  return max;
};

console.log(maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6);
console.log(maxSubArray([-2, -1]), -1);
console.log(maxSubArray([-1, 1, 2, 1]), 4);
