// Remove Nth Node From End of List
// #url: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
// #medium
// Solution:
//   1. Go through list creating array of node references
//   2. Once all done get arr.len - n index
//   3. Get [2] + 1 and [2] - 1 nodes
//   4. Create a new list without [2]

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
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

fn remove_nth_from_end(head: Option<Box<ListNode>>, n: i32) -> Option<Box<ListNode>> {
  let mut node_to_idx: Vec<&ListNode> = vec![];
  let mut cur = &head;
  loop {
    match cur {
      &Some(ref a) => {
        cur = &a.next;
        node_to_idx.push(&a);
      }
      &None => break,
    };
  }

  let len = node_to_idx.len();
  let remove_idx = len - (n as usize);
  let remove_node = node_to_idx[remove_idx];

  if remove_idx == 0 {
    return remove_node.next.clone();
  }

  node_to_idx.iter().rev().fold(None, |list, val| {
    if val == &remove_node {
      return list;
    }
    let mut new_list = ListNode::new((*val.clone()).val);
    new_list.next = list;
    Some(Box::new(new_list))
  })
}

fn main() {
  // 1, 2, 3, 5
  println!(
    "{:?}",
    remove_nth_from_end(create_list(vec![1, 2, 3, 4, 5]), 2)
  );
}

fn create_list(args: Vec<i32>) -> Option<Box<ListNode>> {
  args.iter().rev().fold(None, |list, val| {
    let mut new_list = ListNode::new(*val);
    new_list.next = list;
    Some(Box::new(new_list))
  })
}
