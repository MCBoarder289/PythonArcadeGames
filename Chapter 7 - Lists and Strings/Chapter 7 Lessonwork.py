"""

#############################
# Data Types
#############################

"""

type(3)  # int
type(3.145)  # float
type("Hi there")  # string
type(True)  # boolean

x = 3
type(x)

type((2, 3, 4, 5))  # tuple
type([2, 3, 4, 5])  # list

"""

#############################
# Lists
#############################

"""

# Adding to a List

my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)

# Create an array with 100 zeros.
my_list = [0] * 100


# Running total in list v1 (Using Array Index variable "i")

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop from 0 up to the number of elements
# in the array:
for i in range(len(my_list)):
    # Add element 0, next 1, then 2, etc.
    list_total += my_list[i]

# Print the result
print(list_total)

# Running total in list v1 (Using an iteration of the Array itself, no index variable)

# Copy of the array to sum
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Initial sum should be zero
list_total = 0

# Loop through array, copying each item in the array into
# the variable named item.
for item in my_list:
    # Add each item
    list_total += item

# Print the result
print(list_total)

# Doubling all numbers in a list:
# Copy of the array to modify
my_list = [5, 76, 8, 5, 3, 3, 56, 5, 23]

# Loop from 0 up to the number of elements
# in the array:
for i in range(len(my_list)):
    # Modify the element by doubling it
    my_list[i] = my_list[i] * 2

# Print the result
print(my_list)

"""

#############################
# Working with Strings
#############################

"""


x = "This is a sample string"
# x = "0123456789"

print("x=", x)

# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])

# Accessing from the right side
print("x[-1]=", x[-1])

# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
print("x[6:9]=", x[6:9])

# Adding and Multiplying Strings

a = "Hi"
b = "There"
c = "!"
print(a + b)
print(a + b + c)
print(3 * a)
print(a * 3)
print((a * 2) + (b * 2))

# Getting the length of a string
a = "Hi There"
print(len(a))

b = [3, 4, 5, 6, 76, 4, 3, 3]
print(len(b))

# Because a string is an array, it can be iterated through just like an array
for character in "This is a test.":
    print(character)

"""

Exercise: Starting
with the following code:
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"

n = int(input("Enter a month number: "))

Print the three month abbreviation for the month number that the user enters.
(Calculate the start position in the string, then use the info we just learned to print out the correct substring.)

"""

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

n = int(input("Enter a month number: "))

start = (n*3) - 3
end = start + 3

print(months[start:end])

"""

#######################
Associative Arrays
#######################

"""

# Create an empty associative array
# (Note the curly braces.)
x = {}

# Add some stuff to it
x["fred"] = 2
x["scooby"] = 8
x["wilma"] = 1

# Fetch and print an item
print(x["fred"])


