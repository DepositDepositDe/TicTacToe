def print_board(board):
    """Prints the Tic Tac Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the player has won."""
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def tic_tac_toe():
    """Main function to run the Tic Tac Toe game."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        row = int(input(f"Player {player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {player}, enter column (0, 1, 2): "))
        if board[row][col] != " ":
            print("This cell is already occupied. Try again.")
            continue
        board[row][col] = player
        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            break
        if all(cell != " " for row in board for cell in row):
            print_board(board)
            print("It's a tie!")
            break
        player = "O" if player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        tic_tac_toe()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    tic_tac_toe()


# need to add reset function
# need to add a way to make sure no inputs beside 0, 1, 2 or r are available