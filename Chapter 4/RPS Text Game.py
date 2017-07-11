
# My First Rock Paper Scissors Text Game #


import random
print("\r\nTime to play \"Rock, Paper, Scissors\"\r\n")

# Setting choices equal to each other for the while loop to begin
player_choice = 0
computer_choice = 0

while player_choice == computer_choice:

    try:  # Error Capturing if they enter in words instead of numbers
        player_choice = input("Choose your number wisely.\r\n 1. Rock \r 2. Paper \r 3. Scissors \r\n")
        player_choice = int(player_choice)

        if player_choice == 1:  # Converting number choices to words
            player_choice = "Rock"
        elif player_choice == 2:
            player_choice = "Paper"
        else:
            player_choice = "Scissors"

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
        elif computer_choice == "Paper" and player_choice == "Scissors":
            print("\r\nYOU WIN!!!", player_choice, "beats", computer_choice, "\r\n")
        elif computer_choice == "Scissors" and player_choice == "Rock":
            print("\r\nYOU WIN!!!", player_choice, "beats", computer_choice, "\r\n")
        elif computer_choice == player_choice:
            print("\r\nIt's a Draw... Try Again\r\n")  # Draws will restart the loop because the choice 1 == choice 2
        else:
            print("\r\nYou lose...", computer_choice, "beats", player_choice, "\r\n")

    except ValueError:  # ValueError handling - reset while loop condition and restart the loop.
        print("That wasn't a valid entry. Please enter a number.")
        player_choice = 0
        computer_choice = 0
        continue
