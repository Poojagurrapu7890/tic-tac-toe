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
        (button1, button2, button3),
        (button4, button5, button6),
        (button7, button8, button9),
        (button1, button4, button7),
        (button2, button5, button8),
        (button3, button6, button9),
        (button1, button5, button9),
        (button3, button5, button7)
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
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    button4.config(state=DISABLED)
    button5.config(state=DISABLED)
    button6.config(state=DISABLED)
    button7.config(state=DISABLED)
    button8.config(state=DISABLED)
    button9.config(state=DISABLED)

# Function to initialize the Tic Tac Toe game interface
def initializeGame(player1, player2):
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    global bclick, flag

    bclick = True  # True for Player 1 (X), False for Player 2 (O)
    flag = 0  # Counts the number of moves

    # Create game window
    game_window = Tk()
    game_window.title("Tic Tac Toe")

    # Display player names
    Label(game_window, text=f"{player1} (X)", font=("Arial", 15)).grid(row=0, column=0, columnspan=2)
    Label(game_window, text=f"{player2} (O)", font=("Arial", 15)).grid(row=0, column=2, columnspan=2)

    # Create buttons for the Tic Tac Toe grid
    button1 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button1, player1 if bclick else player2, "X" if bclick else "O"))
    button2 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button2, player1 if bclick else player2, "X" if bclick else "O"))
    button3 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button3, player1 if bclick else player2, "X" if bclick else "O"))
    button4 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button4, player1 if bclick else player2, "X" if bclick else "O"))
    button5 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button5, player1 if bclick else player2, "X" if bclick else "O"))
    button6 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button6, player1 if bclick else player2, "X" if bclick else "O"))
    button7 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button7, player1 if bclick else player2, "X" if bclick else "O"))
    button8 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button8, player1 if bclick else player2, "X" if bclick else "O"))
    button9 = Button(game_window, text=" ", font=("Arial", 20), height=3, width=6, command=lambda: onClick(button9, player1 if bclick else player2, "X" if bclick else "O"))

    # Place buttons in a grid
    button1.grid(row=1, column=0)
    button2.grid(row=1, column=1)
    button3.grid(row=1, column=2)
    button4.grid(row=2, column=0)
    button5.grid(row=2, column=1)
    button6.grid(row=2, column=2)
    button7.grid(row=3, column=0)
    button8.grid(row=3, column=1)
    button9.grid(row=3, column=2)

    game_window.mainloop()