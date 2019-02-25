// Longest Substring Without Repeating Characters
// #url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
// #medium
//
// Example:
//   Input: "abcabcbb"
//   Output: 3
//   Explanation: The answer is "abc", with the length of 3.
//
// Questions to ask:
//   ???
//
// Solution (naive):
//   1. Iterate over characters
//   2. Check if character already exists in a new substring
//     2.1. If doesn't add it to a new substring
//     2.2. if does, check length and update longest substring length
//   3. Substring from duplicate index to the end of the string
//   4. Continue going through characters

// O(n^2)
// fn length_of_longest_substring(s: String) -> i32 {
//   let mut substr_l: i32 = 0;
//   let mut substr = String::from("");

//   for x in s.chars() {
//     if substr_l < substr.len() as i32 {
//       substr_l = substr.len() as i32;
//     }

//     if substr.contains(x) {
//       let index = substr.find(x).unwrap();
//       let new_str = substr.clone();
//       let (_, new_substr) = new_str.split_at(index + 1);
//       substr = String::from(new_substr);
//     }

//     substr.push(x);
//   }

//   if substr_l < substr.len() as i32 {
//     substr_l = substr.len() as i32;
//   }

//   substr_l
// }

use std::collections::HashMap;
use std::cmp;

// Sliding Window Optimized
fn length_of_longest_substring(s: String) -> i32 {
  let byte_str = s.as_bytes();
  let n = s.len();
  let mut result = 0;
  let mut map = HashMap::new();
  let mut i = 0;

  for j in 0..n {
    let chr = byte_str[j];
    if map.contains_key(&chr) {
      i = cmp::max(*map.get(&chr).unwrap(), i);
    }
    result = cmp::max(result, j - i + 1);
    map.insert(chr, j + 1);
  }

  result as i32
}

fn main() {
  println!("{:?}", length_of_longest_substring(String::from("dvdf")))
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_len1() {
    assert_eq!(length_of_longest_substring(String::from("abcabcbb")), 3);
  }

  #[test]
  fn test_len2() {
    assert_eq!(length_of_longest_substring(String::from("bbbbb")), 1);
  }

  #[test]
  fn test_len3() {
    assert_eq!(length_of_longest_substring(String::from("pwwkew")), 3);
  }

  #[test]
  fn test_len4() {
    assert_eq!(length_of_longest_substring(String::from(" ")), 1);
  }
}
