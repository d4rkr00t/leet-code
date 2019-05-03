// Reverse Linked List II
// #url: https://leetcode.com/problems/reverse-linked-list-ii/
// #medium
//
// Note: 1 ≤ m ≤ n ≤ length of list.
// Example:
// Input: 1->2->3->4->5->NULL, m = 2, n = 4
// Output: 1->4->3->2->5->NULL

function ListNode(val) {
  this.val = val;
  this.next = null;
}

ListNode.prototype.toString = function() {
  let result = [];
  let next = this;
  while (next) {
    result.push(next.val);
    next = next.next;
  }
  return result.join("->");
};

/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
let reverseBetween = function(head, m, n) {
  if (!head) return;

  let stop = false;
  let left = head;

  function recurseAndReverse(right, m, n) {
    if (n === 1) return;

    right = right.next;

    if (m > 1) {
      left = left.next;
    }

    recurseAndReverse(right, m - 1, n - 1);

    if (left === right || right.next === left) {
      stop = true;
    }

    if (!stop) {
      let rv = right.val;
      let lv = left.val;
      right.val = lv;
      left.val = rv;
      left = left.next;
    }
  }

  recurseAndReverse(head, m, n);
  return head;
};

console.log(
  reverseBetween(buildList([1, 2, 3, 4, 5]), 2, 4).toString(),
  "1->4->3->2->5"
);
console.log(
  reverseBetween(buildList([1, 2, 3, 4, 5]), 1, 5).toString(),
  "5->4->3->2->1"
);
console.log(
  reverseBetween(buildList([1, 2, 3, 4, 5]), 3, 4).toString(),
  "1->2->4->3->5"
);

function buildList(arr) {
  return arr.reverse().reduce((acc, item) => {
    let node = new ListNode(item);
    node.next = acc;
    return node;
  }, null);
}
