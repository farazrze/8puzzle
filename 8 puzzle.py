import tkinter as tk
import random
from tkinter import messagebox

def move_tile(row, col):
    possible_moves = get_possible_moves()
    if (row, col) in possible_moves:
        blank_row, blank_col = find_blank()
        board[blank_row][blank_col] = board[row][col]
        board[row][col] = 0
        update_buttons()
        if board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]:
            messagebox.showinfo("Congratulations", "You solved the puzzle!")

def find_blank():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def get_possible_moves():
    blank_row, blank_col = find_blank()
    possible_moves = []
    
    if blank_row > 0:
        possible_moves.append((blank_row - 1, blank_col))  # Up
    if blank_row < 2:
        possible_moves.append((blank_row + 1, blank_col))  # Down
    if blank_col > 0:
        possible_moves.append((blank_row, blank_col - 1))  # Left
    if blank_col < 2:
        possible_moves.append((blank_row, blank_col + 1))  # Right
    
    return possible_moves

def update_buttons():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=str(board[i][j]))

root = tk.Tk()
root.title("8-Puzzle Game")
root.geometry("380x280")

board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
unique_numbers = random.sample(range(9), 9)
index = 0
for i in range(3):
    for j in range(3):
        board[i][j] = unique_numbers[index]
        index += 1
buttons = []

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(root, text=str(board[i][j]), width=10, height=5,
                           command=lambda i=i, j=j: move_tile(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)



root.mainloop()