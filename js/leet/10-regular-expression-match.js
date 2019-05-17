// Regular Expression Matching
// #url: https://leetcode.com/problems/regular-expression-matching/
// #hard #recursion #dynamic programming
//
// Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
//
// Conditions:
//   – s could be empty and contains only lowercase letters a-z.
//   – p could be empty and contains only lowercase letters a-z, and characters like . or *.
//

/**
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
// var isMatch = function(s, p) {
//   if (!p.length) {
//     return !s.length;
//   }

//   let isFirstMatch = Boolean(s.length && (s[0] === p[0] || p[0] === "."));

//   if (p[1] === "*") {
//     return isMatch(s, p.substr(2)) || (isFirstMatch && isMatch(s.substr(1), p));
//   }
//   return isFirstMatch && isMatch(s.substr(1), p.substr(1));
// };

//   a a b
// c 1 1 1
// * 1 1 1
// a 1 1 1
// * 1 1 1
// b 0 0 1

/**
 * DP approach
 * @param {string} s
 * @param {string} p
 * @return {boolean}
 */
var isMatch = function(s, p) {
  let dp = new Array(s.length + 1)
    .fill(true)
    .map(() => new Array(p.length + 1).fill(false));

  dp[s.length][p.length] = true;

  for (let i = s.length; i >= 0; i--) {
    for (let j = p.length - 1; j >= 0; j--) {
      let isFirstMatch = Boolean(
        i < s.length && (s[i] === p[j] || p[j] === ".")
      );

      if (j + 1 < p.length && p[j + 1] === "*") {
        dp[i][j] = dp[i][j + 2] || (isFirstMatch && dp[i + 1][j]);
      } else {
        dp[i][j] = isFirstMatch && dp[i + 1][j + 1];
      }
    }
  }

  return dp[0][0];
};

/**
 *   a b
 * a 1 0 0
 * b 0 1 0
 *   0 0 1
 */
console.log(isMatch("ab", "ab"), true);

/**
 *    a *
 *  a 1 0 0
 *  a 1 0 0
 *    1 0 1
 */
console.log(isMatch("aa", "a*"), true);

/**
 *    . * c
 *  a 0 0 0 0
 *  b 0 0 0 0
 *    0 0 0 1
 */
console.log(isMatch("ab", ".*c"), false);
console.log(isMatch("aab", "c*a*b"), true);
console.log(isMatch("aa", "a"), false);
console.log(isMatch("mississippi", "mis*is*p*."), false);
console.log(isMatch("aaa", "aaaa"), false);
console.log(isMatch("aaaab", "a*aab"), true);
console.log(isMatch("aaa", "ab*a*c*a"), true);
