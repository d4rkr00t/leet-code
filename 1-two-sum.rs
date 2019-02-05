// Two Sum
// #url: https://leetcode.com/problems/two-sum/
// #easy
//
// Questions to ask:
//   1. Can there be negative numbers?
//   2. Can there be duplicates / more than 1 solution?
//
// Solution:
//   1. Create a Map where key is current value and value is an index
//   2. If target - cur exist in the Map print it

use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
  let mut map = HashMap::new();
  let mut res: Vec<i32> = vec![];

  for (i, x) in nums.iter().enumerate() {
    let diff = target - x;
    if map.contains_key(&diff) {
      res.push(*map.get(&diff).unwrap());
      res.push(i as i32);
      break;
    } else {
      map.insert(x, i as i32);
    }
  }

  res
}

fn main() {
  println!("{:?}", two_sum(vec![2, 7, 11, 15], 9))
}
