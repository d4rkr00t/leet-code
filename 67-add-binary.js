// Unique Paths II
// #url: https://leetcode.com/problems/add-binary/
// #easy
//
// Input: a = "11", b = "1"
// Output: "100"

// Input: a = "1010", b = "1011"
// Output: "10101"

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
let addBinary = function(a, b) {
  let len = Math.max(a.length, b.length);
  let result = [];
  let carry = 0;
  let ar = a.split("").reverse();
  let br = b.split("").reverse();

  for (let i = 0; i < len; i++) {
    let ac = ar[i] === "1" ? 1 : 0;
    let bc = br[i] === "1" ? 1 : 0;

    result.push((ac + bc + carry) % 2);
    carry = Math.floor((ac + bc + carry) / 2);
  }

  return result
    .concat(carry || undefined)
    .reverse()
    .join("");
};

console.log(addBinary("11", "1"), "100");
console.log(addBinary("1010", "1011"), "10101");
console.log(addBinary("0", "0"), "0");
console.log(addBinary("1111", "1111"), "11110");
