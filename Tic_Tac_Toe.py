# Tic-Tac-Toe Game Implementation
# Experiment 10: Two-Player Zero-Sum Board Game State Validation

def print_board(board):
    # Render the 3x3 game board grid
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board):
    # 1. Test rows and columns for three-in-a-row
    for i in range(3):
        # Check horizontal row
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        # Check vertical column
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # 2. Test main and anti-diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False


# ----------- Main Driver Program -----------
# Initialize empty 3x3 grid
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"

# Up to 9 turns allowed
for turn in range(9):
    print(f"\nPlayer {current_player}'s turn:")
    print_board(board)

    row = int(input("Enter row (0-2): "))
    col = int(input("Enter column (0-2): "))

    # Place symbol in unoccupied cell
    if board[row][col] == " ":
        board[row][col] = current_player

        # Test terminal winning condition
        if check_winner(board):
            print_board(board)
            print(f"\nPlayer {current_player} wins!")
            break

        # Alternate turn to opposing player
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell already occupied. Try again.")

else:
    # All 9 cells filled without a winner
    print_board(board)
    print("\nGame Draw!")
