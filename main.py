#------Global Variavbles------#

# Game Board
board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

# If game is still going
game_still_going = True

# Who win or tie?
winner = None

#whos turn it?
current_player = "O"


# Display Game Board
def display_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])


# Main Function for tictactoe game
def play_game():

  # display board initially
  display_board()

  # While the game is still going
  while game_still_going:

    # handle a single turn for arbitary player
    handle_turn(current_player)

    # check if the game has ended
    check_if_game_over()

    # flip to the other player
    flip_player()

    # the game has ended
    if winner == "X" or winner == "O":
      print(winner + " won.")
    elif winner == None:
      print("Tie.")


# handle a single turn for arbitary player
def handle_turn(player):

  # Which player in time?
  print(player + "'s turn")
  position = input("Choose a position from 1-9: ")

  # 
  valid = False
  while not valid:
    # while 1-9 number are not in position.computer program will kill you.
    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
      position = input("Invalid input. Choose a position from 1-9: ")

    # right positioning
    position = int(position) - 1

    # Don't replace X or O in again and again logic
    if board[position] == "-":
      valid = True
    else:
      print("You can't go there. Go again.")

  # current player positioning in first time
  board[position] = player

  # display_board after positioning
  display_board()


# game Over functionality created for play_game()
def check_if_game_over():
  check_if_win()
  check_if_tie()


# check for winner function for if_game_over()
def check_if_win():

  # set up global variable
  global winner

  # check rows
  row_winner = check_rows()
  # check columns
  column_winner = check_columns()
  # check diagonals
  diagonal_winner = check_diagonals()
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None
  return


# check rows winner function for check_if_win()
def check_rows():
  # Set up global variable
  global game_still_going
  # check if any of the rows have all the same value (and is not empty)
  rows_1 = board[0] == board[1] == board[2] != "-"
  rows_2 = board[3] == board[4] == board[5] != "-"
  rows_3 = board[6] == board[7] == board[8] != "-"
  # if any rows does have a match, flag that there is a win
  if rows_1 or rows_2 or rows_3:
    game_still_going = False

  if rows_1:
    return board[0]
  elif rows_2:
    return board[3]
  elif rows_3:
    return board[6]
  return


# check column winner function for check_if_win()
def check_columns():
  # Set up global variable
  global game_still_going
  # check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[1] == board[2] != "-"
  column_2 = board[4] == board[5] == board[5] != "-"
  column_3 = board[7] == board[8] == board[8] != "-"

  # if any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0]
  elif column_2:
    return board[3]
  elif column_3:
    return board[6]
  return

# check diagonals winner function for check_if_win()
def check_diagonals():
  # Set up global variable
  global game_still_going
  # check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[6] == board[4] == board[2] != "-"

  # if any diagonals does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_still_going = False

  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[6]
  return

# check if_tie. No one is win the game.
def check_if_tie():
  # Global variable we need that
  global game_still_going
  # if "-" in not by win, then i will tie
  if "-" not in board:
    game_still_going = False
  return

# flip function for play_game()
def flip_player():
  # global variable we need that
  global current_player
  # if the current player was the X, then change it to O
  if current_player == "X":
    current_player = "O"
  # if the current player was the O, then change it to X
  elif current_player == "O":
    current_player = "X"

  return

play_game()

# board
# display Board
# play game
# handle turn
# check win
# check rows
# check columns
# check diagonals
# check tie
# check flip