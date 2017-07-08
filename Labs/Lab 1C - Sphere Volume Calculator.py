# Sphere Volume Calculator by Michael Chapman

print("\r\nThis Program will calculate the volume of a sphere\r\n")

radius = input("Enter the radius of the sphere: ")
# While loop that breaks with a Value Error. Ensures we enter in only a valid number)
while True:
    try:
        radius = float(radius)
        if radius <= 0:
            radius = input("This number was not greater than 0. Please enter a number greater than zero: ")
        else:
            break
    except ValueError:
        radius = input("That was an invalid entry. Please enter a number: ")  # issue:If number not entered, this breaks
        radius = float(radius)
        if radius <= 0:
            radius = input("This number was not greater than 0. Please enter a number greater than zero: ")

area = (4 * 3.14) * (radius ** 3) / 3
area = round(area, 2)

print("The area of this sphere is:", area)
