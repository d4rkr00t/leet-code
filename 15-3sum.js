// 3Sum
// #url: https://leetcode.com/problems/3sum/
// #medium
//
// Solution:
//   https://en.wikipedia.org/wiki/3SUM

// function treeSum(arr, target = 0) {
//   if (arr.length < 3) return [];
//   arr = arr.sort((a, b) => a - b);

//   let result = {};
//   let i = 0;
//   while (i < arr.length - 2) {
//     let a = arr[i];
//     let start = i + 1;
//     let end = arr.length - 1;

//     while (start < end) {
//       let b = arr[start];
//       let c = arr[end];

//       if (a + b + c === target) {
//         result[`${a}${b}${c}`] = [a, b, c];
//         start++;
//         end--;
//       } else if (a + b + c > target) {
//         end--;
//       } else {
//         start++;
//       }
//     }

//     i++;
//   }
//   return Object.keys(result).map(key => result[key]);
// }

function treeSum(nums, target = 0) {
  if (nums.length < 3) return [];
  let result = [];
  for (let i = 0; i < nums.length; i++) {
    let set = new Set();
    let sum = target - nums[i];
    for (let j = i + 1; j < nums.length; j++) {
      if (set.has(sum - nums[j])) {
        console.log(nums[i], nums[j], sum - nums[j]);
        let item = [nums[i], nums[j], sum - nums[j]].sort((a, b) => a - b);
        result[item.join("")] = item;
      }
      set.add(nums[j]);
    }
  }

  return Object.keys(result).map(key => result[key]);
}

console.log(treeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]]);
