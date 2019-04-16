// Unique Paths II
// #url: https://leetcode.com/problems/unique-paths-ii/
// #medium
//
// Input:
// [  s
//   [0,0,0],
//   [0,1,0],
//   [0,0,0]
// ]      f
// Output: 2

function walk(grid, pos, finish, cache) {
  if (grid[pos[0]][pos[1]] === 1) {
    return 0;
  }

  if (pos[0] === finish[0] && pos[1] === finish[1]) {
    return 1;
  }

  if (cache[pos.join()] !== undefined) {
    return cache[pos.join()];
  }

  let ways = 0;

  // if can go down
  if (grid[pos[0] + 1] && grid[pos[0] + 1][pos[1]] === 0) {
    ways += walk(grid, [pos[0] + 1, pos[1]], finish, cache);
  }

  // if can go right
  if (grid[pos[0]][pos[1] + 1] === 0) {
    ways += walk(grid, [pos[0], pos[1] + 1], finish, cache);
  }

  cache[pos.join()] = ways;

  return ways;
}

/**
 * @param {number[][]} obstacleGrid
 * @return {number}
 */
let uniquePathsWithObstacles = function(obstacleGrid) {
  let cache = {};
  let finish = [
    obstacleGrid.length - 1,
    obstacleGrid[obstacleGrid.length - 1].length - 1
  ];

  if (obstacleGrid[finish[0]][finish[1]] === 1) {
    return 0;
  }

  return walk(obstacleGrid, [0, 0], finish, cache);
};

console.log(uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]));
console.log(uniquePathsWithObstacles([[1]]));
console.log(uniquePathsWithObstacles([[1, 0]]));
