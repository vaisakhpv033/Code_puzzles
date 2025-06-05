# 🧠 Count Zeros in a Binary Array (Without Conditionals)

## 📝 Problem Statement

Given an array `arr` that contains only the integers `0` and `2`, count the total number of `0`s present in the array.

### Constraints

- You must **not** use:
  - Conditional statements (`if`, `else`, `?:`, `switch`, etc.)
  - Loops (`for`, `while`, etc.)
- The array will only contain the numbers `0` and `2`.
- The array can be empty.

---

## 💡 Insight / Core Trick

Since the array contains only `0`s and `2`s:

- `0` contributes nothing to the sum.
- `2` contributes `2` to the sum.

Let:

- `N` = total number of elements in the array
- `S` = sum of all elements in the array

Then:

- `S = 2 * count_of_twos`
- `N = count_of_zeros + count_of_twos`

From this we derive:

count_of_zeros = N - (S / 2)


This elegant formula uses **no conditionals, no loops** — just arithmetic and built-in functions.

---

## ✅ Examples

| Input                   | Output |
|------------------------|--------|
| `[2, 0, 2, 0, 0, 2]`   | 3      |
| `[2, 2, 2]`            | 0      |
| `[0, 0, 0]`            | 3      |
| `[]`                   | 0      |

---

## 🚀 Implementation

### Python

```python
def count_zeros(arr):
    return len(arr) - sum(arr) // 2


