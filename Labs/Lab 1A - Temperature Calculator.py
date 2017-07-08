# Temperature Calculator by Michael Chapman


print("\r\nThis Program will calculate Fahrenheit temperatures to Celsius\r\n")

tempF = input("Type in a temperature in Fahrenheit: ")
tempF = float(tempF)

tempC = (tempF - 32) * (5/9)
tempC = round(tempC, 2)

print("That temperature in Celsius is:", tempC)

