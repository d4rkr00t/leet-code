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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  let result = new ListNode(null);
  let current = result;

  let l1c = l1;
  let l2c = l2;
  let carry = 0;
  while (l1c !== null || l2c !== null) {
    let interim, newNode;
    if (l1c !== null && l2c !== null) {
      // if we have both of them -> add
      interim = l1c.val + l2c.val + carry;
    } else {
      // take whatever is not null + carry
      interim = (l1c || l2c).val + carry;
    }

    carry = Math.floor(interim / 10);
    newNode = new ListNode(interim % 10);
    current.next = newNode;
    current = newNode;

    l1c = l1c && l1c.next;
    l2c = l2c && l2c.next;
  }

  if (carry) {
    current.next = new ListNode(carry);
  }

  return result.next;
};

console.log(
  addTwoNumbers(buildList([2, 4, 3]), buildList([5, 6, 4])).toString(),
  "7->0->8"
);

console.log(
  addTwoNumbers(buildList([9, 8]), buildList([1])).toString(),
  "0->9"
);

console.log(
  addTwoNumbers(buildList([1, 8]), buildList([0])).toString(),
  "1->8"
);

console.log(addTwoNumbers(buildList([5]), buildList([5])).toString(), "0->1");

function buildList(arr) {
  return arr.reverse().reduce((acc, item) => {
    let node = new ListNode(item);
    node.next = acc;
    return node;
  }, null);
}
