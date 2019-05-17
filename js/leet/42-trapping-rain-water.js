// Trapping Rain Water
// #url: https://leetcode.com/problems/trapping-rain-water/
// #hard

/**
 * @param {number[]} height
 * @return {number}
 */
let trap = function(height) {
  let ans = 0;
  let cur = 1;
  let stack = [0];
  while (cur < height.length) {
    let curH = height[cur];

    while (stack.length && curH > height[stack[stack.length - 1]]) {
      let top = stack.pop();
      if (!stack.length) {
        break;
      }
      let newTop = stack[stack.length - 1];
      let distance = cur - newTop - 1;
      let minHeight = Math.min(curH, height[newTop]) - height[top];
      ans += distance * minHeight;
    }

    stack.push(cur);
    cur++;
  }

  return ans;
};

/**
 *               3
 *       2 # # # 3 2 # 2
 * _ 1 # 2 1 # 1 3 2 1 2  1
 * 0 1 2 3 4 5 6 7 8 9 10 11
 */
console.log(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6);

/**
 * 4
 * 4 # 3
 * 4 2 3
 * 4 2 3
 */
console.log(trap([4, 2, 3]), 1);
