/**
 * @param {number[]} arr
 */
function flatten(arr) {
  let stack = arr.reverse();
  let result = [];
  while (stack.length) {
    while (stack.length) {
      let cur = stack.pop();
      if (Array.isArray(cur)) {
        stack.push(...cur.reverse());
      } else {
        result.push(cur);
      }
    }
  }

  return result;
}

console.log(flatten([1, 2, 3, 4, [5, 6, [7, 8, 9]], 10, 11, 12]));
console.log(flatten([1, 2, 3, 4, [5, 6, [7, [8], 9]], 10, 11, 12]));
console.log(flatten([1, 2, 3, 4, [5, 6, [7, [8], 9]], [[10]], 11, 12]));
console.log(flatten([1, 2, 3, 4, [[[[5, 6, [7, [8], 9]], [[10]], 11]]], 12]));
