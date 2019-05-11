// First Missing Positive
// #url: https://leetcode.com/problems/first-missing-positive/
// #hard

/**
 * @param {number[]} nums
 * @return {number}
 */
let firstMissingPositive = function(nums) {
  let i = 0;
  while (i < nums.length) {
    if (
      nums[i] > 0 &&
      nums[i] <= nums.length &&
      nums[nums[i] - 1] !== nums[i]
    ) {
      [nums[nums[i] - 1], nums[i]] = [nums[i], nums[nums[i] - 1]];
    } else {
      i++;
    }
  }
  for (i = 0; i < nums.length; i++) {
    if (nums[i] !== i + 1) return i + 1;
  }
  return i + 1;
};

console.log(firstMissingPositive([1, 1000]), 2);
console.log(firstMissingPositive([1, 2, 0]), 3);
console.log(firstMissingPositive([1, 2, 3, 0]), 4);
console.log(firstMissingPositive([3, 4, -1, 1]), 2);
console.log(firstMissingPositive([7, 8, 9, 11, 12]), 1);
