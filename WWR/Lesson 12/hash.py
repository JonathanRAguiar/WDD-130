#- TIME: I SPENDED BY MORE THEN 9 HOURS STUDING AND DOING RESEARCHES FOR THE PROGRAM AT THIS TIME
#- ORGANIZATION: IS A EASY CODE TO READ, THERE IS A HOW TO PLAY INSTRUCTIONS, A BOARD SIMPLY DRAWNED BY THE PRINT, A FUNCTION TO CHOOSE A NUMBER OF THE BOARD(IF THE NUMBER IS CHOOSEN OR DOESNT EXISTS IN THE BOARD, A MESSAGE OF ERROR WILL APEAR),  THE TURN OF EACH PLAYER WILL APPEAR TO GET THE CHOOSEN NUMBER AND THE WINNER IS THE ONE WHO TAKES X, Y OR Z VERTICES.
#- PROGRESS: I'M VERY PROUD OF MYSELF GETING THE X, Y, Z VERTICES, THE MAGIC BOX AND MAKE IT RIDE CLEAN FOR TWO PLAYER, NOW  I'MTRYING TO FIGURE IT OUT HOW TO PLAY AGAINST THE CPU
#- DESCRIPTION: IT IS A HASH GAME FOR TWO PLAYERS, THE FIRST PLAYER IS THE X AND THE SECOND THE O IN A BORD BETWEEN 1 TO 9 OF NUMBER TO CHOOSE CORRESPONDING THE SET TO THE BOARD

how_to_play=print("---HOW TO PLAY---")
print("This is a two players game, the first player is X and must choose a number(1,2,3,4,5,6,7,8 or 9)")
print("Only choose numbers determined in the place of the board that's not taken yet, or will be a error message.")
print("For example, let's say you want to play in the center, so you type 5")
print("And then the next player will be O and do the same")
print("This game is not finished yet, annyway... ")
print("Have fun!!! :D")

print(how_to_play)

def hash():
  """The main that all game is here
  BOARD with 9 numbers to take place
  END is false to run the game while true the players puck a number
  MAGIC BOX run the numbers in a range the vertices x, y, z counting to 15"""
  board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
  end = False
  magic_box = [4, 9, 2, 3, 5, 7, 8, 1, 6]

  def p_board():
    """Pompt: Print and shows the board that the game will be, taking the places with numbers to the players."""
    print()
    print('', board[0], "|", board[1], "|", board[2])
    print("---|---|---")
    print('', board[3], "|", board[4], "|", board[5])
    print("---|---|---")
    print('', board[6], "|", board[7], "|", board[8])
    print()

  def pick_number():
    """Prompt: Pick the number that represents a place in the board
    Parameters: 
    Take the place picking a number. The number the player pick will return.
    IF The number is in the range of the board number will be returned
    ELSE Other recognized numbers but out of range will show an error message
    EXCEPT The caracteristc isn't a number, will show an error message."""
    while True:
      number = input()
      try:
        number  = int(number)
        if number in range(1, 10):
          return number
        else:
          print("\nError: Unknow number")
      except ValueError:
        print("\nError: Only numbers are alowed")
        continue
  
  def Turn(player):
    """Prompt: The turn of player to play
    Parameters:  
    IF In the turn the number is a choosen place already with x or o, shows an error message the place is taken
    ELSE Takes the place of choosen free number in the board with X or O."""
    take_place = pick_number() - 1
    if board[take_place] == "X" or board[take_place] == "O":
      print("\nError: This place has been taken.")
      Turn(player)
    else:
      board[take_place] = player
      
  def Check_winner(player):
    """Prompt: Check the vertice range numbers for the winner
    Parameters:
    FOR X, Y, Z Vertices fullfilled with X or O in the MAGIC BOX will return the player that won
    FOR A range IF the 9 moves are taken and no X, Y, Z vertices the game draws. """
    moves = 0

    for x in range(9):
      for y in range(9):
        for z in range(9):
          if x != y and y != z and z != x:
            if board[x] == player and board[y] == player and board[z] == player:
              if magic_box[x] + magic_box[y] + magic_box[z] == 15:
                print("Player", player ,"won!\n")
                return True

    for a in range(9):
      if board[a] == "X" or board[a] == "O":
        moves += 1
      if moves == 9:
        print("Draw!\n")
        return True

  while not end:
    """Prompt: The player still taking numbers to the end of the game and returns X or O
    Parameters:
    Print the board, if end check the winner and the game still on(end==true) breaks and continue the game."""
    p_board()
    end = Check_winner("O")
    if end == True:
      break
    print("Player X, choose a place number")
    Turn("X")
    
    p_board()
    end = Check_winner("X")
    if end == True:
      break
    print("Player O, choose a place number")
    Turn("O")


hash()
