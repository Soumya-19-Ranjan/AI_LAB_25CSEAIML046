# Eight Queen Problem Solver using Backtracking
# Experiment 08: Constraint Satisfaction Search on 8x8 Chessboard

def is_safe(board, row, col):
    n = len(board)

    # 1. Check vertical column in previous rows
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # 2. Check upper-left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == "Q":
            return False
        i -= 1
        j -= 1

    # 3. Check upper-right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == "Q":
            return False
        i -= 1
        j += 1

    return True


def solve_8queens(board, row=0):
    n = len(board)

    # Base case: All 8 queens successfully placed without threat
    if row == n:
        return True

    # Try placing queen in each column of current row
    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"

            # Recursive forward search to place next row
            if solve_8queens(board, row + 1):
                return True

            # Backtrack on failure
            board[row][col] = "."

    return False


# ----------- Main Driver Program -----------
board = [["." for _ in range(8)] for _ in range(8)]

if solve_8queens(board, 0):
    print("Solution for 8-Queens Problem:\n")
    for row in board:
        print(" ".join(row))
else:
    print("No Solution Exists.")
