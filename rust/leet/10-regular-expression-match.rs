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

fn slice_safe(s: String, from: usize) -> String {
  if from > s.len() {
    return String::new();
  }

  return s[from..].to_owned();
}

fn is_match(s: String, p: String) -> bool {
  if p.is_empty() {
    return s.is_empty();
  }

  let first_match = !s.is_empty() && (p.chars().nth(0).unwrap() == s.chars().nth(0).unwrap() || p.chars().nth(0).unwrap() == '.');

  if p.len() >= 2 && p.chars().nth(1).unwrap_or('1') == '*' {
    return is_match(s.clone(), slice_safe(p.clone(), 2)) || (first_match && is_match(slice_safe(s.clone(), 1), p));
  }

  return first_match && is_match(slice_safe(s.clone(), 1), slice_safe(p.clone(), 1));
}

fn main() {
  println!("{}", is_match(String::from("ab"), String::from(".*c")));
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_1() {
    assert_eq!(
      is_match(String::from("aab"), String::from("c*a*b")),
      true
    );
  }

  #[test]
  fn test_2() {
    assert_eq!(
      is_match(String::from("aa"), String::from("a")),
      false
    );
  }

  #[test]
  fn test_3() {
    assert_eq!(
      is_match(String::from("aa"), String::from("a*")),
      true
    );
  }

  #[test]
  fn test_4() {
    assert_eq!(
      is_match(String::from("mississippi"), String::from("mis*is*p*.")),
      false
    );
  }

  #[test]
  fn test_5() {
    assert_eq!(
      is_match(String::from("ab"), String::from(".*c")),
      false
    );
  }

  #[test]
  fn test_6() {
    assert_eq!(
      is_match(String::from("aaa"), String::from("aaaa")),
      false
    );
  }

  #[test]
  fn test_7() {
    assert_eq!(
      is_match(String::from("aaaab"), String::from("a*aab")),
      true
    );
  }

  #[test]
  fn test_8() {
    assert_eq!(
      is_match(String::from("aaa"), String::from("ab*a*c*a")),
      true
    );
  }
}
