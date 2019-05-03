// Convert a binary tree to a doubly linked circular linked list.
// #url: https://www.careercup.com/question?id=5710647581474816

function ListNode(val) {
  this.val = val;
  this.next = null;
  this.prev = null;
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

function btToLinkedList(bt) {
  let tail = null;
  let head = null;
  let stack = [0];
  let root = 0;
  while (stack.length) {
    while (bt[root] !== undefined && bt[root] !== null) {
      stack.push(root);
      root = root * 2 + 1;
    }
    root = stack.pop();
    let newTail = new ListNode(bt[root]);
    if (!head) {
      head = newTail;
    }
    if (tail) {
      newTail.prev = tail;
      tail.next = newTail;
    }
    tail = newTail;
    root += 1;
  }

  tail.next = head;
  head.prev = tail;

  return head;
}

console.log(btToLinkedList([3, 1, 5, 0, 2, 4, 6, null, null, null, 3]));
