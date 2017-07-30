"""
Chapter 9 Lab

For prompts, go here: http://programarcadegames.com/index.php?chapter=lab_functions

"""


import random


def min3(a, b, c):
    """
    Returns minimum of 3 inputs

    Test Cases:

    print(min3(4, 7, 5))
    print(min3(4, 4, 4))
    print(min3(5, 3, 6))
    print(min3(5, 5, 6))
    print(min3(6, 5, 4))
    print(min3(3, 5, 3))
    print(min3(4, 5, 5))
    print(min3(-2, -6, -100))
    print(min3("Z", "B", "A"))

    :param a:
    :param b:
    :param c:
    :return:
    """

    if a < b and a < c:
        minimum = a
    elif a == b and b == c:
        minimum = a
    elif b < a and b < c:
        minimum = b
    elif a == b and b < c:
        minimum = a
    elif c < b and c < a:
        minimum = c
    elif a == c and c < b:
        minimum = a
    elif b == c and c < a:
        minimum = c

    return minimum


def box(height, width):
    """
    Returns a box of asterisks given a height and width

    Test Cases:

    box(7, 5)  # Print a box 7 high, 5 across
    print()   # Blank line
    box(3, 2)  # Print a box 3 high, 2 across
    print()   # Blank line
    box(3, 10)  # Print a box 3 high, 10 across

    :param height:
    :param width:
    :return:
    """
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()


def find(list, key):

    """
    Takes a list and returns all of the locations where the provided key matches

    Test Case:

    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]

    find(my_list, 12)
    find(my_list, 91)
    find(my_list, 80)

    :param list:
    :param key:
    :return:
    """

    for i in range(len(list)):
        if list[i] == key:
            print("Found", key, "at position", i)


def create_list(list_size):
    """
    Creates a list of random numbers from 1-6 with list_size number of elements

    Test Case:
    my_list = create_list(5)
    print(my_list)

    :param list_size:
    :return:
    """

    new_list = []
    for i in range(list_size):
        x = random.randrange(1, 7)
        new_list.append(x)
    return new_list


def count_list(input_list, number):
    """
    Takes a list, and returns the number of times that numbers shows up in the list

    Test Case:
    count = count_list([1,2,3,3,3,4,2,1],3)
    print(count)

    :param input_list:
    :param number:
    :return:
    """

    count = 0
    for i in range(len(input_list)):
        if input_list[i] == number:
            count += 1
    return count


def average_list(list_input):
    """
    Takes an input of a list, and averages the contents

    Test Case:
    avg = average_list([1,2,3])
    print(avg)

    :param list_input:
    :return:
    """

    denom = len(list_input)
    num = 0

    for i in range(len(list_input)):
        num += list_input[i]

    list_avg = num / denom
    return list_avg


def main():
    """ Main Program """

    master_list = create_list(10000)

    print("The number 1 appears", count_list(master_list, 1), "times.")
    print("The number 2 appears", count_list(master_list, 2), "times.")
    print("The number 3 appears", count_list(master_list, 3), "times.")
    print("The number 4 appears", count_list(master_list, 4), "times.")
    print("The number 5 appears", count_list(master_list, 5), "times.")
    print("The number 6 appears", count_list(master_list, 6), "times.")

    print()

    print(average_list(master_list))

main()

