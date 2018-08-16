"""
8/16/2018
Project from Codecademy. The project thus far was basically just following
hand-holding instructions, but I don't like some of what they did and want
to expand the program to include other cool features.
"""

from random import randint
board = []                        #Will hold the board values

# Appends 5 lists of O's, so that when printed in a loop it forms a grid
for x in range(5):
  board.append(["O"] * 5)

# Loop that prints the board as a grid
def print_board(board):
  for row in board:
    print(" ".join(row))

# Functions that enerate a random position for the computer's battleship
def random_row(board):
  return randint(0, len(board) - 1)
def random_col(board):
  return randint(0, len(board[0]) - 1)

# prints the intial message & board position with battleship hidden
print("Welcome to Battleship, the game where you try to sink my Battleship.")
print("")
print_board(board)

# Generating the actual super-secret battleship
ship_row = random_row(board)
ship_col = random_col(board)

# debugging lul
print(ship_row + 1)
print(ship_col + 1)

# Loop that handles the execution of the actual game
for turn in range(4):
  # Getting the user's guess for this turn
  print("Turn #%s" % (turn + 1))
  guess_row = input("Guess Row: ")
  guess_col = input("Guess Col: ")

  # Makes sure user input is an int or float.
  if guess_row.isdigit() == False or guess_col.isdigit() == False:
    guess_row = 10                  # If not, changes value to 10
    guess_col = 10                  #so it doesn't break code
  else:                             # Changes number to string if it's a number
    guess_row = int(guess_row) - 1
    guess_col = int(guess_col) - 1

  # Determining whether the user wins, loses, or tries again
  if guess_row == ship_row and guess_col == ship_col:  # Wins
    print("Congratulations! You sunk my battleship!")
    break
  else:                                                # Doesn't Win
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print("Oops, that's not even in the ocean. Did you enter an integer \
from 1 to 5?")
    elif board[guess_row][guess_col] == "X":
      print("You guessed that one already.")
    else:
      print("You missed my battleship!")
      board[guess_row][guess_col] = "X"
    if turn == 3:                                      # Loses
      print("Game Over")
  print("")
  print_board(board)
