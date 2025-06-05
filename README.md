# Code Puzzles

Welcome to the Code Puzzles repository! This collection is designed to challenge your problem-solving skills with a variety of puzzles, ranging from algorithmic and data structure challenges to mathematical brain teasers and tricky, constraint-based problems.

## Purpose

The main goal of this repository is to:
- Provide a curated list of interesting coding puzzles.
- Offer solutions in multiple programming languages.
- Encourage learning and exploration of different problem-solving techniques.
- Foster a community of puzzle enthusiasts who can contribute and learn from each other.

## Folder Structure

To maintain consistency and ease of navigation, please adhere to the following folder structure when contributing new puzzles:

```
code-puzzles/
├── README.md  <-- You are here
├── solutions/
│   ├── algorithms/
│   │   └── 001_puzzle_name/
│   │       ├── solution.py
│   │       ├── solution.js
│   │       └── README.md  // Explains the puzzle and solution
│   ├── data-structures/
│   │   └── ...
│   ├── math-logic/
│   │   ├── number-theory/
│   │   │   └── 001_puzzle_name/
│   │   │       ├── solution.py
│   │   │       └── README.md
│   │   └── combinatorics/
│   │       └── ...
│   ├── tricky-puzzles/  <-- For puzzles with clever or non-obvious solutions
│   │   ├── 001_puzzle_name/
│   │   │   ├── solution.py
│   │   │   ├── solution.js
│   │   │   └── README.md
│   │   └── 002_another_tricky_one/
│   │       ├── solution.cpp
│   │       └── README.md
│   └── (other-categories)/
│       └── ...
└── .gitignore
```

**Key Points for Structure:**

*   All solutions reside within the `solutions/` directory.
*   Puzzles are categorized (e.g., `algorithms`, `data-structures`, `math-logic`, `tricky-puzzles`).
*   Each puzzle has its own directory, prefixed with a unique number (e.g., `001_`, `002_`) followed by a descriptive name (e.g., `find_max_without_ifs`).
*   Inside each puzzle's directory:
    *   Solution files should be named descriptively (e.g., `solution.py`, `solution.java`, `solution.cpp`).
    *   **A `README.md` file is mandatory for every puzzle.** This file should clearly explain the problem statement, any constraints, hints (optional), and a step-by-step explanation of the solution.

## Contribution Guidelines

We welcome contributions! To ensure a smooth process, please follow these guidelines:

1.  **Fork the Repository:** Start by forking the main repository to your GitHub account.
2.  **Create a New Branch:** For each new puzzle or set of related changes, create a new branch in your forked repository. Use a descriptive branch name (e.g., `feat/add-puzzle-name` or `fix/improve-readme-puzzle-name`).
    ```bash
    git checkout -b feat/add-new-puzzle
    ```
3.  **Add Your Puzzle:**
    *   Create the necessary directory structure as described above.
    *   Add your solution file(s).
    *   **Crucially, add a `README.md` file within your puzzle's directory.** This README should explain:
        *   The problem statement clearly.
        *   Any hints (you can use `<details>` and `<summary>` tags for collapsible hints).
        *   A detailed explanation of your solution and the logic behind it.
    *   Ensure your code is well-commented and follows good coding practices for the respective language.
4.  **Test Your Solution:** (If applicable) Make sure your solution works correctly.
5.  **Commit Your Changes:** Use clear and concise commit messages.
    ```bash
    git add .
    git commit -m "feat: Add [Puzzle Name] to [Category]"
    ```
6.  **Push to Your Fork:**
    ```bash
    git push origin feat/add-new-puzzle
    ```
7.  **Submit a Pull Request (PR):**
    *   Go to the original repository on GitHub.
    *   You should see a prompt to create a Pull Request from your new branch.
    *   Provide a clear title and description for your PR, summarizing the changes you've made.
    *   If your PR addresses an existing issue, please link it.

**Best Practices for Contributions:**

*   **Clarity is Key:** Ensure your puzzle descriptions and solution explanations are easy to understand.
*   **Multiple Languages Welcome:** If you can provide solutions in multiple languages, that's fantastic!
*   **Originality/Attribution:** If your puzzle is from a specific source or inspired by one, please give appropriate credit in the puzzle's `README.md`.
*   **Respectful Interaction:** Be respectful and constructive in all discussions and code reviews.

Thank you for contributing to Code Puzzles!
