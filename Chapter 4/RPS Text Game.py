
# My First Rock Paper Scissors Text Game #


import random
print("\r\nTime to play \"Rock, Paper, Scissors! Best 2 out of 3 wins!\"\r\n")

# Setting choices equal to each other for the while loop to begin
player_choice = 0
computer_choice = 0

player_score = 0
computer_score = 0

while player_choice == computer_choice:

    try:  # Error Capturing if they enter in words instead of numbers
        print("The Current score is:", "\r\nYou:", player_score, "\r\nComputer:", computer_score, "\r\n")

        player_choice = input("Choose your number wisely.\r\n 1. Rock \n 2. Paper \n 3. Scissors \r\nYour Choice?:")
        player_choice = int(player_choice)

        if player_choice == 1:  # Converting number choices to words
            player_choice = "Rock"
        elif player_choice == 2:
            player_choice = "Paper"
        elif player_choice == 3:
            player_choice = "Scissors"
        else:
            print("That wasn't a valid entry. Please enter a number 1-3.\r\n")
            player_choice = 0
            continue

        computer_choice = random.randrange(3)  # Random Computer Choice
        computer_choice = int(computer_choice)

        if computer_choice == 0:   # Converting numbers to words
            computer_choice = "Paper"
        elif computer_choice == 1:
            computer_choice = "Scissors"
        else:
            computer_choice = "Rock"

        # Victory Logic
        if computer_choice == "Rock" and player_choice == "Paper":
            print("\r\nYOU WIN!!!", player_choice, "beats", computer_choice, "\r\n")
            player_score += 1
            if player_score == 2:
                break
            elif computer_score == 2:
                break
            else:
                player_choice = 0
                computer_choice = 0
                continue

        elif computer_choice == "Paper" and player_choice == "Scissors":
            print("\r\nYOU WIN!!!", player_choice, "beats", computer_choice, "\r\n")
            player_score += 1
            if player_score == 2:
                break
            elif computer_score == 2:
                break
            else:
                player_choice = 0
                computer_choice = 0
                continue

        elif computer_choice == "Scissors" and player_choice == "Rock":
            print("\r\nYOU WIN!!!", player_choice, "beats", computer_choice, "\r\n")
            player_score += 1
            if player_score == 2:
                break
            elif computer_score == 2:
                break
            else:
                player_choice = 0
                computer_choice = 0
                continue

        elif computer_choice == player_choice:
            print("\r\nIt's a Draw... Try Again\r\n")  # Draws will restart the loop because choice 1 == choice 2
            player_choice = 0
            computer_choice = 0
            continue
        else:
            print("\r\nYou lose...", computer_choice, "beats", player_choice, "\r\n")
            computer_score += 1
            if player_score == 2:
                break
            elif computer_score == 2:
                break
            else:
                player_choice = 0
                computer_choice = 0
                continue

    except ValueError:  # ValueError handling - reset while loop condition and restart the loop.
        print("That wasn't a valid entry. Please enter a number.\r\n")
        player_choice = 0
        computer_choice = 0
        continue

if player_score == 2:
    print("YOU ARE THE CHAMPION!!!")
else:
    print("You are the loser...")
