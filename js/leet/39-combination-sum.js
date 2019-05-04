// Interval List Intersections
// #url: https://leetcode.com/problems/combination-sum/
// #medium

/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
let combinationSum = function(candidates, target) {
  let sum = (pos, prev, s) => {
    if (pos >= candidates.length) {
      return s === target ? [prev] : [];
    }

    let cur = candidates[pos];
    if (cur + s === target) {
      return [prev.concat(cur), ...sum(pos + 1, prev, s)];
    } else if (cur + s > target) {
      return sum(pos + 1, prev, s);
    }
    return [...sum(pos, prev.concat(cur), s + cur), ...sum(pos + 1, prev, s)];
  };

  return [...sum(0, [candidates[0]], candidates[0]), ...sum(1, [], 0)];
};

console.log(combinationSum([2, 3, 6, 7], 7));
console.log([[7], [2, 2, 3]]);
console.log();
console.log(combinationSum([2, 3, 5], 8));
console.log([[2, 2, 2, 2], [2, 3, 3], [3, 5]]);
console.log();
console.log(combinationSum([1], 1));
console.log([[1]]);
console.log();
