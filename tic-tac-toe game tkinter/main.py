from tkinter import *
from tkinter import messagebox
from tic_tac_toe import initializeGame

def startGame():
    p1 = player1.get()
    p2 = player2.get()
    if p1 and p2:
        name_window.destroy()
        initializeGame(p1, p2)
    else:
        messagebox.showerror("Error", "Enter names for both players!")

name_window = Tk()
name_window.title("Player Names")

Label(name_window, text="Player 1:").grid(row=0, column=0, padx=5, pady=5)
player1 = Entry(name_window)
player1.grid(row=0, column=1, padx=5, pady=5)

Label(name_window, text="Player 2:").grid(row=1, column=0, padx=5, pady=5)
player2 = Entry(name_window)
player2.grid(row=1, column=1, padx=5, pady=5)

Button(name_window, text="Start", command=startGame).grid(row=2, column=0, columnspan=2, pady=10)

name_window.mainloop()
