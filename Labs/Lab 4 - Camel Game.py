#  Michael Chapman "Camel Game" - in the style of FTL

import random

print("\r\nWelcome to Space Escape!\r\n")
print("You have stolen the enemy's secret plans and must return to your home planet.")
print("The enemy's fleet will kill you to get the plans and are chasing you through space!")
print("You must reach the safety of your home planet to defeat the enemy once and for all.\r\n")

done = False

choices = ["A", "B", "C", "D", "E", "Q"]

while not done:
    print("A. Travel normal speed")
    print("B. Travel with hyper-speed boost")
    print("C. Rest your crew")
    print("D. Refuel your ship")
    print("E. Perform Status Check")
    print("Q. Quit\r\n")

    user_choice = input("Your command?: ")
    try:
        user_choice = user_choice.upper()
        pass
    except AttributeError:
        print("Please enter in a proper letter.\r\n")
        continue
    if user_choice not in choices:
        print("Please enter in a proper letter from the options.\r\n")
        continue
    if user_choice.upper() == "Q":
        done = True




