// Validate Binary Search Tree
// #url: https://leetcode.com/problems/validate-binary-search-tree/
// #medium

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

//        10
//      /    \
//     5     15
//    / \    / \
//   4   11 6  20

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
let isValidBST = function(root) {
  let stack = [];
  let inorder = -Infinity;
  while (stack.length || root !== null) {
    while (root !== null) {
      stack.push(root);
      root = root.left;
    }

    root = stack.pop();
    if (root.val <= inorder) return false;
    inorder = root.val;
    root = root.right;
  }
  return true;
};

console.log(isValidBST(createBST([2, 1, 3])), true);
console.log(isValidBST(createBST([5, 1, 4, null, null, 3, 6])), false);
console.log(isValidBST(createBST([10, 5, 15, null, null, 6, 20])), false);
console.log(
  isValidBST(createBST([3, 1, 5, 0, 2, 4, 6, null, null, null, 3])),
  false
);

//     3,
//   1,  5,
// 0, 2, 4, 6,
//     3

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
