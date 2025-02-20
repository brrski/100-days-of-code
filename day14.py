from getpass import getpass as input

print("Epic 🪨  📄 ✂️ Battle Time")
print("Please enter R, P or S, to make your move")
player1 = input("Player 1 > ")
player2 = input("Player 2 > ")


if player1 == "R" :
  if player2 == "R" :
    print("Two rocks don't make a right, it's a draw!")
  elif player2 == "P" :
    print("Player 2's paper covers Player 1's rock!")
  elif player2 == "S" :
    print("Player 1's rock smashes Player 2's scissors!")
  else :
    print("Invalid move Player 2!")

elif player1 == "P" :
  if player2 == "P" :
    print("Y'all pushing P with no dub, it's a draw!")
  elif player2 == "R" :
    print("Player 1's paper covers Player 2's rock!")
  elif player2 == "S" :
    print( "Player 2's scissors cuts Player 1's paper!")
  else :
    print("Invalid move Player 2!")

elif player1 == "S" :
  if player2 == "S" :
    print("Scissoring during a kids game, tsk tsk draw!")
  elif player2 == "R" :
    print("Player 2's rock smashes Player 1's scissors!")
  elif player2 == "P" :
    print("Player 1's scissors cuts Player 2's paper!")
  else :
    print("Invalid move Player 2!")
else:
  print("Invalid move Player 1!")
  
  
