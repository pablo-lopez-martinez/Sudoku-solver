import math 

#Starting with a sudoku of 4 digits 


sudoku_small = [[2, 0, 3, 0],
                [0, 3, 0, 2],
                [3, 0, 4, 0],
                [1, 4, 0, 0]]

sudoku_solved = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
]

sudoku_to_solve = [
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

sudoku_wrong_solved = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 5, 6, 1, 7, 9]  # Hay dos 5 en la misma subcuadrícula
]

#Function to check if the sudoku is valid
 
def is_valid(sudoku,row,column,digit):
    tmp_sudoku = sudoku.copy()
    tmp_sudoku[row][column] = digit
    len_sudoku = len(tmp_sudoku)
    #Check rows
    for row in tmp_sudoku:
        checked = set()
        for digit in row:
            if digit!=0:
                if digit in checked:
                    return False
                checked.add(digit)

    #Check columns 
    for column in range(len_sudoku):
        checked = set()
        for row in range(len_sudoku):
            if tmp_sudoku[row][column] !=0:
                if tmp_sudoku[row][column] in checked:
                    return False
                checked.add(tmp_sudoku[row][column])

    #Check squares
    len_square = int(math.sqrt(len_sudoku))
    for row in range(0,len_sudoku,len_square):
        for column in range(0,len_sudoku,len_square):
            checked = set()
            for h in range(0,len_square):
                for k in range(0,len_square):
                    if tmp_sudoku[row+h][column+k]!=0:    
                        if tmp_sudoku[row+h][column+k] in checked:
                            return False 
                        checked.add(tmp_sudoku[row+h][column+k])
    return True

def sudoku_solver(sudoku):
    for row in range(len(sudoku)):
        for column in range(len(sudoku)):
            if sudoku[row][column]==0:
                for digit in range(1,10):
                    if is_valid(sudoku,row,column,digit):
                        sudoku[row][column] = digit
                        if sudoku_solver(sudoku):
                            return True
                    sudoku[row][column]=0
                return False
    return True






def print_matrix(matrix):
    for row in matrix:
        for digit in row:
            print(digit, end = " ")
        print()


sudoku_solver(sudoku_to_solve)
print_matrix(sudoku_to_solve)