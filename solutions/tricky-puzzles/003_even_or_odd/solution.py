def check_even_odd(n):
  """
  Checks if a number is even or odd without using conditional statements.

  Args:
    n: An integer.
  """
  results = ["even", "odd"]
  print(results[n % 2])

# Example usage:
# check_even_odd(4)  # Output: even
# check_even_odd(7)  # Output: odd
# check_even_odd(0)  # Output: even
# check_even_odd(-2) # Output: even
# check_even_odd(-5) # Output: odd
