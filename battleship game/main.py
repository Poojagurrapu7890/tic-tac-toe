import tkinter as tk
import random

class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")

        self.buttons = []  # Initialize button grid once
        self.create_widgets()
        self.initialize_game()

    def initialize_game(self):
        # Reset game variables
        self.opponent_grid = [["~"] * 5 for _ in range(5)]
        self.hits = 0
        self.turns = 10

        # Place opponent ships
        self.place_opponent_ships()

        # Reset grid buttons
        for r in range(5):
            for c in range(5):
                self.buttons[r][c].config(text="~", bg="#87ceeb", state=tk.NORMAL)

        # Reset status label
        self.status_label.config(text="Turns left: 10")

    def place_opponent_ships(self):
        for _ in range(3):  # Place 3 ships randomly
            x, y = random.randint(0, 4), random.randint(0, 4)
            while self.opponent_grid[x][y] == "S":
                x, y = random.randint(0, 4), random.randint(0, 4)
            self.opponent_grid[x][y] = "S"

    def create_widgets(self):
        title_label = tk.Label(self.root, text="Battleship Game", font=("Arial", 20, "bold"),
                               bg="#4682b4", fg="white", pady=10)
        title_label.pack(fill="x")

        # Create the grid of buttons
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

        # Create status and restart buttons
        self.status_label = tk.Label(self.root, text="Turns left: 10", font=("Arial", 14),
                                     bg="#f0f8ff", fg="black")
        self.status_label.pack(pady=10)

        restart_button = tk.Button(self.root, text="Restart Game", font=("Arial", 14, "bold"),
                                    bg="#32cd32", fg="white", command=self.restart_game)
        restart_button.pack(pady=10)

    def guess_position(self, x, y):
        if self.turns <= 0 or self.hits == 3 or self.buttons[x][y]["state"] == tk.DISABLED:
            return

        if self.opponent_grid[x][y] == "S":
            self.buttons[x][y].config(text="X", bg="red", fg="white")
            self.hits += 1
        elif self.buttons[x][y]["text"] == "~":
            self.buttons[x][y].config(text="O", bg="gray", fg="white")

        self.buttons[x][y].config(state=tk.DISABLED)
        self.turns -= 1
        self.update_status()

    def update_status(self):
        if self.hits == 3:
            self.status_label.config(text="You won! All ships sunk!")
            self.reveal_ships()
            self.disable_all_buttons()
        elif self.turns == 0:
            self.status_label.config(text="Game over! Out of turns.")
            self.reveal_ships()
            self.disable_all_buttons()
        else:
            self.status_label.config(text=f"Turns left: {self.turns}")

    def reveal_ships(self):
        for r in range(5):
            for c in range(5):
                if self.opponent_grid[r][c] == "S" and self.buttons[r][c]["text"] == "~":
                    self.buttons[r][c].config(text="S", bg="yellow", fg="black")

    def disable_all_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state=tk.DISABLED)

    def restart_game(self):
        self.initialize_game()

if __name__ == "__main__":
    root = tk.Tk()
    game = BattleshipGame(root)
    root.mainloop()
