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

use std::cmp;

fn lcs_length(str1: String, str2: String) -> usize {
  let str1_len: usize = str1.len();
  let str2_len: usize = str2.len();
  let mut lookup = vec![vec![0 as usize; str1_len + 1]; str2_len + 1];

  for i in 1..(str1_len + 1) {
    for j in 1..(str2_len + 1) {
      if str1.chars().nth(i - 1) == str2.chars().nth(j - 1) {
        lookup[i][j] = lookup[i - 1][j - 1] + 1;
      } else {
        lookup[i][j] = cmp::max(lookup[i - 1][j], lookup[i][j - 1]);
      }
    }
  }

  return lookup[str1_len][str2_len];
}

fn main() {
  println!(
    "{:?}",
    lcs_length(String::from("XMJYAUZ"), String::from("MZJAWXU"))
  )
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_1() {
    assert_eq!(true, true);
  }
}
