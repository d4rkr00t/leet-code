// Binary Search Tree Iterator
// #url: https://leetcode.com/problems/binary-search-tree-iterator/
// #medium

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 */
var BSTIterator = function(root) {
  this.stack = [];

  while (root !== null) {
    this.stack.push(root);
    root = root.left;
  }
};

/**
 * @return the next smallest number
 * @return {number}
 */
BSTIterator.prototype.next = function() {
  let next = this.stack.pop();
  let root = next.right;
  while (root) {
    this.stack.push(root);
    root = root.left;
  }
  return next.val;
};

/**
 * @return whether we have a next smallest number
 * @return {boolean}
 */
BSTIterator.prototype.hasNext = function() {
  return Boolean(this.stack.length);
};

let iter = new BSTIterator(createBST([7, 3, 15, null, null, 9, 20]));
console.log("next", iter.next(), 3);
console.log("next", iter.next(), 7);
console.log("hasNext", iter.hasNext(), true);
console.log("next", iter.next(), 9);
console.log("hasNext", iter.hasNext(), true);
console.log("next", iter.next(), 15);
console.log("hasNext", iter.hasNext(), true);
console.log("next", iter.next(), 20);
console.log("hasNext", iter.hasNext(), false);

/**
 *
 *
 *  UTILS
 *
 *
 */
function createBST(arr) {
  let result = [new TreeNode(arr[0])];

  for (let i = 1; i < arr.length; i++) {
    if (arr[i] === null) continue;
    let pidx = i % 2 === 0 ? (i - 2) / 2 : (i - 1) / 2;
    let p = result[pidx];
    let child = new TreeNode(arr[i]);
    p[i % 2 === 0 ? "right" : "left"] = child;
    result.push(child);
  }

  return result[0];
}
