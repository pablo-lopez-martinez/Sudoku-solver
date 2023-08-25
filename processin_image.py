import cv2
import numpy as np 
import pytesseract


def process_canvas_image(image):

    # Preprocess the image (similar to previous example)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (9, 9), 0)
    thresholded = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                    cv2.THRESH_BINARY_INV, 11, 2)
    
    # Define the coordinates of the Sudoku grid cells in the image
    cell_coordinates = []  # List of (x, y) cell coordinates

   
    # Define the dimensions of a single cell (assuming all cells are equal)
    cell_width = thresholded.shape[1] // 9
    cell_height = thresholded.shape[0] // 9
   
    #Populate the cell_coordinates list
    for row in range(9):
        for col in range(9):
            cell_x = col * cell_width
            cell_y = row * cell_height
            cell_coordinates.append((cell_x, cell_y))
    
    #Recognize numbers and populate the Sudoku matrix
    sudoku_matrix = np.zeros((9,9), dtype=int)
    for (x, y) in cell_coordinates:
        cell = thresholded[y:y + cell_height, x:x + cell_width]
    
    # Apply a threshold to enhance contrast
        _, thresholded_cell = cv2.threshold(cell, 128, 255, cv2.THRESH_BINARY)
    
    # Perform OCR on the thresholded cell
        recognized_digit = pytesseract.image_to_string(thresholded_cell, config='--psm 6 digits')

    # Update the corresponding position in the Sudoku matrix
        row = y // cell_height
        col = x // cell_width
        if recognized_digit.isdigit():
            sudoku_matrix[row, col] = int(recognized_digit)
    return sudoku_matrix