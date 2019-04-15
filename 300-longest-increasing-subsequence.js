// Longest Increasing Subsequence
// #url: https://leetcode.com/problems/longest-increasing-subsequence/
// #medium
//
// Input: [10,9,2,5,3,7,101,18]
// Output: 4
// Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
// Collection of integers: 2 6 3 4 1 2 9 5 8

// Steps:

// 0. S = {} - Initialize S to the empty set
// 1. S = {2} - New largest LIS
// 2. S = {2, 6} - New largest LIS
// 3. S = {2, 3} - Changed 6 to 3
// 4. S = {2, 3, 4} - New largest LIS
// 5. S = {1, 3, 4} - Changed 2 to 1
// 6. S = {1, 2, 4} - Changed 3 to 2
// 7. S = {1, 2, 4, 9} - New largest LIS
// 8. S = {1, 2, 4, 5} - Changed 9 to 5
// 9. S = {1, 2, 4, 5, 8} - New largest LIS

function bs(nums, num) {
  if (nums.length <= 2) {
    return nums[0] >= num ? 0 : 1;
  }

  let bottom = 0;
  let top = nums.length - 1;
  while (true) {
    let pos = Math.floor((top + bottom) / 2);
    let el = nums[pos];

    if (top - bottom <= 1) {
      return Math.ceil((top + bottom) / 2);
    }

    if (bottom > top) {
      return -1;
    }

    if (el < num) {
      bottom = pos + 1;
    } else if (el > num) {
      top = pos - 1;
    } else {
      return pos;
    }
  }
}

function lengthOfLIS(nums) {
  let result = [nums[0]];

  for (let i = 1; i < nums.length; i++) {
    let el = nums[i];
    if (el > result[result.length - 1]) {
      result.push(el);
    } else {
      let pos = bs(result, el);
      result[pos] = el;
    }
  }

  return result.length;
}

console.log(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4);
console.log(lengthOfLIS([4, 10, 4, 3, 8, 9]), 3);
console.log(lengthOfLIS([26, 90, 67, 100, 83, 33]), 3);
console.log(lengthOfLIS([2, 14, 97, 54, 100, 6]), 4);
console.log(lengthOfLIS([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]), 6);
