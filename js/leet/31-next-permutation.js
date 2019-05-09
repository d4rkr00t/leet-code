// Next Permutation
// #url: https://leetcode.com/problems/next-permutation/
// #medium
// Solution:
//   1. Find k -> n[i-1] > k[i]
//   2. Find l -> n[i] > n[k];
//   3. Swap k and l
//   4. Reverse k+1 -> end

/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
let nextPermutation = function(nums) {
  let k = -1;
  for (let i = 1; i < nums.length; i++) {
    if (nums[i - 1] < nums[i]) {
      k = i - 1;
    }
  }

  if (k === -1) {
    nums.reverse();
  } else {
    let l = 0;
    for (let i = 0; i < nums.length; i++) {
      if (nums[i] > nums[k]) {
        l = i;
      }
    }

    // swap
    let kEl = nums[k];
    let lEl = nums[l];
    nums[l] = kEl;
    nums[k] = lEl;

    let i = k + 1;
    let j = nums.length - 1;
    while (i < j) {
      let a = nums[i];
      let b = nums[j];
      nums[j] = a;
      nums[i] = b;
      i++;
      j--;
    }
  }

  return nums;
};

console.log(nextPermutation([1, 2, 3]), "1,3,2");
console.log(nextPermutation([3, 2, 1]), "1,2,3");
console.log(nextPermutation([1, 1, 5]), "1,5,1");
console.log(nextPermutation([1, 3, 2]), "2,1,3");
