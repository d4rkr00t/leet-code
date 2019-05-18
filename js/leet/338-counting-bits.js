// Counting Bits
// #url: https://leetcode.com/problems/counting-bits/
// #medium

/**
 * @param {number} num
 * @return {number[]}
 */
let countBits = function(num) {
  let c = 0;
  let res = [];

  while (c <= num) {
    let subC = c;
    let subRes = 0;

    while (subC > 0) {
      subRes += subC & 1;
      subC = subC >>> 1;
    }

    res.push(subRes);
    c++;
  }

  return res;
};

console.log(countBits(2), [0, 1, 1]);
console.log(countBits(5), [0, 1, 1, 2, 1, 2]);
