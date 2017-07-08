# Trapezoid Area Calculator by Michael Chapman


print("\r\nThis Program will calculate the area of a trapezoid\r\n")

# Get the height input
while True:
    try:
        height = input("Enter the height of the trapezoid: ")
        height = float(height)
        if height <= 0:
            print("This number was not greater than 0. Please enter a number greater than zero\r\n")
            continue
    except ValueError:
        print("That was an invalid entry. Please enter a number\r\n")
        continue

    else:
        break

# Get the bottomLength input
while True:
    try:
        bottomLength = input("Enter the length of the bottom base: ")
        bottomLength = float(bottomLength)
        if bottomLength <= 0:
            print("This number was not greater than 0. Please enter a number greater than zero\r\n")
            continue
    except ValueError:
        print("That was an invalid entry. Please enter a number\r\n")
        continue

    else:
        break

# Get the topLength input
while True:
    try:
        topLength = input("Enter the length of the top of the trapezoid: ")
        topLength = float(topLength)
        if topLength <= 0:
            print("This number was not greater than 0. Please enter a number greater than zero\r\n")
            continue
    except ValueError:
        print("That was an invalid entry. Please enter a number\r\n")
        continue

    else:
        break

area = (1/2) * (bottomLength + topLength) * height
area = round(area, 2)

print("The area is:", area)
