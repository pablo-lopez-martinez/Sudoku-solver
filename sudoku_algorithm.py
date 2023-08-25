import math 


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