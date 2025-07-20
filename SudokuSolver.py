def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")
            print(board[i][j] if board[i][j] != 0 else ".", end=" ")
        print()

def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def is_valid(board, num, pos):
    row, col = pos
    for i in range(9):
        if board[row][i] == num and i != col:
            return False
    for i in range(9):
        if board[i][col] == num and i != row:
            return False
    box_x = col // 3
    box_y = row // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False
    return True

def solve(board):
    find = find_empty(board)
    if not find:
        return True
    row, col = find
    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def get_user_board():
    print("Enter your Sudoku board (9 lines, 9 digits each, use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            row = input(f"Row {i+1}: ").strip()
            if len(row) == 9 and all(ch.isdigit() for ch in row):
                board.append([int(ch) for ch in row])
                break
            else:
                print("Invalid input. Please enter exactly 9 digits.")
    return board

sudoku_board = get_user_board()
print("\nYour Input Sudoku Board:\n")
print_board(sudoku_board)

if solve(sudoku_board):
    print("\nSolved Sudoku Board:\n")
    print_board(sudoku_board)
else:
    print("No solution exists for this Sudoku.")
