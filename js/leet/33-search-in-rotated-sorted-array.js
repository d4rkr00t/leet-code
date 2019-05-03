// Search in Rotated Sorted Array
// #url: https://leetcode.com/problems/search-in-rotated-sorted-array/
// #medium
//
// Example 1:
// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
//
// Solution:
//   1. Find pivot point
//   2. Search
//              4
//     [4,5,6,7,0,1,2] // offset 3, middle idx = 3 (4)

function findPivot(nums) {
  let cur = 0;
  let prev = nums.length - 1;
  while (nums[cur] > nums[prev]) {
    cur = prev;
    prev--;
  }

  return cur;
}

function bsearch(nums, target, start, end) {
  let middle = Math.floor((start + end) / 2);
  let cur = nums[middle];
  if (cur === target) {
    return middle;
  }
  if (end - start === 0 || start > end) {
    return -1;
  }
  if (cur > target) {
    return bsearch(nums, target, start, middle - 1);
  }
  if (cur < target) {
    return bsearch(nums, target, middle + 1, end);
  }
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
let search = function(nums, target) {
  let pivot = findPivot(nums);
  if (pivot === 0) {
    return bsearch(nums, target, 0, nums.length);
  }
  if (target >= nums[0]) {
    return bsearch(nums, target, 0, pivot - 1);
  }
  return bsearch(nums, target, pivot, nums.length);
};

console.log(search([4, 5, 6, 7, 0, 1, 2], 0), 4);
console.log(search([4, 5, 6, 7, 0, 1, 2], 3), -1);
console.log(search([4, 5, 6, 7, 0, 1, 2], 5), 5);
console.log(search([1, 3], 3), 1);
console.log(search([3, 1], 0), -1);
console.log(search([3, 5, 1], 5), 1);
