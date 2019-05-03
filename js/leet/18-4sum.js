// 4Sum
// #url: https://leetcode.com/problems/4sum/
// #medium

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[][]}
 */
var fourSum = function(nums, target = 0) {
  if (nums.length < 4) return [];
  nums = nums.sort((a, b) => a - b);

  let pairs = {};

  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      pairs[nums[i] + nums[j]] = (pairs[nums[i] + nums[j]] || []).concat({
        i,
        j
      });
    }
  }

  let result = {};

  for (let i = 0; i < nums.length - 1; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      let sum = nums[i] + nums[j];
      let p = pairs[target - sum];
      if (p) {
        p.forEach(pair => {
          if (pair.i !== i && pair.i !== j && pair.j !== i && pair.j !== j) {
            let item = [nums[i], nums[pair.i], nums[pair.j], nums[j]].sort(
              (a, b) => a - b
            );
            result[item.join("")] = item;
          }
        });
      }
    }
  }

  return Object.keys(result).map(key => result[key]);
};

// console.log(fourSum([1, 0, -1, 0, -2, 2], 0));
// console.log([[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]);
console.log(fourSum([-4, -3, -2, -1, 0, 0, 1, 2, 3, 4], 0));
console.log([
  [-4, -3, 3, 4],
  [-4, -2, 2, 4],
  [-4, -1, 1, 4],
  [-4, -1, 2, 3],
  [-4, 0, 0, 4],
  [-4, 0, 1, 3],
  [-3, -2, 1, 4],
  [-3, -2, 2, 3],
  [-3, -1, 0, 4],
  [-3, -1, 1, 3],
  [-3, 0, 0, 3],
  [-3, 0, 1, 2],
  [-2, -1, 0, 3],
  [-2, -1, 1, 2],
  [-2, 0, 0, 2],
  [-1, 0, 0, 1]
]);
