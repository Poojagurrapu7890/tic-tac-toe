import tkinter as tk
from tkinter import messagebox

class BattleshipGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Battleship")
        self.board_size = 5
        self.ships = 3
        self.turns = 8
        self.current_player = 1
        self.boards = {1: [[0]*self.board_size for _ in range(self.board_size)],
                       2: [[0]*self.board_size for _ in range(self.board_size)]}
        self.create_welcome_screen()

    def create_welcome_screen(self):
        tk.Label(self.window, text="Welcome to Battleship!", font=("Arial", 18)).pack(pady=10)
        tk.Button(self.window, text="Start Game", command=self.start_game).pack(pady=10)

    def start_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.place_ships()

    def place_ships(self):
        tk.Label(self.window, text=f"Player {self.current_player}: Place {self.ships} ships").pack()
        self.draw_board(self.place_ship)
        self.add_restart_button()

    def place_ship(self, x, y):
        if self.boards[self.current_player][x][y] == 0:
            self.boards[self.current_player][x][y] = 1
            self.buttons[x][y].config(bg="green")
            self.ships -= 1
        if self.ships == 0:
            self.switch_turn_or_start()

    def switch_turn_or_start(self):
        if self.current_player == 1:
            self.current_player = 2
            self.ships = 3
            self.start_game()
        else:
            self.attack_phase()

    def attack_phase(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        tk.Label(self.window, text=f"Player {self.current_player}: Attack! Turns left: {self.turns}").pack()
        self.draw_board(self.attack)
        self.add_restart_button()

    def attack(self, x, y):
        opponent = 2 if self.current_player == 1 else 1
        if self.boards[opponent][x][y] == 1:
            self.buttons[x][y].config(bg="red")
            messagebox.showinfo("Hit!", "You hit a ship!")
        else:
            self.buttons[x][y].config(bg="gray")
            messagebox.showinfo("Miss!", "You missed.")
        self.turns -= 1
        if self.turns == 0:
            self.end_game()
        else:
            self.switch_turn()

    def switch_turn(self):
        self.current_player = 2 if self.current_player == 1 else 1
        self.attack_phase()

    def end_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        tk.Label(self.window, text="Game Over!", font=("Arial", 18)).pack(pady=10)
        player1_ships = sum(row.count(1) for row in self.boards[1])
        player2_ships = sum(row.count(1) for row in self.boards[2])
        winner = "Player 1" if player1_ships > player2_ships else "Player 2"
        tk.Label(self.window, text=f"Winner: {winner}").pack(pady=10)
        self.add_restart_button()

    def draw_board(self, command):
        self.buttons = []
        for i in range(self.board_size):
            row_buttons = []
            row_frame = tk.Frame(self.window)
            row_frame.pack()
            for j in range(self.board_size):
                btn = tk.Button(row_frame, text=" ", width=4, height=2,
                                command=lambda x=i, y=j: command(x, y))
                btn.pack(side="left")
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def add_restart_button(self):
        tk.Button(self.window, text="Restart Game", command=self.restart_game).pack(pady=10)

    def restart_game(self):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.__init__()
        self.run()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
