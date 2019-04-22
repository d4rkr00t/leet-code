// Permutations
// #url: https://leetcode.com/problems/permutations/
// #medium
//
// Input: [1,2,3]
// Output:
// [
//   [1,2,3],
//   [1,3,2],
//   [2,1,3],
//   [2,3,1],
//   [3,1,2],
//   [3,2,1]
// ]
// Input: [1,2,3,4]
// Output:
// [
//   [1,2,3,4], [1] [2, 3, 4]
//   [1,4,3,2], [1] [4, 3, 2]
//   [1,3,4,2],
//   [1,2,4,3],
//   [1,3,2,4],
//   [1,4,2,3],
// ]
//
// 1. Find the largest index k such that a[k] < a[k + 1]. If no such index exists, the permutation is the last permutation.
// 2. Find the largest index l greater than k such that a[k] < a[l].
// 3. Swap the value of a[k] with that of a[l].
// 4. Reverse the sequence from a[k + 1] up to and including the final element a[n].
//
// 1, 2, 3 | k = 1, l = 2
// 1, 3, 2 | k = 0, l = 1
// 3, 2, 1

/**
 * @param {number[]} nums
 * @return {number[][]}
 */
let permute = function(nums) {
  let k = nums.length - 2;
  let l = nums.length - 1;
  let cur = [].concat(nums).sort((a, b) => a - b);
  let permutations = [[].concat(cur)];

  while (k !== -1) {
    // swap
    let kEl = cur[k];
    let lEl = cur[l];
    cur[l] = kEl;
    cur[k] = lEl;

    // reverse curr[k + 1]
    let start = cur.slice(0, k + 1);
    let end = cur.slice(k + 1, cur.length);

    cur = start.concat(end.length >= 2 ? end.reverse() : end);
    permutations.push([].concat(cur));

    // find new k and l
    k = -1;
    for (let i = 1; i < cur.length; i++) {
      if (cur[i - 1] < cur[i]) {
        k = i - 1;
      }
    }

    l = 0;
    for (let i = 0; i < cur.length; i++) {
      if (cur[i] > cur[k]) {
        l = i;
      }
    }
  }

  return permutations;
};

console.log(permute([1, 2, 3]));
console.log(permute([1, 2, 3, 4]));
console.log(permute([0, -1, 1]));
console.log(permute([5, 4, 6, 2]));
