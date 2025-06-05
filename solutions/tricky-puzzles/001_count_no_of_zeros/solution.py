def count_zeros(arr):
  """
  Counts the number of zeros in an array containing only 0s and 2s,
  without using explicit conditionals or loops.

  The logic is:
  - Let N be the total number of elements.
  - Let S be the sum of all elements.
  - Since elements are only 0 or 2, S = 2 * count_of_twos.
  - So, count_of_twos = S / 2.
  - And, count_of_zeros = N - count_of_twos.
  - Therefore, count_of_zeros = N - (S / 2).
  """
  if not arr:
    return 0
  return len(arr) - sum(arr) // 2

# Example Usage:
# print(count_zeros([2, 0, 2, 0, 0, 2]))  # Expected: 3
# print(count_zeros([2, 2, 2]))          # Expected: 0
# print(count_zeros([0, 0, 0]))          # Expected: 3
# print(count_zeros([]))                 # Expected: 0
# print(count_zeros([0]))                # Expected: 1
# print(count_zeros([2]))                # Expected: 0
