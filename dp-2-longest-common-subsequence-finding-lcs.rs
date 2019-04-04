// Longest Common Subsequence | Finding all LCS
// #url: https://www.techiedelight.com/longest-common-subsequence-finding-lcs/
// #dp

use std::cmp;
use std::collections::HashSet;

fn lcs_length(str1: &str, str2: &str) -> Vec<Vec<usize>> {
  let str1_len: usize = str1.len();
  let str2_len: usize = str2.len();
  let mut lookup = vec![vec![0 as usize; str2_len + 1]; str1_len + 1];

  for i in 1..(str1_len + 1) {
    for j in 1..(str2_len + 1) {
      if str1.chars().nth(i - 1) == str2.chars().nth(j - 1) {
        lookup[i][j] = lookup[i - 1][j - 1] + 1;
      } else {
        lookup[i][j] = cmp::max(lookup[i - 1][j], lookup[i][j - 1]);
      }
    }
  }

  return lookup;
}

fn dedupe(vec: Vec<String>) -> Vec<String> {
  let mut results = HashSet::new();
  for s in vec {
    results.insert(s);
  }
  results.iter().map(|res| res.clone()).collect()
}

fn lcs(str1: &str, str2: &str, lookup: &Vec<Vec<usize>>, m: usize, n: usize) -> Vec<String> {
  if m == 0 || n == 0 {
    return vec![String::new()];
  }

  if str1.chars().nth(m - 1).unwrap() == str2.chars().nth(n - 1).unwrap() {
    let all_lcs = lcs(str1, str2, lookup, m - 1, n - 1);
    let mut result_lcs: Vec<String> = vec![];
    for l in all_lcs {
      result_lcs.push(format!("{}{}", l, str1.chars().nth(m - 1).unwrap()));
    }
    return result_lcs;
  }

  if lookup[m - 1][n] > lookup[m][n - 1] {
    return lcs(str1, str2, lookup, m - 1, n);
  }

  if lookup[m][n - 1] > lookup[m - 1][n] {
    return lcs(str1, str2, lookup, m, n - 1);
  }

  let mut top = lcs(str1, str2, lookup, m - 1, n);
  let mut left = lcs(str1, str2, lookup, m, n - 1);

  top.append(&mut left);

  return dedupe(top);
}

fn main() {
  // let str1 = String::from("XMJYAUZ");
  // let str2 = String::from("MZJAWXU");
  let str1 = String::from("ABCBDAB");
  let str2 = String::from("BDCABA");
  let str1_len = str1.len();
  let str2_len = str2.len();
  let lookup = lcs_length(&str1, &str2);

  // println!("{:?}", lookup);
  println!("{:?}", lcs(&str1, &str2, &lookup, str1_len, str2_len))
}
