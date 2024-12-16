import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.geometry("300x300")
        self.player_turn = "X"
        self.score_x = 0
        self.score_o = 0

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, command=lambda row=i, column=j: self.click(row, column), height=3, width=6)
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)

        self.score_label = tk.Label(self.window, text="X: 0 - O: 0", font=('Helvetica', 12))
        self.score_label.grid(row=3, column=0, columnspan=3)

        self.new_game_button = tk.Button(self.window, text="New Game", command=self.new_game, font=('Helvetica', 12))
        self.new_game_button.grid(row=4, column=0, columnspan=3)

    def click(self, row, column):
        if self.buttons[row][column]['text'] == "":
            self.buttons[row][column]['text'] = self.player_turn
            if self.check_win():
                self.score_label['text'] = f"X: {self.score_x + 1} - O: {self.score_o}" if self.player_turn == "X" else f"X: {self.score_x} - O: {self.score_o + 1}"
                messagebox.showinfo("Game Over", f"Player {self.player_turn} wins!")
                self.new_game()
            self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        for row in self.buttons:
            if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
                return True
        for column in range(3):
            if self.buttons[0][column]['text'] == self.buttons[1][column]['text'] == self.buttons[2][column]['text'] != "":
                return True
        if self.buttons[0][0]['text'] == self.buttons[1][1]['text'] == self.buttons[2][2]['text'] != "":
            return True
        if self.buttons[0][2]['text'] == self.buttons[1][1]['text'] == self.buttons[2][0]['text'] != "":
            return True
        return False

    def new_game(self):
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button['text'] = ""

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()