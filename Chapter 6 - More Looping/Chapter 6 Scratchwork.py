
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
7.) Adjust the prior program to print:
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1
2 2 2 2 2 2 2 2 2 2
3 3 3 3 3 3 3 3 3 3
4 4 4 4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5 5
6 6 6 6 6 6 6 6 6 6
7 7 7 7 7 7 7 7 7 7
8 8 8 8 8 8 8 8 8 8
9 9 9 9 9 9 9 9 9 9
'''

for i in range(10):
    for j in range(10):
        print(i, end=" ")
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

for i in range(10):
    for j in range(i+1):  # Have to do i+1 because the first iteration is 0
        print(j, end=" ")
    print()

'''
6.3 Advanced Looping Problems
9.) Write code that will print the following:

0 1 2 3 4 5 6 7 8 9
  0 1 2 3 4 5 6 7 8
    0 1 2 3 4 5 6 7
      0 1 2 3 4 5 6
        0 1 2 3 4 5
          0 1 2 3 4
            0 1 2 3
              0 1 2
                0 1
                  0

This one is difficult. Tip: Two loops are needed inside the outer loop that controls each row. 
First, a loop prints spaces, then a loop prints the numbers. Loop both these for each row. 

To start with, try writing just one inside loop that prints:

0 1 2 3 4 5 6 7 8 9
0 1 2 3 4 5 6 7 8
0 1 2 3 4 5 6 7
0 1 2 3 4 5 6
0 1 2 3 4 5
0 1 2 3 4
0 1 2 3
0 1 2
0 1
0

Then once that is working, add a loop after the outside loop starts and before the already existing inside loop. 
Use this new loop to print enough spaces to right justify the other loops. 
'''

# Attempt 1 -- cool pattern, but wrong answer
for i in range(10):
    for j in range(10):
        print(" ", end=" ")
        for k in range(10-i):
            print(j, end=" ")
    print()

# Attempt 2 actual answer:
for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for k in range(10-i):
        print(k, end=" ")
    print()

'''
6.3 Advanced Looping Problems
10.) Write code that will print the following (Getting the alignment is hard, at least get the numbers):
1   2   3   4   5   6   7   8   9
2   4   6   8  10  12  14  16  18
3   6   9  12  15  18  21  24  27
4   8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81

Tip: Start by adjusting the code in problem 1 to print:
0  0  0  0  0  0  0  0  0  0
0  1  2  3  4  5  6  7  8  9
0  2  4  6  8  10  12  14  16  18
0  3  6  9  12  15  18  21  24  27
0  4  8  12  16  20  24  28  32  36
0  5  10  15  20  25  30  35  40  45
0  6  12  18  24  30  36  42  48  54
0  7  14  21  28  35  42  49  56  63
0  8  16  24  32  40  48  56  64  72
0  9  18  27  36  45  54  63  72  81

Then adjust the code to print:
1  2  3  4  5  6  7  8  9
2  4  6  8  10  12  14  16  18
3  6  9  12  15  18  21  24  27
4  8  12  16  20  24  28  32  36
5  10  15  20  25  30  35  40  45
6  12  18  24  30  36  42  48  54
7  14  21  28  35  42  49  56  63
8  16  24  32  40  48  56  64  72
9  18  27  36  45  54  63  72  81

Finally, use an if to print spaces if the number being printed is less than 10. 
'''

for i in range(1, 10, 1):
    for j in range(1, 10, 1):
        if i*j < 10:  # If number is less than 10, need to print an extra space to format the numbers properly
            print(" ", end="")

        print(i*j, end=" ")
    print()

'''
6.3 Advanced Looping Problems
11.) Write code that will print the following:

                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

Tip: first write code to print:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9

Then write code to print:

1
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1
1 2 3 4 5 6 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
  

Then finish by adding spaces to print the final answer.  
'''

# My Answer
for i in range(1, 10):
    for l in range(10-i):
        print(" ", end=" ")
    for j in range(i):
        print(j+1, end=" ")
    for k in range(j):
        print(j-k, end=" ")
    print()

# Actual Answer
for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

'''
6.3 Advanced Looping Problems
12.) Write code that will print the following:

                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8
      1 2 3 4 5 6 7
        1 2 3 4 5 6
          1 2 3 4 5
            1 2 3 4
              1 2 3
                1 2
                  1

This can be done by combining problems 11 and 9. 
'''

# My Answer
for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    for j in range(i):
        print(" ", end=" ")
    for k in range(10-i):
        print(k+1, end=" ")
    print()

# Actual Answer -- Like this one a lot better, mine has some flaws...
for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i + 2):  # After starting with copy/paste to get first triangle, need to start with 2 spaces
        print(" ", end=" ")
    # Count down
    for j in range(1, 9 - i):  # Counting up from 1-8, and then 1-7 etc. -> 1
        print(j, end=" ")
    # Next row
    print()

'''
6.3 Advanced Looping Problems
13.) Write code that will print the following:

                  1
                1 2 1
              1 2 3 2 1
            1 2 3 4 3 2 1
          1 2 3 4 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
  1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
    1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
      1 2 3 4 5 6 7 6 5 4 3 2 1
        1 2 3 4 5 6 5 4 3 2 1
          1 2 3 4 5 4 3 2 1
            1 2 3 4 3 2 1
              1 2 3 2 1
                1 2 1
                  1
 
'''

for i in range(10):
    # Print leading spaces
    for j in range(10 - i):
        print(" ", end=" ")
    # Count up
    for j in range(1, i + 1):
        print(j, end=" ")
    # Count down
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    # Next row
    print()

for i in range(10):
    # Print leading spaces
    for j in range(i + 2):  # After starting with copy/paste to get first triangle, need to start with 2 spaces
        print(" ", end=" ")
    # Count down
    for j in range(1, 9 - i):  # Counting up from 1-8, and then 1-7 etc. -> 1
        print(j, end=" ")
    # Count up
    for j in range(7-i, 0, -1):
        print(j, end=" ")
    # Next row
    print()
