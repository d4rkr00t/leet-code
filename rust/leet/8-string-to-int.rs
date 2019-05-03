// String to Integer (atoi)
// #url: https://leetcode.com/problems/string-to-integer-atoi/
// #medium
//
// Implement atoi which converts a string to an integer.
//
// Conditions:
//   1. String can contain whitespace characters
//   2. String can contain additional characters
//   3. Ignore If the first sequence of non-whitespace characters in str is not a valid integral number.
//   4. If no valid conversion could be performed, a zero value is returned.
//
// Solution:
//   1. Check 3 and 4
//   2. Filter non numeric characters
//   3. Try and convert to number
//   4. Return 0 if 3 fails

fn my_atoi(str: String) -> i32 {
  let closest_number_idx = str.chars().enumerate().position(|(_, s)| s.is_numeric()).unwrap_or(0);
  let last_number_idx = str.chars().enumerate().position(|(_, s)| s.is_numeric()).unwrap_or(0);
  let closest_non_number_idx = str.chars().enumerate().position(|(_, s)| s.is_alphabetic()).unwrap_or(str.len());
  println!("{:?} {:?}", closest_number_idx, closest_non_number_idx);

  if closest_non_number_idx < closest_number_idx {
    return 0;
  }

  let filtered_string: String = str[..closest_non_number_idx].chars().
        filter_map(|a| if a.is_numeric() || a == '-' || a == '.' || a == '+' { Some(a) } else { None }).
        collect::<Vec<_>>().
        into_iter().
        collect();

  println!("{:?}", filtered_string);

  let maybe_num = filtered_string.parse::<f32>();
  return match maybe_num {
    Err(e) => {
      if e.to_string() == "number too large to fit in target type" {
        return std::i32::MAX;
      }
      else if e.to_string() == "number too small to fit in target type" {
        return std::i32::MIN;
      }

      return 0;
    },
    Ok(i) => i as i32,
  };
}

fn main() {
  println!("{}", my_atoi(String::from("   +0 123")))
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_1() {
    assert_eq!(
      my_atoi(String::from("4193 with words")),
      4193
    );
  }

  #[test]
  fn test_2() {
    assert_eq!(
      my_atoi(String::from("42")),
      42
    );
  }

  #[test]
  fn test_3() {
    assert_eq!(
      my_atoi(String::from("   -42")),
      -42
    );
  }

  #[test]
  fn test_4() {
    assert_eq!(
      my_atoi(String::from("words and 987")),
      0
    );
  }

  #[test]
  fn test_5() {
    assert_eq!(
      my_atoi(String::from("-91283472332")),
      -2147483648
    );
  }

  #[test]
  fn test_6() {
    assert_eq!(
      my_atoi(String::from("3.14159")),
      3
    );
  }

  #[test]
  fn test_7() {
    assert_eq!(
      my_atoi(String::from("+-2")),
      0
    );
  }

  #[test]
  fn test_8() {
    assert_eq!(
      my_atoi(String::from("  -0012a42")),
      -12
    );
  }

  #[test]
  fn test_9() {
    assert_eq!(
      my_atoi(String::from("   +0 123")),
      0
    );
  }
}
