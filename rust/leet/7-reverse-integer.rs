// Reverse Integer
// #url: https://leetcode.com/problems/reverse-integer/
// #easy
//
// Given a 32-bit signed integer, reverse digits of an integer.
//
// Solution:
//   1. Figure out if negative or positive
//   2. Convert to string and reverse
//   3. Convert to number and add sign


fn reverse(x: i32) -> i32 {
  let is_positive = if x > 0 { true } else { false };
  let as_str = x.abs().to_string().chars().rev().collect::<String>();
  let maybe_num = as_str.parse::<i32>();
  return match maybe_num {
    Err(_) => 0,
    Ok(i) => if is_positive {
      i
    } else {
      -i
    },
  };
}

fn main() {
  println!("{}", reverse(-123));
}
