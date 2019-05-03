// Rotate Image
// #url: https://leetcode.com/problems/rotate-image/
// #medium
//
// Given input matrix =
// [
//   [1,2,3],     [1,4,7],     [7,4,1],
//   [4,5,6], ->  [2,5,8], ->  [8,5,2],
//   [7,8,9]      [3,6,9]      [9,6,3]
// ],
// rotate the input matrix in-place such that it becomes:
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ]
//
// [
//   [ 5, 1, 9,11]    [5,  2, 13, 15]
//   [ 2, 4, 8,10] -> [1,  4, 3,  6]
//   [13, 3, 6, 7]    [9,  8, 6,  12]
//   [15,14,12,16]    [11, 10, 7, 16]
// ],
//
// [ x
// y [1, 2, 3, 4, 5],
//   [1, 2, 3, 4, 5],
//   [1, 2, 3, 4, 5],
//   [1, 2, 3, 4, 5],
//   [1, 2, 3, 4, 5]
// ];

/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
let rotate = function(matrix) {
  // transpose
  let x = 0;
  let y = 1;
  while (x < matrix.length || y < matrix.length) {
    if (y === matrix.length) {
      x++;
      y = x;
      continue;
    }

    let a = matrix[x][y];
    let b = matrix[y][x];
    matrix[x][y] = b;
    matrix[y][x] = a;
    y++;
  }

  // reverse
  matrix.forEach(row => row.reverse());

  return matrix;
};

console.log("Actaul:   ", rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));
console.log("Expected: ", [[7, 4, 1], [8, 5, 2], [9, 6, 3]]);
