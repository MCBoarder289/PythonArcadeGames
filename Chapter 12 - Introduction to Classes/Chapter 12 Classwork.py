"""
12.4.2 Review Questions

    Create a class called Cat. Give it attributes for name, color, and weight. Give it a method called meow.
    Create an instance of the cat class, set the attributes, and call the meow method.
    Create a class called Monster. Give it an attribute for name and an integer attribute for health.
    Create a method called decrease_health that takes in a parameter amount and decreases the health by that much.
    Inside that method, print that the animal died if health goes below zero

"""


class Cat():

    name = ""
    color = ""
    weight = 0

    def __init__(self, my_name):
        self.name = my_name
        self.color = "Black"
        self.weight = 5
        print("A new Cat is born! It's name is", my_name)

    def meow(self):
        print("\"Meow!\"", "said", self.name)


class Monster():

    name = ""
    health = 5

    def __init__(self):
        self.name = "Spooky"
        self.health = 5

    def decrease_health(self, number):
        self.health -= number
        if self.health <= 0:
            print(self.name, "has died")


new_cat = Cat("Stripes")
# new_cat.name = "Max"
new_cat.color = "Orange"
new_cat.weight = 8

new_cat.meow()

"""
12.5.2 Review Questions

    Should class names begin with an upper or lower case letter?
    Should method names begin with an upper or lower case letter?
    Should attribute names begin with an upper or lower case letter?
    Which should be listed first in a class, attributes or methods?
    What are other names for a reference?
    What is another name for instance variable?
    What is the name for an instance of a class?
    Create a class called Star that will print out “A star is born!” every time it is created.
    Create a class called Monster with attributes for health and a name. 
    Add a constructor to the class that sets the health and name of the object with data passed in as parameters. 
"""

# Upper
# lower
# lower
# attributes
# attributes, fields
# pointer


class Star():

    def __init__(self):
        print("A star is born!")


class Monster():

    name = ""
    health = 0

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def decrease_health(self, number):
        self.health -= number
        if self.health <= 0:
            print(self.name, "has died")


spooky = Monster("Spooky", 5)

print(spooky.health, spooky.name)



""" Chapter 12 Worksheet """

# Question 1 - What is the difference between a class and an object?

# Answer - A Class is more of a general definition or grouping of common attributes that can make up multiple instances
# of an object. An object is a singular thing, whereas a class is a definition/structure of what an object can be.

# Question 2 - What is the difference between a function and a method?

# Answer -  A function is a single defined action that can be done in general in a script/program. A method is a
# function that is specifically tied to a class. Therefore it can be only be used by an instance of a class.

# Question 3 - Write code to create an instance of this class and set its attributes. Remember, don't store numbers
# as strings. Use 40 and not "40".


class Dog():
    def __init__(self):
        self.age = 0
        self.name = ""
        self.weight = 0


spot = Dog()
spot.name = "Spot"
spot.weight = 15
spot.age = 3

# Question 4 - Write code to create two different instances of this class and set attributes for both objects.
# While a phone number is a number, those should be stored as strings. So we can keep leading zeros and those dashes.


class Person():
    def __init__(self):
        self.name = ""
        self.cell_phone = ""
        self.email = ""


mike = Person()
mike.name = "Mike"
mike.cell_phone = "222-555-1515"
mike.email = "test@gmail.com"

lauren = Person()
lauren.name = "Lauren"
lauren.cell_phone = "333-555-1616"
lauren.email = "test2@gmail.com"

# Question 5 - For the code below, write a class that has the appropriate class name
# and attributes that will allow the code to work.

# Answer = next 5 lines...
class Bird():
    def __init__(self):
        self.color = ""
        self.name = ""
        self.breed = ""


my_bird = Bird()
my_bird.color = "green"
my_bird.name = "Sunny"
my_bird.breed = "Sun Conure"

# Question 6 - Define a class that would represent a character in a simple 2D game.
# Include attributes for the position, name, and strength.


class Character():
    def __init__(self):
        self.x_position = 0
        self.y_position = 0
        self.name = ""
        self.strength = 0


# Question 7 - The following code runs, but it is not correct. What did the programmer do wrong?


class Person():
    def __init__(self):
        self.name = ""
        self.money = 0

nancy = Person()
name = "Nancy"
money = 100

# Answer - The programmer didn't assign the attributes to the instance "nancy" of the class with the dot operator.

# Question 8 - Take a look at the code. It does not run. What is the error that prevents it from running?


class Person():
    def __init__(self):
        self.name = ""
        self.money = 0


bob = Person()
print(bob.name, "has", money, "dollars.")

# Answer - The code does not run because there is no variable "money" defined.
# We need to make it specific to the bob instance

# Question 9 - Even with that error fixed, the program will not print out:
"""
Bob has 0 dollars.
Instead it just prints out:
has 0 dollars.
Why is this the case? 
"""

# Answer - This is the case because the bob instance's name has not been changed from the default "" setting.

# Section 2:

"""
To answer the next four questions, create one program. In that program will be the answers for all four questions. 
Make sure the program runs, and then copy/paste from the program to answer each of the questions below.

You should have a program that starts with three class definitions, one each for the first three questions. 
Then code that will create instances of each class, and that will be the answer to the last problem.

    Write code that defines a class named Animal:
        Add an attribute for the animal name.
        Add an eat() method for Animal that prints ``Munch munch.''
        A make_noise() method for Animal that prints ``Grrr says [animal name].''
        Add a constructor for the Animal class that prints ``An animal has been born.''
    A class named Cat:
        Make Animal the parent.
        A make_noise() method for Cat that prints ``Meow says [animal name].''
        A constructor for Cat that prints ``A cat has been born.''
        Modify the constructor so it calls the parent constructor as well.
    A class named Dog:
        Make Animal the parent.
        A make_noise() method for Dog that prints ``Bark says [animal name].''
        A constructor for Dog that prints ``A dog has been born.''
        Modify the constructor so it calls the parent constructor as well.
    A main program with:
        Code that creates a cat, two dogs, and an animal.
        Sets the name for each animal.
        Code that calls eat() and make_noise() for each animal. (Don't forget this!) 

"""

class Animal():
    def __init__(self):
        self.name = ""
        print('An animal has been born')

    def eat(self):
        print('Munch munch.')

    def make_noise(self):
        print('Grrr says', self.name)


class Cat(Animal):
    def __init__(self):
        super().__init__()
        print('A cat has been born')

    def make_noise(self):
        print('Meow says', self.name)


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('A dog has been born')

    def make_noise(self):
        print('Woof says', self.name)



max = Cat()
max.name = "Max"

king = Dog()
king.name = "King"

ebony = Dog()
ebony.name = "Ebony"

me = Animal()
me.name = "Tiger"

max.eat()
max.make_noise()

king.eat()
king.make_noise()

ebony.eat()
ebony.make_noise()

me.eat()
me.make_noise()




