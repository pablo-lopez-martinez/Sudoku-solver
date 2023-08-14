import math 

#Starting with a sudoku of 4 digits 

sudoku_resuelto = [
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

sudoku_mal_resuelto = [
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
 
def is_valid(sudoku):
    len_sudoku = len(sudoku)
    #Check rows
    for row in sudoku:
        checked = set()
        for digit in row:
            if digit!=0:
                if digit in checked:
                    return False
                checked.add(digit)

    #Check columns 
    for i in range(len(sudoku[0])):
        checked = set()
        for j in range(len_sudoku):
            if sudoku[j][i] !=0:
                if sudoku[i][j] in checked:
                    return False
                checked.add(sudoku[i][j])

    #Check squares
    len_square = int(math.sqrt(len_sudoku))
    for i in range(0,len_sudoku,len_square):
        for j in range(0,len_sudoku,len_square):
            checked = set()
            for h in range(0,len_square):
                for k in range(0,len_square):
                    if sudoku[i+h][j+k]!=0:    
                        if sudoku[i+h][j+k] in checked:
                            return False 
                        checked.add(sudoku[i+h][j+k])


    return True
