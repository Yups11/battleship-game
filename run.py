import random

""" Board size 5 """
board = []
rc_number = 5

for i in range(0, rc_number):
    board.append(["0"] * rc_number)

""" Print board """
def print_board(board):
    for row in board:
        print(" ".join(row))

print_board(board)