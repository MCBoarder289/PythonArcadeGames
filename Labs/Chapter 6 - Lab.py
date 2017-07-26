
"""

Part 1
Write a Python program that will print the following:

10
11 12
13 14 15
16 17 18 19
20 21 22 23 24
25 26 27 28 29 30
31 32 33 34 35 36 37
38 39 40 41 42 43 44 45
46 47 48 49 50 51 52 53 54

Tips for Part 1

   1.) Generate the output for part one using two for loops, one nested.
   2.) To start, go back to chapter 6 and remember how to create a triangle of asterisks. Recreate that.
   3.) Then create a new variable. Don't use i, j, row, or column, or whatever you already used.
        Set it to your starting value. Print that.

This problem requires a bit of an “a-ha” to get. Make sure to ask around if you have problems.
My students often find it to be one of the harder problems in this course.

"""
x = 10

for i in range(9):
    for j in range(i+1):
        print(x, end=" ")
        x += 1
    print()

"""

Part 2

Create a big box out of n rows of little o's for any desired size n. 
Use an input statement to allow the user to enter the value for n and then print the properly sized box.
E.g. n = 3
oooooo
o    o
oooooo
 
E.g. n = 8
oooooooooooooooo
o              o
o              o
o              o
o              o
o              o
o              o
oooooooooooooooo

Tip: Break this problem into parts. First, draw the first line with the proper number of o's:
oooooo

Then, draw the last line too:
oooooo
oooooo

Then, print an o between them:
oooooo
o
oooooo

Then repeat it:
oooooo
o
o
o
o
oooooo

Then add another one:
oooooo
oo
oo
oo
oo
oooooo

Then add spaces:
oooooo
o    o
o    o
o    o
o    o
oooooo

"""

# Get Input from User
n = input("Enter a number for your box:")
n = int(n)  # remember to convert to int, since it will be a string

for i in range(n*2):  # First we need to print 2*n dots for the top
    print("o", end="")
print()

for i in range(n-2):  # The middle part is hard, but basically need to discount the top and bottom (n-2)
    print("o", end="")
    for j in range((n*2) - 2):  # After printing the side o, need to input in (n*2)-2 spaces before the next side o
        print(" ", end="")
    print("o")  # Need an implied carriage return to put the bottom loop on the bottom
for i in range(n*2):
    print("o", end="")

"""

Part 3

Print the following for any positive integer n. Use an input statement to allow the user to enter the value for n and then print the properly sized box.
E.g. n = 3
 
1 3 5 5 3 1
3 5     5 3
5         5
5         5
3 5     5 3
1 3 5 5 3 1
 
E.g. n = 5
1 3 5 7 9 9 7 5 3 1
3 5 7 9     9 7 5 3
5 7 9         9 7 5
7 9             9 7
9                 9
9                 9
7 9             9 7
5 7 9         9 7 5
3 5 7 9     9 7 5 3
1 3 5 7 9 9 7 5 3 1

Don't worry about handling the spacing for multi-digit numbers. Chapter 20 covers this if you want to look ahead, but it isn't needed.

This part of the lab is difficult. Skip to part 4 if you aren't interested in the challenge. 

"""


# Get Input from User
n = input("Enter a number for your box:")
n = int(n)  # remember to convert to int, since it will be a string

n = 5
# Gets the first upper left triangle
for i in range(1, n+1):
    for j in range((2*i)-1, (2*n), 2):
        print(j, end="")
    print()

n = 5

# Reverses the order of the first triangle
for i in range(1, n+1):
    for j in range((2*n)-1, (2*i)-2, -2):
        print(j, end="")
    print()

n = 5

# Gets the first upper right Triangle
for i in range(1, n+1):
    for k in range(i-1):
        print(" ", end="")
    for j in range((2*n)-1, (2*i)-2, -2):
        print(j, end="")
    print()

"""
#####################
GETS THE FIRST HALF
#####################
"""

# Get Input from User
n = input("Enter a number for your box:")
n = int(n)  # remember to convert to int, since it will be a string

for i in range(1, n+1):
    for j in range((2*i)-1, (2*n), 2):
        print(j, end=" ")
    for k in range((2*i)-2):
        print(" ", end=" ")
    for l in range((2*n)-1, (2*i)-2, -2):
        print(l, end=" ")
    print()
# #############################################

# Working on Bottom Half

# Gets Bottom Right half:
n = 5
for i in range(1, n+1):
    for k in range(((3 * (n - 2)) + (2 * (1 - i))) - 1):
        print(" ", end="")
    for j in range((2*n)-1, ((3*(n-2)) + (2*(1-i)))-1, -2):
        print(j, end=" ")
    print()


# Gets Bottom Left half:
n = 5
for i in range(1, n+1):
    for j in range(((3*(n-2)) + (2*(1-i))), (2*n), 2):
        print(j, end=" ")
    for k in range(((3 * (n - 2)) + (2 * (1 - i))) - 1):
        print(" ", end="")
    print()

"""
#####################
GETS THE SECOND HALF
#####################
"""
n = 5
for i in range(1, n+1):
    for j in range(((3*(n-2)) + (2*(1-i))), (2*n), 2):
        print(j, end=" ")
    for k in range(((3 * (n - 2)) + (2 * (1 - i))) - 1):
        print(" ", end=" ")
    for j in range((2*n)-1, ((3*(n-2)) + (2*(1-i)))-1, -2):
        print(j, end=" ")
    print()


"""
##########################################
COMBINATION OF BOTH HALVES = Final Answer
##########################################
"""

# Works for n = 5... doesn't work for 3 or 9...

# Get Input from User
n = input("Enter a number for your box:")
n = int(n)  # remember to convert to int, since it will be a string

n = 5  # This one works for 3 and 5 only
for i in range(1, n+1):
    for j in range((2*i)-1, (2*n), 2):
        print(j, end=" ")
    for k in range((2*i)-2):
        print(" ", end=" ")
    for l in range((2*n)-1, (2*i)-2, -2):
        print(l, end=" ")
    print()


# n = 10
# i = 6
# print((3*(n-2)) + (2*(1-i))-1)

n = 5  # This one only works for 5
for i in range(1, n+1):
    for x in range(((3*(n-2)) + (2*(1-i))), (2*n), 2):
        print(x, end=" ")
    for y in range(((3 * (n - 2)) + (2 * (1 - i))) - 1):
        print(" ", end=" ")
    # Need another nested loop that creates a floor for the range - going down by 2 related to i can produce low
    # negative numbers. My pattern only works for 5
    for z in range((2*n)-1, ((3*(n-2)) + (2*(1-i)))-1, -2):
        print(z, end=" ")
    print()

"""
Attempt to handle double digits
"""

n = 5
for i in range(1, n+1):
    for j in range((2*i)-1, (2*n), 2):
        print(j, end=" ")
    for k in range((2*i)-2):
        if len(str(k)) >= 2:
            for a in range(len(str(k))):
                print(" ", end="")
            print(" ", end=" ")
        else:
            print(" ", end=" ")
    for l in range((2*n)-1, (2*i)-2, -2):
        print(l, end=" ")
    print()

"""

"""
