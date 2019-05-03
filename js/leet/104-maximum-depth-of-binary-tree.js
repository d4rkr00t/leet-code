// Maximum Depth of Binary Tree
// #url: https://leetcode.com/problems/maximum-depth-of-binary-tree/
// #easy

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
let maxDepth = function(root) {
  if (!root) return 0;
  let stack = [root];
  let depth = 0;

  while (stack.length) {
    depth++;
    stack = stack.reduce((acc, node) => {
      if (node.left !== null) {
        acc.push(node.left);
      }
      if (node.right !== null) {
        acc.push(node.right);
      }
      return acc;
    }, []);
  }

  return depth;
};

// Slower recursive solution
// let maxDepth = function(root) {
//   if (!root) return 0;

//   return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
// };

console.log(maxDepth(createBST([2, 1, 3])), 2);
console.log(maxDepth(createBST([5, 1, 4, null, null, 3, 6])), 3);
console.log(maxDepth(createBST([10, 5, 15, null, null, 6, 20])), 3);
console.log(maxDepth(createBST([3, 1, 5, 0, 2, 4, 6, null, null, null, 3])), 4);

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
