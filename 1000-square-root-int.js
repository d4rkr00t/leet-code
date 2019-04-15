function sqrt(num) {
  let root = 1;
  while (Math.pow(root, 2) < num) {
    root += 1;
  }
  return Math.pow(root, 2) === num ? root : root - 1;
}

console.log(11, sqrt(11));
console.log(12, sqrt(12));
console.log(144, sqrt(144));
