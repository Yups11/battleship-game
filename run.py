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

""" Set hide the batleships and battleship is ready """

def random_row(board):
    return random.randrange(0, len(board))

def random_col(board):
    return random.randrange(0, len(board))

ship_row_1 = random_row(board)
ship_row_1 = random_col(board)

ship_row_2 = random_row(board)
ship_row_2 = random_col(board)