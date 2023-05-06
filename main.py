from constraint import *

# Define the Sudoku matrix
sudoku = [[0, 0, 5, 0, 0, 2, 0, 0, 0],
          [0, 3, 0, 0, 9, 0, 0, 1, 0],
          [4, 0, 6, 0, 0, 0, 0, 8, 0],
          [0, 0, 0, 0, 0, 4, 0, 0, 9],
          [0, 0, 0, 5, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 3, 0, 2, 0],
          [0, 0, 0, 0, 6, 0, 0, 0, 7],
          [0, 0, 0, 2, 0, 0, 5, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Create a problem instance
problem = Problem()

# Define the variables and domains for the Sudoku matrix
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            problem.addVariable((i,j), range(1,10))

# Define the constraints for the rows, columns, and sub-grids
for i in range(9):
    row = [(i,j) for j in range(9)]
    problem.addConstraint(AllDifferentConstraint(), row)

for j in range(9):
    col = [(i,j) for i in range(9)]
    problem.addConstraint(AllDifferentConstraint(), col)

for k in range(3):
    for l in range(3):
        box = [(i,j) for i in range(3*k, 3*(k+1)) for j in range(3*l, 3*(l+1))]
        problem.addConstraint(AllDifferentConstraint(), box)

# Solve the Sudoku puzzle using the min_conflicts algorithm
solutions = problem.getSolutions()
if solutions:
    solved_sudoku = [[0 for j in range(9)] for i in range(9)]
    for key, val in solutions[0].items():
        solved_sudoku[key[0]][key[1]] = val
    print("Solved Sudoku:")
    for row in solved_sudoku:
        print(row)
else:
    print("No solution found")
