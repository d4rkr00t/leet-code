// Serialize and Deserialize Binary Tree
// #url: https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
// #hard

function TreeNode(val) {
  this.val = val;
  this.left = this.right = null;
}

/**
 * Encodes a tree to a single string.
 *
 * @param {TreeNode} root
 * @return {string}
 */
let serialize = function(root) {
  let rec = (prev, node) => {
    if (!node) {
      prev.push(null);
      return;
    }

    prev.push(node.val);
    rec(prev, node.left);
    rec(prev, node.right);
  };

  let res = [];
  rec(res, root); // [], 1

  return JSON.stringify(res);
};

/**
 * Decodes your encoded data to tree.
 *
 * @param {string} data
 * @return {TreeNode}
 */
let deserialize = function(data) {
  let rec = list => {
    if (list[0] === null || list[0] === undefined) {
      list.shift();
      return null;
    }

    let node = new TreeNode(list[0]);
    list.shift();
    node.left = rec(list);
    node.right = rec(list);
    return node;
  };

  return rec(JSON.parse(data));
};

console.log(
  JSON.stringify(
    deserialize(serialize(deserialize("[1, 2, 3, null, null, 4, 5]"))),
    null,
    2
  )
);

// console.log(
//   JSON.stringify(deserialize("[ -1, 0, null, null, 1, null, null ]"), null, 2)
// );

//  1            | 0
//  2 3          | 1
//  - 8 4 5      | 2
//  9 - - 6 7    | 3

//          1
//      2      6
//   3    4  n  7
// n n  5  n   n n
