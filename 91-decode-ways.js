// Decode Ways
// #url: https://leetcode.com/problems/decode-ways/
// #medium
//
// Input: "226"
// Output: 3
// Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

/**
 * @param {string} s
 * @return {number}
 */
let numDecodings = function(s) {
  let dp = new Array(s.length + 1).fill(0);
  dp[0] = 1;
  dp[1] = s[0] === "0" ? 0 : 1;

  for (let i = 2; i <= s.length; i++) {
    let oneDigit = Number(s.substr(i - 1, 1));
    let twoDigits = Number(s.substr(i - 2, 2));

    if (oneDigit >= 1) {
      dp[i] += dp[i - 1];
    }
    if (twoDigits >= 10 && twoDigits <= 26) {
      dp[i] += dp[i - 2];
    }
  }

  return dp[s.length];
};

console.log(numDecodings("226"), 3);
console.log(numDecodings("12"), 2);
console.log(numDecodings("120"), 1);
console.log(numDecodings("27"), 1);
console.log(numDecodings("00"), 0);
console.log(numDecodings("01"), 0);
console.log(numDecodings("12120"), 3);
