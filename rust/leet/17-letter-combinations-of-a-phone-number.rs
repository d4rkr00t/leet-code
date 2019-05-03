// Letter Combinations of a Phone Number
// #url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
// #medium
//
// Solution:
use std::collections::HashMap;

fn build_combinations(
  digits: &str,
  char_idx: usize,
  prefix: &str,
  map: &HashMap<char, Vec<char>>,
) -> Vec<String> {
  if char_idx >= digits.len() {
    return vec![];
  }

  let c = digits.chars().nth(char_idx).unwrap();
  if c == '1' {
    return build_combinations(digits, char_idx + 1, prefix, map);
  }

  let letters = map.get(&c).unwrap();
  let mut result = vec![];
  for l in letters {
    let combs = build_combinations(digits, char_idx + 1, &l.to_string(), map);
    if combs.len() >= 1 {
      for comb in combs {
        result.push(format!("{}{}", prefix, comb))
      }
    } else {
      result.push(format!("{}{}", prefix, l));
    }
  }

  result
}

fn letter_combinations(digits: String) -> Vec<String> {
  let map: HashMap<char, Vec<char>> = [
    ('2', vec!['a', 'b', 'c']),
    ('3', vec!['d', 'e', 'f']),
    ('4', vec!['g', 'h', 'i']),
    ('5', vec!['j', 'k', 'l']),
    ('6', vec!['m', 'n', 'o']),
    ('7', vec!['p', 'q', 'r', 's']),
    ('8', vec!['t', 'u', 'v']),
    ('9', vec!['w', 'x', 'y', 'z']),
  ].iter()
    .cloned()
    .collect();
  return build_combinations(&digits, 0, "", &map);
}

fn main() {
  println!("{:?}", letter_combinations(String::from("2314")))
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
