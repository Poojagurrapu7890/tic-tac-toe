import tkinter as tk
import random

class BattleshipGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Battleship Game")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f8ff")  # Light blue background

        self.player_grid = [["~"] * 5 for _ in range(5)]
        self.opponent_grid = [["~"] * 5 for _ in range(5)]
        self.buttons = []  # To store button references
        self.hits = 0
        self.turns = 10

        # Place opponent ships
        self.place_opponent_ships()

        # Create GUI
        self.create_widgets()

    def place_opponent_ships(self):
        for _ in range(3):  # Opponent has 3 ships
            x, y = random.randint(0, 4), random.randint(0, 4)
            while self.opponent_grid[x][y] == "S":  # Avoid overlapping ships
                x, y = random.randint(0, 4), random.randint(0, 4)
            self.opponent_grid[x][y] = "S"

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(
            self.root, text="Battleship Game", font=("Arial", 20, "bold"),
            bg="#4682b4", fg="white", pady=10
        )
        title_label.pack(fill="x")

        # Game Grid
        grid_frame = tk.Frame(self.root, bg="#f0f8ff")
        grid_frame.pack(pady=20)

        for r in range(5):
            row_buttons = []
            for c in range(5):
                button = tk.Button(
                    grid_frame, text="~", width=4, height=2, font=("Arial", 12, "bold"),
                    bg="#87ceeb", fg="black",  # Light blue for water
                    command=lambda x=r, y=c: self.make_guess(x, y)
                )
                button.grid(row=r, column=c, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        # Status Label
        self.status_label = tk.Label(
            self.root, text="Turns left: 10", font=("Arial", 14),
            bg="#f0f8ff", fg="black"
        )
        self.status_label.pack(pady=10)

        # Restart Button
        restart_button = tk.Button(
            self.root, text="Restart Game", font=("Arial", 12),
            bg="#4682b4", fg="white", command=self.restart_game
        )
        restart_button.pack(pady=10)

    def make_guess(self, x, y):
        if self.turns <= 0 or self.hits == 3:
            return

        if self.opponent_grid[x][y] == "S":
            self.buttons[x][y].config(text="X", bg="red", fg="white")  # Red for hit
            self.opponent_grid[x][y] = "~"  # Mark ship as hit
            self.hits += 1
            self.status_label.config(text=f"Hit! {3 - self.hits} ships left.")
        elif self.buttons[x][y]["text"] == "~":
            self.buttons[x][y].config(text="O", bg="gray", fg="white")  # Gray for miss
            self.status_label.config(text=f"Miss! Turns left: {self.turns - 1}.")
        else:
            return  # Cell already guessed

        self.turns -= 1

        # Check for game over
        if self.hits == 3:
            self.status_label.config(text="Congratulations! You win!")
            self.disable_buttons()
        elif self.turns == 0:
            self.status_label.config(text="Game over! You ran out of turns.")
            self.disable_buttons()

    def disable_buttons(self):
        for row in self.buttons:
            for button in row:
                button.config(state="disabled")

    def restart_game(self):
        # Reset game state
        self.player_grid = [["~"] * 5 for _ in range(5)]
        self.opponent_grid = [["~"] * 5 for _ in range(5)]
        self.buttons = []
        self.hits = 0
        self.turns = 10

        # Clear old widgets and reinitialize
        for widget in self.root.winfo_children():
            widget.destroy()
        self.place_opponent_ships()
        self.create_widgets()

# Run the game
root = tk.Tk()
game = BattleshipGame(root)
root.mainloop()
