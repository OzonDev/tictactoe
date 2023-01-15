#Function to print the board
def print_board():
  print("\n")
  print("  "+board[0]+" | "+board[1]+" | "+board[2]+" ")
  print("--------------")
  print("  "+board[3]+" | "+board[4]+" | "+board[5]+" ")
  print("--------------")
  print("  "+board[6]+" | "+board[7]+" | "+board[8]+" \n")

#Function to check if a player has won
def has_won(player):
  if board[0] == board[1] == board[2] == player or \
  board[3] == board[4] == board[5] == player or \
  board[6] == board[7] == board[8] == player or \
  board[0] == board[3] == board[6] == player or \
  board[1] == board[4] == board[7] == player or \
  board[2] == board[5] == board[8] == player or \
  board[0] == board[4] == board[8] == player or \
  board[2] == board[4] == board[6] == player:
    return True
  else:
    return False

#Function to check if the board is full
def is_full():
  if " " in board:
    return False
  else:
    return True

#Initializing the board
board = [" " for x in range(9)]

#Assigning players and their markers
player1 = "X"
player2 = "O"

#Declaring turn variable
turn = player1

#Loop until the game ends
while True:
  #Print the board
  print_board()

  #Get the position of the move
  move = int(input("It's "+turn+"'s turn. Enter the position of the move (1-9): "))
  if move < 1 or move > 9:
    print("Invalid move!")
    continue

  #Check if the move is valid
  if board[move-1] != " ":
    print("That space is already occupied!")
    continue

  #Make the move
  board[move-1] = turn

  #Check if the player has won
  if has_won(turn):
    print_board()
    print("Congrats! "+turn+" has won the game!")
    break

  #Check if the board is full
  if is_full():
    print_board()
    print("It's a tie!")
    break

  #Change the turn
  if turn == player1:
    turn = player2
  else:
    turn = player1