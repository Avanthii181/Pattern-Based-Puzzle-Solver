def is_valid(board, row, col, num):
    """
    Check if placing `num` in `board[row][col]` is valid.
    """
    # Check the row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check the 3x3 sub-grid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using backtracking.
    """
    for row in range(9):
        for col in range(9):
            # Find an empty cell
            if board[row][col] == 0:
                # Try all possible numbers (1-9)
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        if solve_sudoku(board):  # Recursive call
                            return True

                        board[row][col] = 0  # Backtrack if needed

                return False  # No number is valid, so backtrack

    return True  # Puzzle is solved


def print_board(board):
    """
    Print the Sudoku board in a readable format.
    """
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-" * 21)
        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end=" ")
            print(board[row][col] if board[row][col] != 0 else ".", end=" ")
        print()


# Example Sudoku board (0 represents empty cells)
sudoku_board = [
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

# Solve and print the solved Sudoku board
print("Original Sudoku board:")
print_board(sudoku_board)

if solve_sudoku(sudoku_board):
    print("\nSolved Sudoku board:")
    print_board(sudoku_board)
else:
    print("\nNo solution exists.")
