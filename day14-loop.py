from getpass import getpass as input

def determine_winner(player1, player2):
    if player1 == player2:
        return "draw"
    elif player1 == "R":
        return "player1" if player2 == "S" else "player2"
    elif player1 == "P":
        return "player1" if player2 == "R" else "player2"
    elif player1 == "S":
        return "player1" if player2 == "P" else "player2"
    return "invalid"

print("Epic 🪨  📄 ✂️ Battle Time - Best of 3!")
print("Please enter R, P or S, to make your move")

player1_score = 0
player2_score = 0
rounds_played = 0
rounds_to_win = 2  # First to 2 wins (best of 3)

while player1_score < rounds_to_win and player2_score < rounds_to_win:
    rounds_played += 1
    print(f"\nRound {rounds_played}")
    print(f"Score - Player 1: {player1_score}, Player 2: {player2_score}")
    
    player1 = input("Player 1 > ")
    player2 = input("Player 2 > ")

    if player1 not in ["R", "P", "S"]:
        print("Invalid move Player 1!")
        continue
    if player2 not in ["R", "P", "S"]:
        print("Invalid move Player 2!")
        continue

    result = determine_winner(player1, player2)
    
    if result == "draw":
        if player1 == "R":
            print("Two rocks don't make a right, it's a draw!")
        elif player1 == "P":
            print("Y'all pushing P with no dub, it's a draw!")
        else:  # Scissors
            print("Scissoring during a kids game, tsk tsk draw!")
    elif result == "player1":
        player1_score += 1
        if player1 == "R":
            print("Player 1's rock smashes Player 2's scissors!")
        elif player1 == "P":
            print("Player 1's paper covers Player 2's rock!")
        else:  # Scissors
            print("Player 1's scissors cuts Player 2's paper!")
    else:  # player2 wins
        player2_score += 1
        if player2 == "R":
            print("Player 2's rock smashes Player 1's scissors!")
        elif player2 == "P":
            print("Player 2's paper covers Player 1's rock!")
        else:  # Scissors
            print("Player 2's scissors cuts Player 1's paper!")

print("\nGame Over!")
print(f"Final Score - Player 1: {player1_score}, Player 2: {player2_score}")
if player1_score > player2_score:
    print("Player 1 wins the game!")
else:
    print("Player 2 wins the game!")
