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

""" The player is ready """

hit_count = 0

for turn in range(5):
    guess_row = int(input("\nGuess Row: (allowed values: 0-4) "))
    guess_col = int(input("Guess Col: (allowed values: 0-4)"))

    if (guess_row < 0 or guess_row > (rc_number-1)) or (guess_col < 0 or guess_col > (rc_number-1)):
        print("Values must be between 0 and 4!\n")

    elif board[guess_row] [guess_col] == "*":
        print("This point is already taken.\n")

    elif (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
            hit_count = hit_count + 1
            board[guess_row] [guess_col] = "*"
            print("\nCongratulation!")
            if hit_count == 1:
                   print("You hit first battleship!\n")
            elif hit_count == 2:
                print("You hit second battleship!\n")
                print_board(board)
                break
    else:
        if (board[guess_row] [guess_col]) == "X":
            print("You guessed that one already.\n")
        else:
            print("You missed my battleship!\n")
            board[guess_row] [guess_col] = "X"
        print (turn + 1, "turn")
    print_board(board)
if hit_count == 2:
    print("Congratulations", player_1, "You win!!!")
else:
    print("Sorry", player_1, "You Lose.")
print ("Ship 1 is hidden:")
print (ship_row_1)
print (ship_col_1)

print ("Ship 2 is hidden:")
print (ship_row_2)
print (ship_col_2)