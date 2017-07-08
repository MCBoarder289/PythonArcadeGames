# Temperature Calculator by Michael Chapman


print("\r\nThis Program will calculate Fahrenheit temperatures to Celsius\r\n")

while True:
    try:
        tempF = input("Type in a temperature in Fahrenheit: ")
        tempF = float(tempF)
        break
    except ValueError:
        print("That was not a valid entry. Please enter a number.")
        continue

tempC = (tempF - 32) * (5/9)
tempC = round(tempC, 2)

print("That temperature in Celsius is:", tempC)

