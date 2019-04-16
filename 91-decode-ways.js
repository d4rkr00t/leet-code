// Decode Ways
// #url: https://leetcode.com/problems/decode-ways/
// #medium
//
// Input: "226"
// Output: 3
// Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

function decode(s, cache, pos) {
  if (pos >= s.length) {
    return 1;
  }

  if (cache[pos] > -1) {
    return cache[pos];
  }

  let totalWays = 0;

  if (pos + 1 <= s.length && s[pos] !== "0") {
    totalWays += decode(s, cache, pos + 1);
  }

  if (pos + 2 <= s.length) {
    let d = +s.substr(pos, 2);
    if (d > 0 && d < 27 && s[pos] !== "0") {
      totalWays += decode(s, cache, pos + 2);
    }
  }

  cache[pos] = totalWays;
  return totalWays;
}

/**
 * @param {string} s
 * @return {number}
 */
var numDecodings = function(s) {
  let cache = new Array(s.length).fill(-1);
  return decode(s, cache, 0);
};

console.log(numDecodings("226"), 3);
console.log(numDecodings("12"), 2);
console.log(numDecodings("120"), 1);
console.log(numDecodings("27"), 1);
console.log(numDecodings("00"), 0);
console.log(numDecodings("01"), 0);
console.log(numDecodings("12120"), 3);
