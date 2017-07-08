# Sphere Volume Calculator by Michael Chapman

print("\r\nThis Program will calculate the volume of a sphere\r\n")

# Needed to wrap the input itself in the while loop. Also needed the input to remain the same, instead of putting
# additional inputs within the response (bring it back to the beginning to try again)

while True:
    try:
        radius = input("Enter the radius of the sphere: ")
        radius = float(radius)
        if radius <= 0:
            print("This number was not greater than 0. Please enter a number greater than zero\r\n")
            continue

    except ValueError:
        print("That was an invalid entry. Please enter a number\r\n")
        continue

    else:
        break

area = (4 * 3.14) * (radius ** 3) / 3
area = round(area, 2)

print("The area of this sphere is:", area)
