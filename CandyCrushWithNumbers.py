import random

ROWS, COLS = 10, 10
COLORS = [1, 2, 3, 4, 5]

def create_board():
    while True:
        board = [[random.choice(COLORS) for _ in range(COLS)] for _ in range(ROWS)]
        if not has_5_or_more(board):
            return board

def has_5_or_more(board):
    for r in range(ROWS):
        count = 1
        for c in range(1, COLS):
            if board[r][c] == board[r][c-1]:
                count += 1
                if count >= 5:
                    return True
            else:
                count = 1

    for c in range(COLS):
        count = 1
        for r in range(1, ROWS):
            if board[r][c] == board[r-1][c]:
                count += 1
                if count >= 5:
                    return True
            else:
                count = 1
    return False

def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))
    print()

def find_matches(board):
    to_crush = [[False]*COLS for _ in range(ROWS)]

   
    for r in range(ROWS):
        count = 1
        for c in range(1, COLS):
            if board[r][c] == board[r][c-1] != 0:
                count += 1
            else:
                if count >= 3:
                    for k in range(c-count, c):
                        to_crush[r][k] = True
                count = 1
        if count >= 3:
            for k in range(COLS - count, COLS):
                to_crush[r][k] = True


    for c in range(COLS):
        count = 1
        for r in range(1, ROWS):
            if board[r][c] == board[r-1][c] != 0:
                count += 1
            else:
                if count >= 3:
                    for k in range(r-count, r):
                        to_crush[k][c] = True
                count = 1
        if count >= 3:
            for k in range(ROWS - count, ROWS):
                to_crush[k][c] = True

    return to_crush

def crush_and_drop(board, to_crush):
    crushed_any = False
    
    for r in range(ROWS):
        for c in range(COLS):
            if to_crush[r][c]:
                board[r][c] = 0
                crushed_any = True

    for c in range(COLS):
        pointer = ROWS - 1
        for r in range(ROWS -1, -1, -1):
            if board[r][c] != 0:
                board[pointer][c] = board[r][c]
                if pointer != r:
                    board[r][c] = 0
                pointer -= 1
       
        for r in range(pointer, -1, -1):
            board[r][c] = random.choice(COLORS)

    return crushed_any

def candy_crush():
    board = create_board()
    print("Initial Board:")
    print_board(board)

    while True:
        to_crush = find_matches(board)
        if not any(any(row) for row in to_crush):
            print("No more matches, game over.")
            break
        changed = crush_and_drop(board, to_crush)
        print("Board after crushing and dropping:")
        print_board(board)
        if not changed:
            print("No more moves, game over.")
            break

if __name__ == "__main__":
    candy_crush()
