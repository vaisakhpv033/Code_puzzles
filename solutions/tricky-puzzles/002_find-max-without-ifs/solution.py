def find_max_without_ifs(a, b):
  """
  Finds the maximum of two numbers using an arithmetic trick.
  max(a, b) = (a + b + abs(a - b)) / 2
  """
  return (a + b + abs(a - b)) // 2

# Example Usage:
# num1 = 10
# num2 = 20
# print(f"The maximum of {num1} and {num2} is: {find_max_without_ifs(num1, num2)}")

# num3 = -5
# num4 = -1
# print(f"The maximum of {num3} and {num4} is: {find_max_without_ifs(num3, num4)}")

# num5 = 7
# num6 = 7
# print(f"The maximum of {num5} and {num6} is: {find_max_without_ifs(num5, num6)}")
