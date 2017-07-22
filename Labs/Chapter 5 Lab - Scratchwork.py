
# Import Statements

import random
import math


# Defining my colors:

SKY = (131, 211, 242)
SUN = (242, 247, 77)
CLOUDS = (206, 207, 202)
LODGE_BASE = (105, 6, 6)
BLACK = (0, 0, 0)
TRUNK = (51, 5, 5)
GREEN = (28, 51, 5)
WHITE = (255, 255, 255)

# Set the width and height of the screen

size = (800, 600)


# For Random Clouds, setting up random plots
# cloud_num = random.randrange(1, 4) -- Will force 2 clouds, can't figure out naming 1...n variable names
cloud_xlim = 720
cloud_ylim = 100
cloud_heightlim = 100
cloud_widthlim = 180

cloud_coordinates = {}  # Create a dictionary of cloud coordinates
for i in range(1, 3, 1):
    cloud_coordinates["cloud{0}".format(i)] = [(random.randrange(10, cloud_xlim), random.randrange(10, cloud_ylim)),
                                               (random.randrange(10, cloud_xlim), random.randrange(10, cloud_ylim)), 5]

cloud_coordinates  # Returns every element in the dictionary
cloud_coordinates['cloud1']  # Returns the Cloud 1 data
cloud_coordinates['cloud1'][0]  # Returns the first element Cloud 1's data

# {'cloud1': [(337, 63), (48, 74), 5], 'cloud2': [(365, 85), (264, 40), 5]}
# 337, 74, 5 // 365, 40 , 5
print(cloud_coordinates)

for a, b in cloud_coordinates.items():
    print(a)
    print(b[1][1])

for x, y in cloud_coordinates.items():
    print(y[1])  # Can take an index from a tuple
    # https://stackoverflow.com/questions/3136059/getting-one-value-from-a-python-tuple
print(cloud_coordinates['cloud1'])
print(cloud_coordinates['cloud2'])
# print(cloud_coordinates[cloud1])
