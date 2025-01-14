import tkinter as tk
from tkinter import messagebox

class BattleshipGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Battleship Game")
        self.current_player = 1
        self.board_size = 5
        self.ship_count = 3
        self.turns = {1: 8, 2: 8}  # Total turns for each player

        self.player_boards = {
            1: [[0] * self.board_size for _ in range(self.board_size)],
            2: [[0] * self.board_size for _ in range(self.board_size)],
        }

        self.is_placing_ships = True
        self.ship_placements = {1: 0, 2: 0}

        self.create_welcome_screen()

    def create_welcome_screen(self):
        self.welcome_frame = tk.Frame(self.window, bg="lightblue")
        self.welcome_frame.pack(fill="both", expand=True)

        tk.Label(
            self.welcome_frame, text="Welcome to Battleship!", font=("Helvetica", 24), bg="lightblue"
        ).pack(pady=20)

        tk.Button(
            self.welcome_frame, text="Start Game", font=("Helvetica", 18), command=self.start_game
        ).pack(pady=20)

    def start_game(self):
        self.welcome_frame.destroy()
        self.reset_game()
        self.create_board()

    def create_board(self):
        self.board_frame = tk.Frame(self.window, bg="white")
        self.board_frame.pack(fill="both", expand=True)

        tk.Label(
            self.board_frame,
            text=f"Player {self.current_player}'s Turn (Turns left: {self.turns[self.current_player]})",
            font=("Helvetica", 18),
        ).pack(pady=10)

        self.buttons = []
        for i in range(self.board_size):
            row_buttons = []
            row_frame = tk.Frame(self.board_frame)
            row_frame.pack()
            for j in range(self.board_size):
                btn = tk.Button(
                    row_frame,
                    text=" ",
                    width=4,
                    height=2,
                    font=("Helvetica", 12),
                    bg="skyblue",
                    command=lambda x=i, y=j: self.cell_click(x, y),
                )
                btn.pack(side="left", padx=2, pady=2)
                row_buttons.append(btn)
            self.buttons.append(row_buttons)

    def cell_click(self, x, y):
        if self.is_placing_ships:
            if self.player_boards[self.current_player][x][y] == 0:
                self.player_boards[self.current_player][x][y] = 1
                self.buttons[x][y].config(bg="green")
                self.ship_placements[self.current_player] += 1

                if self.ship_placements[self.current_player] == self.ship_count:
                    self.next_phase()
        else:
            self.attack_cell(x, y)

    def next_phase(self):
        self.board_frame.destroy()
        if self.current_player == 1:
            self.current_player = 2
            messagebox.showinfo("Switch Turns", f"Player {self.current_player}, it's your turn to place {self.ship_count} ships!")
            self.create_board()
        else:
            self.is_placing_ships = False
            self.current_player = 1
            messagebox.showinfo("Start Attacking", "Player 1, start attacking!")
            self.create_board()

    def attack_cell(self, x, y):
        opponent = 2 if self.current_player == 1 else 1
        if self.player_boards[opponent][x][y] == 1:
            self.buttons[x][y].config(bg="red")
            self.player_boards[opponent][x][y] = -1
            messagebox.showinfo("Hit!", "You hit a ship!")
        else:
            self.buttons[x][y].config(bg="gray")
            messagebox.showinfo("Miss!", "You missed.")

        self.turns[self.current_player] -= 1

        if self.turns[self.current_player] == 0:
            self.end_game()
        else:
            self.switch_turn()

    def end_game(self):
        self.board_frame.destroy()

        result_frame = tk.Frame(self.window, bg="white")
        result_frame.pack(fill="both", expand=True)

        tk.Label(
            result_frame, text="Game Over!", font=("Helvetica", 24), bg="white"
        ).pack(pady=10)

        player1_ships = sum(row.count(1) for row in self.player_boards[1])
        player2_ships = sum(row.count(1) for row in self.player_boards[2])

        if player1_ships < player2_ships:
            winner = "Player 2"
        elif player1_ships > player2_ships:
            winner = "Player 1"
        else:
            winner = "No one, it's a draw!"

        tk.Label(
            result_frame, text=f"Winner: {winner}", font=("Helvetica", 18), bg="white"
        ).pack(pady=10)

        tk.Button(
            result_frame, text="Show Ship Locations", font=("Helvetica", 14), command=self.show_ships
        ).pack(pady=10)

        tk.Button(
            result_frame, text="Restart Game", font=("Helvetica", 14), command=self.restart_game
        ).pack(pady=10)

    def show_ships(self):
        self.board_frame.destroy()

        ship_frame = tk.Frame(self.window, bg="white")
        ship_frame.pack(fill="both", expand=True)

        tk.Label(
            ship_frame, text="Ship Locations", font=("Helvetica", 24), bg="white"
        ).pack(pady=10)

        for player in [1, 2]:
            tk.Label(
                ship_frame, text=f"Player {player} Ships:", font=("Helvetica", 18), bg="white"
            ).pack(pady=5)

            for row in self.player_boards[player]:
                row_text = " ".join("S" if cell == 1 else "X" if cell == -1 else "~" for cell in row)
                tk.Label(
                    ship_frame, text=row_text, font=("Courier", 14), bg="white"
                ).pack()

        tk.Button(
            ship_frame, text="Exit Game", font=("Helvetica", 14), command=self.window.destroy
        ).pack(pady=20)

    def switch_turn(self):
        self.board_frame.destroy()
        self.current_player = 2 if self.current_player == 1 else 1
        self.create_board()

    def restart_game(self):
        self.window.destroy()
        self.__init__()
        self.run()

    def reset_game(self):
        self.current_player = 1
        self.turns = {1: 8, 2: 8}
        self.is_placing_ships = True
        self.ship_placements = {1: 0, 2: 0}
        self.player_boards = {
            1: [[0] * self.board_size for _ in range(self.board_size)],
            2: [[0] * self.board_size for _ in range(self.board_size)],
        }

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = BattleshipGame()
    game.run()
