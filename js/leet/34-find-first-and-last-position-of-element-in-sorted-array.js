// Find First and Last Position of Element in Sorted Array
// #url: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// #medium

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
let searchRange = function(nums, target) {
  let findIdx = (s, e) => {
    if (s >= e) {
      return -1;
    }
    let middle = Math.floor((e + s) / 2);

    if (nums[middle] === target) {
      return middle;
    } else if (nums[middle] > target) {
      return findIdx(s, middle);
    } else {
      return findIdx(middle + 1, e);
    }
  };
  let s, e;
  s = e = findIdx(0, nums.length);

  if (s === -1 && e === -1) {
    return [s, e];
  }

  while (nums[s - 1] === target || nums[e + 1] === target) {
    if (nums[s - 1] === target) {
      s--;
    }
    if (nums[e + 1] === target) {
      e++;
    }
  }

  return [s, e];
};

console.log(searchRange([1, 3], 1), `[0, 0]`);
console.log(searchRange([5, 7, 7, 8, 8, 10], 8), `[3, 4]`);
console.log(searchRange([5, 7, 7, 8, 8, 10], 6), `[-1, -1]`);
