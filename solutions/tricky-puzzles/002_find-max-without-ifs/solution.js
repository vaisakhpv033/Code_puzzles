function findMaxWithoutIfs(a, b) {
  /**
   * Finds the maximum of two numbers using an arithmetic trick.
   * max(a, b) = (a + b + Math.abs(a - b)) / 2
   */
  return (a + b + Math.abs(a - b)) / 2;
}

// Example Usage:
/*
let num1 = 10;
let num2 = 20;
console.log(`The maximum of ${num1} and ${num2} is: ${findMaxWithoutIfs(num1, num2)}`);

let num3 = -5;
let num4 = -1;
console.log(`The maximum of ${num3} and ${num4} is: ${findMaxWithoutIfs(num3, num4)}`);

let num5 = 7;
let num6 = 7;
console.log(`The maximum of ${num5} and ${num6} is: ${findMaxWithoutIfs(num5, num6)}`);
*/
