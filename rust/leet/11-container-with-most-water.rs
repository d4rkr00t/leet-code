// Container With Most Water
// #url: https://leetcode.com/problems/container-with-most-water/
// #medium
//
// Solution:
//  – Go from both sides decreasing range, recursively

use std::cmp;

fn max_area_with_cache(height: Vec<i32>) -> i32 {
  let mut max_area = 0;
  let mut l = 0;
  let mut r = height.len() - 1;

  while l < r {
    max_area = cmp::max(cmp::min(height[l], height[r]) * (r - l) as i32, max_area);

    if height[l] < height[r] {
      l += 1;
    } else {
      r -= 1;
    }
  }

  return max_area;
}

fn max_area(height: Vec<i32>) -> i32 {
  max_area_with_cache(height)
}

fn main() {
  // 49
  println!("{:?}", max_area(vec![2, 3, 4, 5, 18, 17, 6]))
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_1() {
    assert_eq!(max_area(vec![1, 8, 6, 2, 5, 4, 8, 3, 7]), 49);
  }
}
