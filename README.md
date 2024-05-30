Sudoku Solver

Project Description

This project is a Sudoku solver implemented in Python. The solver uses a backtracking algorithm to find a solution to any given Sudoku puzzle. The algorithm systematically fills in empty cells while adhering to the rules of Sudoku, ensuring that each row, column, and 3x3 sub-grid contains all the digits from 1 to 9 without repetition.

Features

Backtracking Algorithm: Efficiently solves Sudoku puzzles by exploring possible solutions and backtracking when a conflict is found.
Input Board: The initial Sudoku board can be customized.
Validation: Ensures that the board configuration remains valid according to Sudoku rules during the solving process.
Console Output: Prints the initial and solved Sudoku board in a readable format.
How to Use

Clone the Repository:


git clone https://github.com/huzishah02/sudoku-solver.git
cd sudoku-solver
Run the Solver:
The board variable in the script contains the initial Sudoku board. Modify it as needed.


python sudoku_solver.py
Output:
The script prints the initial and solved Sudoku board to the console.

Code Explanation

Solver Function
The solve function is the core of the solver. It uses recursion and backtracking to solve the puzzle.

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0  # Backtrack

    return False


Validation Function
The valid function checks if placing a number on the board violates Sudoku rules.

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


Board Printing Function
The print_board function prints the Sudoku board in a formatted manner.


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + ' ', end="")


Find Empty Cells Function
The find_empty function locates the next empty cell in the board.


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


Example

Initial Sudoku Board
diff
Copy code
7 8 0 | 4 0 0 | 1 2 0 
6 0 0 | 0 7 5 | 0 0 9 
0 0 0 | 6 0 1 | 0 7 8 
- - - - - - - - - - - - - 
0 0 7 | 0 4 0 | 2 6 0 
0 0 1 | 0 5 0 | 9 3 0 
9 0 4 | 0 6 0 | 0 0 5 
- - - - - - - - - - - - - 
0 7 0 | 3 0 0 | 0 1 2 
1 2 0 | 0 0 7 | 4 0 0 
0 4 9 | 2 0 6 | 0 0 7 
Solved Sudoku Board
diff
Copy code
7 8 5 | 4 3 9 | 1 2 6 
6 1 2 | 8 7 5 | 3 4 9 
4 9 3 | 6 2 1 | 5 7 8 
- - - - - - - - - - - - - 
8 5 7 | 9 4 3 | 2 6 1 
2 6 1 | 7 5 8 | 9 3 4 
9 3 4 | 1 6 2 | 7 8 5 
- - - - - - - - - - - - - 
5 7 8 | 3 9 4 | 6 1 2 
1 2 6 | 5 8 7 | 4 9 3 
3 4 9 | 2 1 6 | 8 5 7 


Contact

For any questions or suggestions, feel free to reach out to huzishah02@gmail.com
