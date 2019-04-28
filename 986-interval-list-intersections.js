// Interval List Intersections
// #url: https://leetcode.com/problems/interval-list-intersections/
// #medium

/**
 * @param {number[][]} A
 * @param {number[][]} B
 * @return {number[][]}
 */
let intervalIntersection = function(A, B) {
  let result = [];
  let ai = 0;
  let bi = 0;
  while (A[ai] && B[bi]) {
    let aa = A[ai];
    let bb = B[bi];
    // check if intersect
    let start = Math.max(bb[0], aa[0]);
    let end = Math.min(bb[1], aa[1]);
    if (start <= end) {
      result.push([start, end]);
    }

    if (bb[1] > aa[1]) {
      ai++;
    } else {
      bi++;
    }
  }

  return result;
};

console.log(
  intervalIntersection(
    [[0, 2], [5, 10], [13, 23], [24, 25]],
    [[1, 5], [8, 12], [15, 24], [25, 26]]
  )
);
console.log([[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]);
