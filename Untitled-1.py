import tkinter


def set_title(row, column):
    global curr_player, game_over

    # Prevent further moves if game is over or the cell is already filled
    if game_over or board[row][column]["text"] != "":
        return

    # Mark the board with the current player's symbol
    board[row][column]["text"] = curr_player

    # Switch turns between Player X and Player O
    if curr_player == playerO:
        curr_player = playerX
    else:
        curr_player = playerO
    label["text"] = curr_player + " s turn"

    # Check for a winner or a tie after each move
    check_winner()


def check_winner():
    global turns, game_over
    turns += 1

    # Vertical check
    for row in range(3):
        if (board[row][0]["text"] == board[row][1]["text"] == board[row][2]["text"]
                and board[row][0]["text"] != ""):
            label.config(text=board[row][0]["text"] + " is the winner!", foreground=colour_yellow)
            for column in range(3):
                board[row][column].config(foreground=colour_yellow, background=colour_light_grey)
            game_over = True
            return

    # Horizontal check
    for column in range(3):
        if (board[0][column]["text"] == board[1][column]["text"] == board[2][column]["text"]
                and board[0][column]["text"] != ""):
            label.config(text=board[0][column]["text"] + " is the winner!", foreground=colour_yellow)
            for row in range(3):
                board[row][column].config(foreground=colour_yellow, background=colour_light_grey)
            game_over = True
            return

    # Diagonal check
    if (board[0][0]["text"] == board[1][1]["text"] == board[2][2]["text"]
            and board[0][0]["text"] != ""):
        label.config(text=board[0][0]["text"] + " is the winner!", foreground=colour_yellow)
        for i in range(3):
            board[i][i].config(foreground=colour_yellow, background=colour_light_grey)
        game_over = True
        return

    # Anti-diagonal check
    if (board[0][2]["text"] == board[1][1]["text"] == board[2][0]["text"]
            and board[0][2]["text"] != ""):
        label.config(text=board[0][2]["text"] + " is the winner!", foreground=colour_yellow)
        board[0][2].config(foreground=colour_yellow, background=colour_light_grey)
        board[1][1].config(foreground=colour_yellow, background=colour_light_grey)
        board[2][0].config(foreground=colour_yellow, background=colour_light_grey)
        game_over = True
        return

    # Check for a tie (when all 9 turns have been taken)
    if turns == 9:
        game_over = True
        label.config(text="Tie!", foreground=colour_yellow)


def new_game():
    global turns, game_over, curr_player
    turns = 0
    game_over = False
    curr_player = playerX
    label.config(text=curr_player + "'s turn", foreground="white")

    # Reset the board to start a new game
    for row in range(3):
        for column in range(3):
            board[row][column].config(text="", background=colour_grey)


# Game setup variables
playerX = "X"
playerO = "O"
curr_player = playerX
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# Colors
colour_blue = "#4584b6"
colour_yellow = "#ffde57"
colour_grey = "#343434"
colour_light_grey = "#646464"

turns = 0
game_over = False

# Window setup
window = tkinter.Tk()
window.title("Tic Tac Toe")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text=curr_player + " s turn", font=("Consolas", 20), background=colour_grey,
                      foreground="white")
label.grid(row=0, column=0, columnspan=3, sticky="we")

# Board buttons setup
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame, text="", font=("Consolas", 50, "bold"),
                                            background=colour_grey, foreground=colour_blue, width=4, height=1,
                                            command=lambda row=row, column=column: set_title(row, column))
        board[row][column].grid(row=row+1, column=column)

# Restart button
button = tkinter.Button(frame, text="Restart", font=("Consolas", 20), background=colour_grey,
                        foreground="white", command=new_game)
button.grid(row=4, column=0, columnspan=3, sticky="we")
frame.pack()

window.mainloop()
