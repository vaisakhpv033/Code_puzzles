# Puzzle: Find the Maximum of Two Numbers (Without Conditionals)

## Problem Statement

Given two numbers, `a` and `b`, find the maximum value without using any conditional statements (like `if-else` or ternary operators) or the built-in `max()` function.

## Hint

<details>
<summary>Click to see a hint</summary>
Think about how the absolute difference `abs(a - b)` relates to the two numbers. The sum `a + b` and the difference `a - b` (or `b - a`) are key components. Consider their average.
</details>

## Solution Explained

The maximum of two numbers, `a` and `b`, can be found using a clever arithmetic trick. The formula is:

`max(a, b) = (a + b + abs(a - b)) / 2`

Let's break down why this works:

1.  **`a + b`**: This is the sum of the two numbers.
2.  **`abs(a - b)`**: This is the absolute difference between the two numbers.
    *   If `a` is greater than `b`, `abs(a - b)` is `a - b`.
    *   If `b` is greater than `a`, `abs(a - b)` is `b - a`.
    *   If `a` equals `b`, `abs(a - b)` is `0`.

3.  **Combining them:**
    *   **Case 1: `a > b`**
        The expression becomes `(a + b + (a - b)) / 2`.
        Simplifying: `(a + b + a - b) / 2 = (2a) / 2 = a`.
        This correctly gives `a` as the maximum.

    *   **Case 2: `b > a`**
        The expression becomes `(a + b + (b - a)) / 2`.
        Simplifying: `(a + b + b - a) / 2 = (2b) / 2 = b`.
        This correctly gives `b` as the maximum.

    *   **Case 3: `a = b`**
        The expression becomes `(a + b + 0) / 2`.
        Simplifying: `(a + a + 0) / 2 = (2a) / 2 = a` (or `b`).
        This correctly gives `a` (or `b`) as the maximum.

This method avoids explicit conditional checks by leveraging mathematical properties.

### Implementation Notes:
*   In Python, use `// 2` for integer division if `a` and `b` are integers and an integer result is expected. If floating-point numbers are possible, `/ 2` is fine.
*   In JavaScript, `/ 2` will work for both integers and floating-point numbers.
