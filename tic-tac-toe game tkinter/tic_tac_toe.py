from tkinter import *
from tkinter import messagebox

# Function to handle button clicks
def onClick(button, player, symbol):
    global bclick, flag

    if button["text"] == " ":
        button["text"] = symbol
        bclick = not bclick
        checkForWin(player, symbol)
        flag += 1
    else:
        messagebox.showinfo("Tic Tac Toe", "This button is already clicked!")

# Function to check for win conditions
def checkForWin(player, symbol):
    win_conditions = [
        (buttons[0], buttons[1], buttons[2]),
        (buttons[3], buttons[4], buttons[5]),
        (buttons[6], buttons[7], buttons[8]),
        (buttons[0], buttons[3], buttons[6]),
        (buttons[1], buttons[4], buttons[7]),
        (buttons[2], buttons[5], buttons[8]),
        (buttons[0], buttons[4], buttons[8]),
        (buttons[2], buttons[4], buttons[6])
    ]

    for condition in win_conditions:
        if condition[0]["text"] == symbol and condition[1]["text"] == symbol and condition[2]["text"] == symbol:
            disableAllButtons()
            messagebox.showinfo("Tic Tac Toe", f"{player} wins!")
            return

    if flag == 8:
        messagebox.showinfo("Tic Tac Toe", "It's a tie!")
        disableAllButtons()

# Function to disable all buttons
def disableAllButtons():
    for button in buttons:
        button.config(state=DISABLED)
def initializeGame(player1, player2):
    global buttons, bclick, flag

    bclick = True  # True for Player 1 (X), False for Player 2 (O)
    flag = 0  # Counts the number of moves

    # Create game window
    game_window = Tk()
    game_window.title("Tic Tac Toe")

    # Display player names
    Label(game_window, text=f"{player1} (X)", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    Label(game_window, text=f"{player2} (O)", font=("Arial", 15)).grid(row=0, column=2, columnspan=2)

    # Create list to hold buttons
    buttons = []
    # Create buttons for the Tic Tac Toe grid and store them in the buttons list
    for i in range(9):
        button = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda i=i: onClick(buttons[i], player1 if bclick else player2, "X" if bclick else "O"))
        buttons.append(button)

    # Place buttons in a grid
    for i in range(9):
        row = i // 3 + 1
        col = i % 3
        buttons[i].grid(row=row, column=col)

    game_window.mainloop()
