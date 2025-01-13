import tkinter as tk
import random

class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")

        self.opponent_grid = [["~"] * 5 for _ in range(5)]
        self.buttons = []
        self.hits = 0
        self.turns = 10

        self.place_opponent_ships()
        self.create_widgets()

    def place_opponent_ships(self):
        for _ in range(3):
            x, y = random.randint(0, 4), random.randint(0, 4)
            while self.opponent_grid[x][y] == "S":
                x, y = random.randint(0, 4)
            self.opponent_grid[x][y] = "S"

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Battleship Game", font=("Arial", 20, "bold"),
                               bg="#4682b4", fg="white", pady=10)
        title_label.pack(fill="x")

        grid_frame = tk.Frame(self.root, bg="#f0f8ff")
        grid_frame.pack(pady=20)

        for r in range(5):
            row_buttons = []
            for c in range(5):
                button = tk.Button(grid_frame, text="~", width=4, height=2, font=("Arial", 12, "bold"),
                                   bg="#87ceeb", command=lambda x=r, y=c: self.guess_position(x, y))
                button.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        self.status_label = tk.Label(self.root, text="Turns left: 10", font=("Arial", 14),
                                     bg="#f0f8ff", fg="black")
        self.status_label.pack(pady=10)

    def guess_position(self, x, y):
        if self.turns <= 0 or self.hits == 3:
            return

        if self.opponent_grid[x][y] == "S":
            self.buttons[x][y].config(text="X", bg="red", fg="white")
            self.hits += 1
        elif self.buttons[x][y]["text"] == "~":
            self.buttons[x][y].config(text="O", bg="gray", fg="white")

        self.turns -= 1

root = tk.Tk()
game = BattleshipGame(root)
root.mainloop()
