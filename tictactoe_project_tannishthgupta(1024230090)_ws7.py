board = [" " for _ in range(9)]

def print_board(b):
    print(f" {b[0]} | {b[1]} | {b[2]} ")
    print("---|---|---")
    print(f" {b[3]} | {b[4]} | {b[5]} ")
    print("---|---|---")
    print(f" {b[6]} | {b[7]} | {b[8]} ")

def get_player_input(player, b):
    while True:
        move = input(f"Player {player}, choose a position (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if move >= 0 and move < 9 and b[move] == " ":
                return move
        print("Invalid move. Try again.")

def check_winner(b, player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in wins:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] == player:
            return True
    return False

def check_tie(b):
    return " " not in b

def play_game():
    current = "X"
    while True:
        print_board(board)
        move = get_player_input(current, board)
        board[move] = current

        if check_winner(board, current):
            print_board(board)
            print(f"Player {current} wins!! 🎉")
            break

        if check_tie(board):
            print_board(board)
            print("It's a tie!! 😐")
            break

        current = "O" if current == "X" else "X"

while True:
    play_game()
    again = input("Play again? (y/n): ")
    if again.lower() != "y":
        print("Thanks for playing!")
        break
