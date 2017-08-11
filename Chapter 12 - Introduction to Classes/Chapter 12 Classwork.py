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