
'''
6.2 Advanced Looping Problems
1.) Write code that will print ten asterisks (*) like the following:
* * * * * * * * * *

Have this code print using a for loop, and print each asterisk individually,
rather than just printing ten asterisks with one print statement.
This can be done in two lines of code, a for loop and a print statement.
'''

for i in range(10):
    print("*", end= " ")

'''

6.3 Advanced Looping Problems
2.) Write code that will print the following:
* * * * * * * * * *
* * * * *
* * * * * * * * * * * * * * * * * * * *

This is just like the prior problem, but also printing five and twenty stars.
Copy and paste from the prior problem, adjusting the for loop as needed. 
'''

for i in range(35):
    if i == 9:
        print("*")
    if i == 14:
        print("*")
    else:
        print("*", end=" ")

# Actual Answer
for row in range(10):
    print("*",end=" ")
print()
for row in range(5):
    print("*",end=" ")
print()
for row in range(20):
    print("*",end=" ")

'''
6.3 Advanced Looping Problems
3.) Use two for loops, one of them nested inside the other, to print the following 10x10 rectangle:
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

To start, take a look at Problem 1. The code in Problem 1 generates one line of asterisks. 
It needs to be repeated ten times. Work on this problem for at least ten minutes before looking at the answer. 
'''

for i in range(10):
    for i in range(10):
        print("*", end= " ")
    print()

'''
6.3 Advanced Looping Problems
4.) Use two for loops, one of them nested, to print the following 5x10 rectangle:
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *

This is a lot like the prior problem.
Experiment with the ranges on the loops to find exactly what the numbers passed to the range function control. 
'''

for i in range(10):
    for i in range(5):
        print("*", end=" ")
    print()

'''
6.3 Advanced Looping Problems
5.) Use two for loops, one of them nested, to print the following 20x5 rectangle:
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *
* * * * * * * * * * * * * * * * * * * *

Again, like Problem 3 and Problem 4, but with different range values. 
'''

for i in range(5):
    for i in range(20):
        print("*", end=" ")
    print()

'''
6.3 Advanced Looping Problems
6.) Write code that will print the following:
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8 9

Use two nested loops. Print the first line with a loop, and not with:
print("0 1 2 3 4 5 6 7 8 9")

Tip: First, create a loop that prints the first line. Then enclose it in another loop that repeats the line 10 times.
Use either i or j variables for what the program prints. 
This example and the next one helps reinforce what those index variables are doing. 
'''

for i in range(10):
    for j in range(10):
        print(j, end=" ")
    print()

'''
6.3 Advanced Looping Problems
8.) Write code that will print the following:

0
0 1
0 1 2
0 1 2 3
0 1 2 3 4
0 1 2 3 4 5
0 1 2 3 4 5 6
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7 8 9

Tip: This is just problem 6, but the inside loop no longer loops a fixed number of times. 
Don't use range(10), but adjust that range amount. 
'''



