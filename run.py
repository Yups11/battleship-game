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
ship_col_1 = random_col(board)

"""
I comment this code because random point on game area can be the same for both players because is random for computer
ship_row_2 = random_row(board)
ship_col_2 = random_col(board)
"""

""" While loop in order to avoid two the same points chosen in game area"""
ship_row_2, ship_col_2 = ship_row_1, ship_col_1

while ship_row_2==ship_row_1:
    ship_row_2 = random_row(board)

while ship_col_2==ship_col_1:
    ship_col_2 = random_col(board)

print("Here we go!")
player_1 = input("What is your name warrior ?: ")
print(player_1, "Get ready, starting!!!\n")