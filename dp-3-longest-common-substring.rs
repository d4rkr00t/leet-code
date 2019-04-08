// Longest Common Substring
// #url: https://www.techiedelight.com/longest-common-substring-problem/
// #dp
//
// [0, 0, 0, 0, 0],
// [0, 0, 1, 0, 1],
// [0, 1, 0, 2, 0],
// [0, 0, 2, 0, 3],
// [0, 1, 0, 3, 0]
//
// [0, 0, 0, 0],
// [0, 0, 1, 0],
// [0, 1, 0, 0],
// [0, 0, 2, 0],
// [0, 0, 0, 0]
//
//       B  A  B  A
//   [0, 0, 0, 0, 0],
// A [0, 0, 1, 0, 0],
// B [0, 1, 0, 2, 0],
// A [0, 0, 2, 0, 0],
// B [0, 0, 0, 0, 0]

use std::cmp;

fn lcs(x: &str, y: &str, m: usize, n: usize) -> String {
  let mut max_len = 0;
  let mut ending_idx = m;
  let mut lookup = vec![vec![0 as usize; cmp::max(m + 1, n + 1)]; cmp::max(m + 1, n + 1)];

  for i in 1..(m + 1) {
    for j in 1..(n + 1) {
      if x.chars().nth(i - 1) == y.chars().nth(j - 1) {
        lookup[i][j] = lookup[i - 1][j - 1] + 1;
        if lookup[i][j] > max_len {
          max_len = lookup[i][j];
          ending_idx = i;
        }
      }
    }
  }

  x[(ending_idx - max_len)..(max_len)].to_owned()
}

fn main() {
  let x = "ABAB";
  // let x = "ABC";
  let y = "BABA";
  println!("{:?}", lcs(&x, &y, x.len(), y.len()))
}
