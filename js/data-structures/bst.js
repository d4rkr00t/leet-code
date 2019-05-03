class BST {
  constructor(comparator = (a, b) => (a > b ? 1 : a === b ? 0 : -1)) {
    this._comp = comparator;
    this._root = null;
    this._nodeCount = 0;
  }

  insert(item) {
    if (!this._root) {
      this._nodeCount++;
      this._root = {
        val: item,
        left: null,
        right: null
      };
      return;
    }

    let cur = this._root;
    while (cur) {
      let comp = this._comp(cur.val, item);

      if (comp === 1) {
        if (!cur.left) {
          this._nodeCount++;
          cur.left = { val: item, left: null, right: null, _p: cur };
          return;
        }
        cur = cur.left;
      } else if (comp === -1) {
        if (!cur.right) {
          this._nodeCount++;
          cur.right = { val: item, left: null, right: null, _p: cur };
          return;
        }
        cur = cur.right;
      } else {
        cur.val = item;
        return;
      }
    }
  }

  getNodeCount() {
    return this._nodeCount;
  }

  printValues() {
    let root = this._root;
    let stack = [];
    let inorder = [];
    while (stack.length || root) {
      while (root) {
        stack.push(root);
        root = root.left;
      }
      root = stack.pop();
      inorder.push(root.val);
      root = root.right;
    }

    return inorder.join(", ");
  }

  find(item) {
    let cur = this._root;
    while (cur) {
      let comp = this._comp(cur.val, item);

      if (comp === 1) {
        cur = cur.left;
      } else if (comp === -1) {
        cur = cur.right;
      } else {
        return cur;
      }
    }

    return false;
  }

  has(item) {
    return this.find(item) ? true : false;
  }

  depth() {
    let depth = 0;
    let stack = [this._root];
    while (stack.length) {
      depth++;
      stack = stack.reduce((acc, node) => {
        if (node.left) {
          acc.push(node.left);
        }
        if (node.right) {
          acc.push(node.right);
        }
        return acc;
      }, []);
    }

    return depth;
  }

  getMin() {
    let root = this._root;
    while (root.left) {
      root = root.left;
    }

    return root.val;
  }

  getMax() {
    let root = this._root;
    while (root.right) {
      root = root.right;
    }

    return root.val;
  }

  delete(item) {
    let node = this.find(item);
    if (!node) return false;

    // leaf
    if (!node.left && !node.right) {
      if (node._p.right === node) {
        node._p.right = null;
      } else if (node._p.left === node) {
        node._p.left = null;
      }
    }

    // 1 child [left]
    if (node.left && !node.right) {
      let pos = node._p.left === node ? "left" : "right";
      node._p[pos] = node.left;
    }

    // 1 child [right]
    if (node.right && !node.left) {
      let pos = node._p.left === node ? "left" : "right";
      node._p[pos] = node.right;
    }

    // 2 children
    if (node.right && node.left) {
      let pos = node._p.left === node ? "left" : "right";
      let inorder = node.right;
      while (inorder.left) {
        inorder = inorder.left;
      }
      node._p[pos] = inorder;
      inorder.left = node.left;
      inorder.right = node.right;
      inorder._p[inorder._p.left === inorder ? "left" : "right"] = null;
      inorder._p = node._p;
    }

    return true;
  }

  toString() {
    let stack = [this._root];
    let res = [stack.map(i => i.val).join(", ")];

    while (stack.length) {
      let newStack = [];
      while (stack.length) {
        let cur = stack.shift();
        if (cur) {
          newStack.push(cur.left);
          newStack.push(cur.right);
        }
      }
      res.push(newStack.map(i => (i ? i.val : "null")).join(", "));
      stack = newStack;
    }

    return res.join("\n");
  }
}

let bst1 = new BST();

bst1.insert(7);
bst1.insert(3);
bst1.insert(15);
bst1.insert(9);
bst1.insert(20);
bst1.insert(10);
bst1.insert(14);
bst1.insert(4);
bst1.insert(5);
bst1.insert(16);
bst1.insert(21);

console.log(bst1.toString());

console.log("Node count:", bst1.getNodeCount());
console.log("Print inorder:", bst1.printValues());
console.log("Depth:", bst1.depth());
console.log("Min:", bst1.getMin());
console.log("Max:", bst1.getMax());

console.log("Has 9:", bst1.has(9));
console.log("Has 999:", bst1.has(999));

console.log("Delete: 21");
bst1.delete(21);
console.log(bst1.toString());

let del = 15;
console.log("Delete: ", del);
bst1.delete(del);
console.log(bst1.toString());

//                          7
//             3,                      15
//       2,          4,          9,         20
//   _,    _,    _,     5,    _,    10,   16,   21
// _, _, _, _, _, _,                   14,
