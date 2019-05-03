// Evaluate Expression
// #url: https://www.interviewbit.com/problems/evaluate-expression/
// ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
// ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

function evalRPN(expr) {
  if (!expr.length) return;

  let validOp = ["+", "-", "*", "/"];
  let stack = [];
  let pos = 0;

  while (pos < expr.length) {
    let op = expr[pos];
    if (validOp.indexOf(op) > -1) {
      let a = Number(stack.pop());
      let b = Number(stack.pop());

      switch (op) {
        case "+":
          stack.push(b + a);
          break;
        case "-":
          stack.push(b - a);
          break;
        case "*":
          stack.push(b * a);
          break;
        case "/":
          stack.push(Math.floor(b / a));
          break;
      }
    } else {
      stack.push(Number(op));
    }
    pos++;
  }

  return stack[0];
}

console.log("Expected: 9", "Actual:", evalRPN(["2", "1", "+", "3", "*"]));
console.log("Expected: 6", "Actual:", evalRPN(["4", "13", "5", "/", "+"]));
