
# What does this print? Why? --- this will print a a a b b b because the loops are in order, and the indent is equal
for i in range(3):
    print("a")
for j in range(3):
    print("b")

# What does this print? Why? --- this will print a b b b 3 times because the j loop is indented inside the i loop.
for i in range(3):
    print("a")
    for j in range(3):
        print("b")

print("Done")

# Keep a running total:

total = 0
for i in range(5):
    new_number = int(input("Enter a number: " ))
    total += new_number
print("The total is: ", total)


# What is the value of a? --- it will be 110, because the inner loop will add 10, then plus 1 for the first loop.

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)
