// Swap Nodes in Pairs
// #url: https://leetcode.com/problems/swap-nodes-in-pairs/
// #medium

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
let swapPairs = function(head) {
  if (!head || !head.next) return head;
  let newHead = new ListNode();
  newHead.next = head;
  let cur = newHead;
  while (cur.next && cur.next.next) {
    let tmp1 = cur.next;
    let tmp2 = cur.next.next;

    cur.next.next = cur.next.next.next;
    cur.next = tmp2;
    cur.next.next = tmp1;

    cur = tmp1;
  }

  return newHead.next;
};

console.log(JSON.stringify(swapPairs(buildList([1, 2, 3, 4])), null, 2));

/**
 *
 *
 * HELPERS
 *
 *
 */

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

function buildList(arr) {
  return arr.reverse().reduce((acc, item) => {
    let node = new ListNode(item);
    node.next = acc;
    return node;
  }, null);
}
