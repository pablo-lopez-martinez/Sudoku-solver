#Starting with a sudoku of 4 digits 

matrix = [[4, 0, 0, 1],
          [0, 1, 3, 0],
          [0, 4, 1, 0],
          [1, 0, 0, 3]]

matrix_prueba = [[1, 2, 4, 3],
                 [2, 1, 3, 4],
                 [3, 4, 1, 2],
                 [4, 3, 2, 1]]

#Function to check if the sudoku is valid
 
def is_valid(sudoku):
    #Check rows
    for row in sudoku:
        list = [0,0,0,0]
        for digit in row:
            if list[digit-1]==0:
                list[digit-1] = digit 
            else: return False


    #Check columns 
    for i in range(len(sudoku[0])):
        list = [0,0,0,0]
        for j in range(len(sudoku)):
            if list[sudoku[j][i]-1]==0:
                list[sudoku[j][i]-1] = sudoku[j][i]
            else: return False
    

    #Check squares
    

print(is_valid(matrix_prueba))