# Sudoku Solver

This Python script contains functions to check the validity of a Sudoku puzzle and to solve it using backtracking.

## Contents

- **sudoku_solver.py**: This file contains the functions to check the validity of a Sudoku puzzle and to solve it using backtracking.

## Usage

To use the Sudoku solver, you can import the `sudoku_solver.py` file into your Python script and call the `is_valid()` and `sudoku_solver()` functions as needed.

Example usage:

```python
from sudoku_solver import is_valid, sudoku_solver

# Define your Sudoku puzzle as a list of lists
sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Check if the Sudoku puzzle is valid
valid = is_valid(sudoku, 0, 2, 4)
print("Is the Sudoku valid?", valid)

# Solve the Sudoku puzzle
sudoku_solver(sudoku)
print("Solved Sudoku:")
for row in sudoku:
    print(row)
