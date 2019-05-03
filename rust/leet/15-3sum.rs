// 3Sum
// #url: https://leetcode.com/problems/3sum/
// #medium
//
// Solution:
//   https://en.wikipedia.org/wiki/3SUM

use std::collections::HashMap;

fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
  if nums.len() < 3 {
    return vec![];
  }

  let mut sorted_nums = nums.clone();
  sorted_nums.sort();
  let mut i: usize = 0;
  let mut results = HashMap::new();

  while i < sorted_nums.len() - 2 {
    let a = sorted_nums[i];
    let mut start = i + 1;
    let mut end = sorted_nums.len() - 1;

    while start < end {
      let b = sorted_nums[start];
      let c = sorted_nums[end];

      if a + b + c == 0 {
        results.insert(format!("{}{}{}", a, b, c), vec![a, b, c]);
        start = start + 1;
        end = end - 1;
      } else if a + b + c > 0 {
        end = end - 1;
      } else {
        start = start + 1;
      }
    }
    i += 1;
  }

  results.iter().map(|(_, res)| res.clone()).collect()
}

fn main() {
  println!("{:?}", three_sum(vec![-1, 0, 1, 2, -1, -4]))
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
