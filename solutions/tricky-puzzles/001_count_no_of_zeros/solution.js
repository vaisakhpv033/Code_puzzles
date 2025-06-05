function countZeros(arr) {
  /**
   * Counts the number of zeros in an array containing only 0s and 2s,
   * without using explicit conditionals or loops.
   *
   * The logic is:
   * - Let N be the total number of elements.
   * - Let S be the sum of all elements.
   * - Since elements are only 0 or 2, S = 2 * count_of_twos.
   * - So, count_of_twos = S / 2.
   * - And, count_of_zeros = N - count_of_twos.
   * - Therefore, count_of_zeros = N - (S / 2).
   */
  if (!arr || arr.length === 0) {
    return 0;
  }
  const sum = arr.reduce((acc, val) => acc + val, 0);
  return arr.length - sum / 2;
}

// Example Usage:
/*
console.log(countZeros([2, 0, 2, 0, 0, 2])); // Expected: 3
console.log(countZeros([2, 2, 2]));          // Expected: 0
console.log(countZeros([0, 0, 0]));          // Expected: 3
console.log(countZeros([]));                 // Expected: 0
console.log(countZeros([0]));                // Expected: 1
console.log(countZeros([2]));                // Expected: 0
*/
