// ZigZag Conversion
// #url: https://leetcode.com/problems/zigzag-conversion/
// #medium
//
// Example 1:
//   Input: "PAYPALISHIRING" 3
//   Output:
//     P   A   H   N
//     A P L S I I G
//     Y   I   R
//
// Questions to ask:
//   TBD
//
// Things to consider:
//   TBD
//
// Solution:
//   1   3   5
//   1 2 3 4 5
//   1   3   5
//
//   1    4    7  P     I     N
//   1  3 4  6 7  A   L S   I G
//   1 2  4 5  7  Y A   H R
//   1    4    7  P     I
//
//   1     5     9
//   1   4 5   8 9
//   1  3  5  7  9
//   1 2   5 6   9
//   1     5     9
//
//   1      5     9
//   1    5 5   8 9
//   1   4  5  7  9
//   1  3   5 6   9
//   1 2    5     9
//   1      5     9
//
use std::cmp;

fn convert(s: String, num_rows: i32) -> String {
  let mut rows: Vec<String> = vec![];

  if num_rows == 1 {
    return s;
  }

  for _ in 0..cmp::min(num_rows, s.len() as _) {
    rows.push(String::new());
  }

  let mut current_row: i32 = 0;
  let mut going_down = false;

  for (i, c) in s.chars().enumerate() {
    rows[current_row as usize].push(c);
    if (current_row == 0 || current_row == num_rows - 1) {
      going_down = !going_down;
    }
    current_row += if going_down { 1 } else { -1 };
  }

  let mut result = String::new();

  for row in rows {
    result = format!("{}{}", result, row);
  }

  result
}

fn main() {
  println!("{}", convert(String::from("PAYPALISHIRING"), 4));
}
