#  Michael Chapman "Camel Game" - in the style of FTL


# Import packages
import random

# Introduction Text
print("\r\nWelcome to Space Escape!\r\n")
print("You have stolen the enemy's secret plans and must return to your home planet.")
print("The enemy's fleet will kill you to get the plans and are chasing you through space!")
print("You must reach the safety of your home planet to defeat the enemy once and for all.\r\n")

# Setting initial variables and loop criteria
done = False

total_ly_traveled = 0
crew_fatigue = 0
ship_fuel = 100
enemy_distance = -80
fuel_cells = 5

# print(str(ship_fuel)+"%") -- A way to print a percentage

choices = ["A", "B", "C", "D", "E", "Q"]

# Main Loop in Game
while not done:
    # Print the Options
    print("A. Travel normal speed")
    print("B. Travel with hyperdrive boost")
    print("C. Rest your crew")
    print("D. Refuel your ship")
    print("E. Perform Status Check")
    print("Q. Quit\r\n")

    # Warning Messages / End Game Scenarios
    if not done and ship_fuel <= 0:
        print("\r\nYou ran out of fuel... your fate is sealed, and the enemy is victorious...\r\n")
        done = True
        break

    if not done and crew_fatigue >= 8:
        print("\r\nYour crew has reached exhaustion and have accidentally navigated you to a black hole.")
        print("Your home world has been destroyed by the enemy...\r\n")
        done = True
        break

    if not done and enemy_distance >= 0:
        print("\r\nThe enemy fleet has reached your position. Your defenses can't hold up against the attack")
        print("Your ship perishes, as does your home world without knowledge of the stolen secret plans...")
        done = True
        break

    if not done and total_ly_traveled >= 200:
        print("\r\nYou have reached your home world, and are safely behind their fortified defenses")
        print("Congratulations, you have accomplished your mission!")
        done = True
        break

    if not done and enemy_distance >= -15:
        print("\---------WARNING: Enemy Fleet is gaining on your position---------")

    if not done and ship_fuel < 20:
        print("---------WARNING: Ship's remaining fuel is below 20%---------")

    elif not done and ship_fuel < 50:
        print("---------Ship's remaining fuel is below 50%---------")

    if not done and crew_fatigue >= 5:
        print("\r\nYour crew is fatigued, and may become prone to navigational mistakes\r\n")

    # Request input
    user_choice = input("Your command?: ")
    try:  # Error Handling
        user_choice = user_choice.upper()
        pass

    except AttributeError:  # Error Handling
        print("Please enter in a proper letter.\r\n")
        continue

    # Choices Outcomes
    if user_choice not in choices:
        print("Please enter in a proper letter from the options.\r\n")
        continue

    elif user_choice.upper() == "Q":
        done = True

    elif user_choice.upper() == "E":
        print("\r\nLight Years Traveled:", total_ly_traveled)
        print("Emergency Fuel Cells:", fuel_cells)
        print("Remaining Fuel:", str(ship_fuel)+"%")
        print("The enemy's fleet is", enemy_distance, "Light Years back.\r\n")

    elif user_choice.upper() == "C":
        crew_fatigue = 0
        enemy_distance += random.randrange(7, 15)
        print("\r\nAlthough difficult to get some sleep, the crew takes a much needed rest.")
        print("They are now ready to take orders and continue the journey.\r\n")

    elif user_choice.upper() == "B":
        ly_traveled = random.randrange(10, 21)
        total_ly_traveled += ly_traveled
        crew_fatigue += 1
        ship_fuel -= random.randrange(15, 21)
        enemy_distance += random.randrange(1, 7)
        print("\r\nWith the extra boost from the hyperdrive, you travelled", ly_traveled, "Light Years.")
        print("The enemy needed to travel slower to relocate your position\r\n")
        salvage_event = random.randrange(1, 21)
        if salvage_event == 1:
            fuel_cells = 5
            print("\r\nYou have come across a derelict ship. Your emergency fuel reserves are replenished,")
            print("and your crew takes a rest.\n")

    elif user_choice.upper() == "A":
        ly_traveled = random.randrange(5, 13)
        total_ly_traveled += ly_traveled
        crew_fatigue += 1
        ship_fuel -= 10
        enemy_distance += random.randrange(7, 15)
        print("\r\nYou make a quick jump, and travelled", ly_traveled, "Light Years.\r\n")
        salvage_event = random.randrange(1, 21)
        if salvage_event == 1:
            fuel_cells = 5
            print("\r\nYou have come across a derelict ship. Your emergency fuel reserves are replenished\r\n")

    elif user_choice.upper() == "D":
        if fuel_cells > 0:
            fuel_cells -= 1
            ship_fuel += 10
        else:
            print("\r\nYou have no more emergency fuel remaining...\r\n")

print("\r\nGame Over. Thank you for playing!")







