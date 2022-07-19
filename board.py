board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

current_player = "Player 1"

chars = {"Player 1": "X", "Player 2": "O"}

def print_board():
    print("The board:")
    for row in board:
        print(row)
    print()

def prompt_player(player):
    # Prompt the player
    print(player, "choose a cell. Your symbol is", chars[player])
    row = input("Enter the row number (0-2): ")
    column = input("Enter the column number (0-2): ")
    print()

    return (row, column)

def check_cell(row, col):
    isValid = False
    error = ""

    if row.isnumeric() and col.isnumeric():
        row = int(row)
        col = int(col)
        if 0 <= row <= 2 and 0<= col <= 2:
            if board[row][col] == "-":
                isValid = True
            else:
                error = f'The ({row}, {col}) cell is already selected!'
        else:
            error = "The row and column number should be either 0, 1, or 2!"
    else:
        error = "The row and column should be a number!"

    return (row, col, isValid, error)

def choose_cell(player):
    row, col = prompt_player(player)

    # Validate the cell
    row, col, isValid, error = check_cell(row, col)
    while not isValid:
        print_board()

        print(error)
        row, col = prompt_player(player)
        row, col, isValid, error = check_cell(row, col)

    board[row][col] = chars[player]


def check_winner():
    finished = False

    for i in range(3):
        # Check rows
        if (board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][2] != "-"):
            finished = True

        # Check columns
        if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[2][i] != "-"):
            finished = True

    # Check diagonals
    if (board[0][0] == board[1][1] and board[1][1] == board[2][2]) or (board[0][2] == board[1][1] and board[1][1] ==  board[2][0]):
        finished = board[1][1] != "-"
    return finished

def display_winner(winner):
    print(winner, "won the game!")

def check_draw():
    isDraw = True

    for i in range(3):
        if "-" in board[i]:
            isDraw = False

    return isDraw


while True:
    # Display the board
    print_board()

    # Let the player choose a cell
    choose_cell(current_player)

    # Check for winner
    if check_winner():
        print_board()
        display_winner(current_player)
        break
    else:
        # Check draw
        if check_draw():
            print_board()
            print("No one won, it is a draw!")
            break
        else:
            # Change the player
            if current_player == "Player 1":
                current_player = "Player 2"
            else:
                current_player = "Player 1"