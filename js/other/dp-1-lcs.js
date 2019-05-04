// Longest Common Subsequence
// #url: https://www.techiedelight.com/longest-common-subsequence/
// #dp
//
// Table:
//       0 1 2 3 4 5 6 7
//      () M Z J A W X U
//  0 () 0 0 0 0 0 0 0 0
//  1 X  0 0 0 0 0 0 1 1
//  2 M  0 1 1 1 1 1 1 1
//  3 J  0 1 1 2 2 2 2 2
//  4 Y  0 1 1 2 2 2 2 2
//  5 A  0 1 1 2 3 3 3 3
//  6 U  0 1 1 2 3 3 3 4
//  7 Z  0 1 2 2 3 3 3 4

function create2DArr(n, m, pl = 0) {
  return new Array(n).fill(0).map(_ => new Array(m).fill(pl));
}

/**
 * @param {string} str1
 * @param {string} str2
 */
function lcs(str1, str2) {
  let table = create2DArr(str1.length + 1, str2.length + 1, 0);

  for (let i = 1; i <= str1.length; i++) {
    for (let j = 1; j <= str2.length; j++) {
      let a = str1[i - 1];
      let b = str2[j - 1];
      if (a === b) {
        table[i][j] = table[i - 1][j - 1] + 1;
      } else {
        table[i][j] = Math.max(table[i][j - 1], table[i - 1][j]);
      }
    }
  }

  return table[str1.length][str2.length];
}

console.log(lcs("XMJYAUZ", "MZJAWXU"));
