import copy
import random

from generator import (
    is_valid,
    solve_sudoku,  
    remove_numbers,
    generate_sudoku,
    generate_puzzle,
    DIFFICULTY,
)


def play_game():
    print("All defeat is psychological.")

    choice = input("Choose difficulty (easy, medium, hard): ").strip().lower()

    puzzle, solution = generate_puzzle(choice)

    initial_puzzle = [[puzzle[r][c] != 0 for c in range(9)] for r in range(9)]

    print("\n--- GAME STARTED ---")
    print("Instructions:")
    print("- Enter Row, Column, and Value as numbers 1-9.")
    print("- Enter '0' as the Value to clear a cell you filled.")
    print("- Enter 'q' at any prompt to quit the game.")

    while True:
        print("\n Game Board:")
        generate_sudoku(puzzle)

        if puzzle == solution:
            print("Congratulations! You've solved the Sudoku puzzle!")
            break
        elif not any(0 in row for row in puzzle):
            print("The puzzle is complete, but the solution is incorrect. Keep trying!")

            #get user input

        row_input = input("Enter Row (1-9) or 'q' to quit: ").strip().lower()
        if row_input == 'q':
            break

        col_input = input("Enter Column (1-9) or 'q' to quit: ").strip().lower()
        if col_input == 'q':
            break

        num_input = input("Enter Value (1-9) or '0' to clear or 'q' to quit: ").strip().lower()
        if num_input == 'q':
            break

        if not (row_input.isdigit() and col_input.isdigit() and num_input.isdigit()):
            print("Invalid input. Please enter numbers between 1 and 9.")
            continue

        row, col, num = int(row_input) - 1, int(col_input) - 1, int(num_input)

        if not (0 <= row < 9 and 0 <= col < 9 and 0 <= num <= 9):
            print("Invalid input. Please enter numbers between 1 and 9.")
            continue

        if initial_puzzle[row][col]:
            print("This cell is part of the initial puzzle and cannot be changed.")
            continue

        if num == 0:
            puzzle[row][col] = 0
            print(f"Cleared cell at Row {row + 1}, Column {col + 1}.")

        else:
            puzzle[row][col] = num
            print(f"Placed {num} at Row {row + 1}, Column {col + 1}.")

if __name__ == "__main__":
    play_game()
