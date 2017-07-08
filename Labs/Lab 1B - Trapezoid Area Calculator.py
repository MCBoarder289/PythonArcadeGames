# Trapezoid Area Calculator by Michael Chapman


print("\r\nThis Program will calculate the area of a trapezoid\r\n")

height = input("Enter the height of the trapezoid: ")
# While loop that breaks with a Value Error. Ensures we enter in only a valid number)
while True:
    try:
        height = float(height)
        break
    except ValueError:
        height = input("That was an invalid entry. Please enter a number: ")
        height = float(height)

bottomLength = input("Enter the length of the bottom base: ")
while True:
    try:
        bottomLength = float(bottomLength)
        break
    except ValueError:
        bottomLength = input("That was an invalid entry. Please enter a number: ")
        bottomLength = float(bottomLength)

topLength = input("Enter the length of the top base: ")
while True:
    try:
        topLength = float(topLength)
        break
    except ValueError:
        topLength = input("That was an invalid entry. Please enter a number: ")
        topLength = float(topLength)

area = (1/2) * (bottomLength + topLength) * height
area = round(area, 2)

print("The area is:", area)
