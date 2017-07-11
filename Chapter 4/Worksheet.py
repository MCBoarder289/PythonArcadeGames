
# Write a Python program that will use a for loop to print your name 10 times, and then the word ``Done'' at the end.

for i in range(10):
    print("Mike")
print("Done")

# Write a Python program that will use a for loop to print ``Red'' and then ``Gold'' 20 times.
# (Red Gold Red Gold Red Gold... all on separate lines. Don't use \n.)

for i in range(20):
    print("Red")
    print("Gold")

# Write a Python program that will use a for loop to print the even numbers from 2 to 100, inclusive.

for i in range(2, 102, 2):
    print(i)

# Write a Python program that will use a while loop to count from 10 down to, and including, 0.
# Then print the words ``Blast off!'' Remember, use a WHILE loop, don't use a FOR loop.

x = 10

while x >= 0:
    print(x)
    x -= 1

print("Blast off!")

# There are three things wrong with this program. List each. (3 pts)
print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = input("Enter a number: ")
    total = total + i
print("The total is:", x)
# 1.) The input is not actually used in the variable calculation
# 2.) The end result total is not the sum AND the entry is never converted to a number to add
# 3.) The variable and print at the end are not sum, and we could used +=

# Write a program that prints a random integer from 1 to 10 (inclusive).

import random

x = random.randrange(1, 11)
print(x)

# Write a program that prints a random floating point number somewhere between 1 and 10 (inclusive).
# Do not make the mistake of generating a random number from 0 to 10 instead of 1 to 10

import random

x = random.random()*10 + 1
print(x)

# Write a Python program that will: (3 pts)

#  Ask the user for seven numbers
#  Print the total sum of the numbers
#  Print the count of the positive entries, the number entries equal to zero, and the number of negative entries.
#  Use an if, elif, else chain, not just three if statements.

print("\r\nThis is program will tell you facts about seven numbers\r\n")

positive_count = 0
zero_count = 0
negative_count = 0

"""
# This is how it would originally have been written
for i in range(7):
    try:
        number = input("Enter a number: ")
        number = float(number)
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
    except ValueError:
        print("That was not a number. Please enter a valid number.")
        continue
"""
# This is more advanced:

count = 1
while count <= 7:
    try:
        number = input("Enter a number: ")
        number = float(number)
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1
        count += 1
    except ValueError:
        print("That was not a number. Please enter a valid number.")
        continue

print("The count of positive entries is:", positive_count)
print("The count of negative entries is:", negative_count)
print("The count of zero entries is:", zero_count)

# Coin flip tosser: (4 pts)

# Create a program that will print a random 0 or 1.
# Instead of 0 or 1, print heads or tails. Do this using if statements. Don't select from a list, as shown in the chapter.
# Add a loop so that the program does this 50 times.
# Create a running total for the number of heads flipped, and the number of tails.

import random
print("\r\nThis program will flip a coin 50 times and summarize")

heads_count = 0
tails_count = 0

for i in range(50):
    result = random.randrange(2)
    if result == 1:
        coin_flip = "Tails"
        print(coin_flip)
        tails_count += 1
    else:
        coin_flip = "Heads"
        print(coin_flip)
        heads_count += 1

print("The total count of heads flips is:", heads_count)
print("The total count of tails flips is:", tails_count)

# Write a program that plays rock, paper, scissors: (4 pts)

# Create a program that randomly prints 0, 1, or 2.
# Expand the program so it randomly prints rock, paper, or scissors using if statements.
# Don't select from a list, as shown in the chapter.
# Add to the program so it first asks the user their choice.
# (It will be easier if you have them enter 1, 2, or 3.)
# Add conditional statement to figure out who wins.

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
