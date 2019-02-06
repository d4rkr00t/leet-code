// Add Two Numbers
// #url: https://leetcode.com/problems/add-two-numbers/
// #medium
//
// Example:
//   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
//   Output: 7 -> 0 -> 8
//   Explanation: 342 + 465 = 807.
//
// Questions to ask:
//   1. Are they always same length?
//   2. Can be of length 1?
//
// Solution:
//   1. Get next value of a list

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>,
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode { next: None, val }
  }
}

fn get_clean_value(sum: i32, d: i32) -> (i32, i32) {
  let new_sum = sum + d;
  let new_d = new_sum / 10;
  (new_sum - (new_d * 10), new_d)
}

fn add_two_numbers(l1: Option<Box<ListNode>>, l2: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
  let mut result: Vec<i32> = vec![];
  let mut l1p = &l1;
  let mut l2p = &l2;
  let mut d: i32 = 0;

  loop {
    match (l1p, l2p) {
      (&Some(ref a), &Some(ref b)) => {
        let (new_sum, new_d) = get_clean_value(&a.val + &b.val, d);
        d = new_d;
        result.push(new_sum);
        l1p = &a.next;
        l2p = &b.next;
      }
      (&Some(ref a), &None) => {
        let (new_sum, new_d) = get_clean_value(a.val, d);
        d = new_d;
        result.push(new_sum);
        l1p = &a.next;
      }
      (&None, &Some(ref b)) => {
        let (new_sum, new_d) = get_clean_value(b.val, d);
        d = new_d;
        result.push(new_sum);
        l2p = &b.next;
      }
      _ => {
        if d > 0 {
          result.push(d);
        }
        break;
      }
    }
  }

  create_list(result)
}

fn create_list(args: Vec<i32>) -> Option<Box<ListNode>> {
  args.iter().rev().fold(None, |list, val| {
    let mut new_list = ListNode::new(*val);
    new_list.next = list;
    Some(Box::new(new_list))
  })
}

// fn main() {
//   println!(
//     "{:?}",
//     add_two_numbers(create_list(vec![2, 4, 3]), create_list(vec![5, 6, 4]))
//   )
// }

fn main() {
  println!(
    "{:?}",
    add_two_numbers(create_list(vec![9, 8]), create_list(vec![1]))
  )
}

#[cfg(test)]
mod tests {
  // Note this useful idiom: importing names from outer (for mod tests) scope.
  use super::*;

  #[test]
  fn test_add1() {
    assert_eq!(
      add_two_numbers(create_list(vec![9, 8]), create_list(vec![1])),
      create_list(vec![0, 9])
    );
  }

  #[test]
  fn test_add2() {
    assert_eq!(
      add_two_numbers(create_list(vec![1, 8]), create_list(vec![0])),
      create_list(vec![1, 8])
    );
  }

  #[test]
  fn test_add3() {
    assert_eq!(
      add_two_numbers(create_list(vec![5]), create_list(vec![5])),
      create_list(vec![0, 1])
    );
  }

  #[test]
  fn test_add4() {
    assert_eq!(
      add_two_numbers(create_list(vec![2, 4, 3]), create_list(vec![5, 6, 4])),
      create_list(vec![7, 0, 8])
    );
  }
}
