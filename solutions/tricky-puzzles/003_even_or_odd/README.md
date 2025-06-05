# 🧠 Even or Odd (Without Conditionals)

## 📝 Problem Statement

Given an integer `n`, print "even" if `n` is even, and "odd" if `n` is odd.

### Constraints

- You must **not** use conditional statements (`if`, `else`, `?:`, `switch`, etc.).
- Only arithmetic operators are allowed.

---

## 💡 Insight / Core Trick

The core idea is to leverage the behavior of the modulo operator (`%`).
When an integer `n` is divided by `2`:
- If `n` is even, `n % 2` results in `0`.
- If `n` is odd, `n % 2` results in `1`.

We can use these results (`0` or `1`) as indices to access elements in a list or tuple.
Consider the list `results = ["even", "odd"]`:
- If `n` is even, `n % 2` is `0`, so `results[0]` gives "even".
- If `n` is odd, `n % 2` is `1`, so `results[1]` gives "odd".

This approach avoids explicit conditional logic and relies only on arithmetic operations and list indexing.

---

## ✅ Examples

| Input | Output |
|-------|--------|
| 4     | even   |
| 7     | odd    |
| 0     | even   |
| -2    | even   |
| -5    | odd    |

Note: For negative numbers, the behavior of the modulo operator in Python is such that `-5 % 2` is `1`, and `-2 % 2` is `0`, which aligns with the desired "odd" and "even" classification respectively.

---

## 🚀 Implementation

### Python

```python
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
```
