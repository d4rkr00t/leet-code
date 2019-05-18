// Reverse Bits
// #url: https://leetcode.com/problems/reverse-bits/
// #easy

/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
let reverseBits = function(n) {
  let result = 0;
  let count = 32;

  while (count--) {
    result *= 2;
    result += n & 1;
    n = n >> 1;
  }
  return result;
};

console.log(
  reverseBits(0b00000010100101000001111010011100),
  0b00111001011110000010100101000000
);
