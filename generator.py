import random

print("Welcome to the Sudoku Generator!")

#LIST OF EMPTY ROWS

'''
empty_row = [0] * 9

sudoku_grid = [[0] * 9 for _ in range(9)]

print("Generating a Sudoku puzzle:")
for row in sudoku_grid:
    print(row)
    '''

#FUNCTION TO CHECK IF A NUMBER IS VALID IN A GIVEN CELL

def is_valid(sudoku_grid, row, col, num):
    # Check if the number is already in the row
    if num in sudoku_grid[row]:
        return False

    # Check if the number is already in the column
    for r in range(9):
        if sudoku_grid[r][col] == num:
            return False

    # Check if the number is already in the 3x3 block
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if sudoku_grid[r][c] == num:
                return False

    return True

#FUNCTION TO SOLVE THE SUDOKU GRID USING BACKTRACKING

def solve_sudoku(sudoku_grid):
    for row in range(9):
        for col in range(9):
            if sudoku_grid[row][col] == 0:  # Find an empty cell
                
                numbers = list(range(1, 10))
                random.shuffle(numbers)  # Shuffle numbers to generate different solutions

                for num in numbers:  # Try numbers 1-9
                    if is_valid(sudoku_grid, row, col, num):
                        sudoku_grid[row][col] = num  # Place the number

                        if solve_sudoku(sudoku_grid):  # Recursively try to solve
                            return True

                        sudoku_grid[row][col] = 0  # Backtrack if not solvable

                return False  # No valid number found, trigger backtracking

    return True  # Solved successfully


#FUNCTION TO STRIP THE NUMBERS FROM THE SUDOKU BASED ON DIFFICULTY LEVEL CHOICE

def remove_numbers(sudoku_grid, target_level=30):
    cells = [(r, c) for r in range(9) for c in range(9)]
    random.shuffle(cells)  # Shuffle the list of cells

    current_level = 81  # Start with all cells filled

    for row, col in cells:
        if current_level <= target_level:
            break  # Stop if we have reached the target level
        
        #Store original number incase we need it later
        temp = sudoku_grid[row][col]
        sudoku_grid[row][col] = 0  # Remove the number
        current_level -= 1  # Decrease the current level



#GENERATING SUDOKU GRID W/ DIVIDERS

def generate_sudoku(sudoku_grid):
    # 9x9 board w 3x3 block dividers
    for row_index, row in enumerate(sudoku_grid):
        if row_index % 3 == 0 and row_index != 0:
            print("- " * 11)

        row_text = ""
        for col_index, num in enumerate(row):
            if col_index % 3 == 0 and col_index != 0:
                row_text += "| "
            
            if num == 0:
                row_text += ". "
            else:
                row_text += f"{num} "

        print(row_text)


board = [[0] * 9 for _ in range(9)]

board[0][0] = 5

solve_sudoku(board)

remove_numbers(board, target_level=30)  # Remove numbers to create a puzzle with 30 empty cells

generate_sudoku(board)

