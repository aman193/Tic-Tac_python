# ........... Global Variable..........

# if game is still going on ?
game_is_going = True

# who win or tie ?
winner = None

# whoes turn it is ?
current_player = "X"


# Starting board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

# dislpay board
def dislpay_board():
  print(board[0] + " | " + board[1] + " | " + board[2])
  print(board[3] + " | " + board[4] + " | " + board[5])
  print(board[6] + " | " + board[7] + " | " + board[8])

# Main funtion to play game tic-tac
def play_game():

  dislpay_board()

  while game_is_going:
    handle_turn(current_player)

    check_if_game_over()

    flip_player()

  # The game is over 
  if winner == "X" or winner == "O":
    print(winner + " won.")
  else:
    print("Tie.")  


# handle turn of player
def handle_turn(player):

  print(player + "'s turn.")
  position = input("Choose a position from 1 to 9 >> ")
  board_index = int(position)-1

  valid = False
  while not valid:

  # Mkae sue if input is currect
    while board_index < 0 or board_index >= 9:
      position = input("Invalid Input. Please choose a position from 1-9 >> ")
      board_index = int(position)-1

    # board_index = int(position)-1
    if board[board_index] == "-":
      valid = True
    else:  
      print("You can't overwrite.")
      #reset board_index
      board_index = -1

  board[board_index] = player
  dislpay_board()

# check if game is over
def check_if_game_over():
  check_for_win()
  check_if_tie()


## check if win 
def check_for_win():
  # set global variables
  global winner

  row_winner = check_rows()
  
  column_winner = check_columns()

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
 

def check_rows():
  # set up global variables
  global game_is_going

  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  
  if row_1 or row_2 or row_2:
    game_is_going = False

  if row_1:
    return board[0]
  elif row_2:    
    return board[3]
  elif row_3:
    return board[6]

  return


def check_columns():
  # set up global variables
  global game_is_going

  columns_1 = board[0] == board[3] == board[6] != "-"
  columns_2 = board[1] == board[4] == board[7] != "-"
  columns_3 = board[2] == board[5] == board[8] != "-"
  
  if columns_1 or columns_2 or columns_2:
    game_is_going = False

  if columns_1:
    return board[0]
  elif columns_2:    
    return board[1]
  elif columns_3:
    return board[2]
    
  return

def check_diagonals():
  # set up global variables
  global game_is_going

  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  
  if diagonal_1 or diagonal_2:
    game_is_going = False

  if diagonal_1 or diagonal_2:
    return board[4]
    
  return

# check tie
def check_if_tie():
  
  global game_is_going

  if "-" not in board:
    game_is_going = False
  return


# flip player
def flip_player():
  # global variable set up
  global current_player

  if current_player=="X":
    current_player="O"
  else:
    current_player="X"  
 
  return

# Start Plying Game Call function
play_game()
