
"""

Chapter 5 Lab - Drawing the Ski Slope Scene

"""

# Import Statements

import pygame
import random
import math


pygame.init()

# Defining my colors:

SKY = (131, 211, 242)
SUN = (242, 247, 77)
CLOUDS = (206, 207, 202)
LODGE_BASE = (105, 6, 6)
BLACK = (0, 0, 0)
TRUNK = (51, 5, 5)
GREEN = (28, 51, 5)
WHITE = (255, 255, 255)
SNOW = (235, 240, 242)
BLUE = (0, 0, 255)

# Set the width and height of the screen

size = (800, 600)
screen = pygame.display.set_mode(size)

screen_max_x = size[0] - 1  # 699 is max because 700 pixels starting at 0
screen_max_y = size[1] - 1  # 499 is max because 500 pixels starting at 0

# For Random Clouds, setting up random plots and forcing boundaries
# cloud_num = random.randrange(1, 4) -- Will force 2 clouds, can't figure out naming 1...n variable names- SOLVED BELOW!
cloud_xlim = 720
cloud_ylim = 100
cloud_heightlim = 100
cloud_widthlim = 180

cloud_elements = {}  # Create a dictionary of cloud coordinates
for i in range(1, 3, 1):
    cloud_elements["cloud{0}".format(i)] = (random.randrange(10, cloud_xlim), random.randrange(10, cloud_ylim),
                                               random.randrange(100, cloud_widthlim),
                                               random.randrange(50, cloud_heightlim))


# For Random Trees, setting up random initial coordinates

# Trees on the left first....

trees_y_upperlim = 200
trees_y_lowerlim = 600
trees_left_xlim = 320
trees_right_xlim = 480

left_trees = {}
right_trees = {}

for i in range(25):
    left_trees["tree{0}".format(i)] = (random.randrange(-5, trees_left_xlim),  # Random x coordinate
                                       random.randrange(trees_y_upperlim, trees_y_lowerlim))  # Random y coordinate

    right_trees["tree{0}".format(i)] = (random.randrange(trees_right_xlim, 805),
                                        random.randrange(trees_y_upperlim, trees_y_lowerlim))

# Random Snowfall animation (from Chapter 8):

snow_coordinates = []
for i in range(50):
    x = random.randrange(0, screen_max_x)
    y = random.randrange(0, screen_max_y)
    snow_coordinates.append([x, y])

# Random People Coordinates:
people_coordinates = []
for i in range(6):
    x = random.randrange(trees_left_xlim, trees_right_xlim)
    y = random.randrange(trees_y_upperlim, trees_y_lowerlim)
    x_motion = 2
    y_motion = 2
    people_coordinates.append([x, y, x_motion, y_motion])

# People Vectors:
people_change_x = 2
people_change_y = 2

''' # Taking out bad practice of numbered variables

cloud1x = random.randrange(10, cloud_xlim)
cloud1y = random.randrange(10, cloud_ylim)
cloud1width = random.randrange(100, cloud_widthlim)
cloud1height = random.randrange(50, cloud_heightlim)

cloud2x = random.randrange(10, cloud_xlim)
cloud2y = random.randrange(10, cloud_ylim)
cloud2width = random.randrange(100, cloud_widthlim)
cloud2height = random.randrange(50, cloud_heightlim)
'''
pygame.display.set_caption("Ski Scene - Ch. 5 Lab")

# Set Frame Rate
FRAME_RATE = 60

done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # Control for how fast game runs

# Main Program Loop -------------------------------------

while not done:

    # ---------- Main Event Loop ---------- #
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close note, this is not pygame.quit() which is a function
            done = True  # Flag that we are done, so we exit this loop

    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(WHITE)  # This will act as the snow

    # Draw my sky -----------------------------
    pygame.draw.polygon(screen, SKY, [[0, 0], [800, 0], [800, 200], [0, 150]], 0)

    # Draw the sun ----------------------------
    pygame.draw.ellipse(screen, SUN, [750, -10, 60, 60], 0)

    # Draw random clouds ----------------------
    # Need to do the randomizing outside the loop, or else it will continuously change...
    
    # Cloud 1  Basically draws an ellipse, and then one to the left and one to the right
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud_elements["cloud1"][0] + x_offset,  # cloud_elements index pull
                                             cloud_elements["cloud1"][1] + y_offset,  # cloud_elements index pull
                                             70 + x_offset, 70 - y_offset], 0)
        x_offset += 20
        y_offset += 25
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud_elements["cloud1"][0] + x_offset,  # cloud_elements index pull
                                             cloud_elements["cloud1"][1] + y_offset,  # cloud_elements index pull
                                             70 + x_offset, 70 - y_offset], 0)
        x_offset -= 20
        y_offset += 25

    # Cloud 2
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud_elements["cloud2"][0] + x_offset,
                                             cloud_elements["cloud2"][1] + y_offset,
                                             70 - x_offset, 70 - y_offset], 0)
        x_offset -= 35
        y_offset += 25
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud_elements["cloud2"][0] + x_offset,
                                             cloud_elements["cloud2"][1] + y_offset,
                                             70 + x_offset, 70 - y_offset], 0)
        x_offset += 20
        y_offset += 25

    # Draw Lodge -------------------------
    pygame.draw.rect(screen, LODGE_BASE, [375, 210, 50, 30], 0)
    pygame.draw.polygon(screen, BLACK, [(375, 210), (400, 195), (425, 210)], 0)

    # Draw People ------------------------ with animation
    for i in range(len(people_coordinates)):
        # Draw Head  -- Need to create variables for each of these once done drawing...
        pygame.draw.circle(screen, BLACK, [people_coordinates[i][0], people_coordinates[i][1]], 4)
        if people_coordinates[i][2] < 0:  # Skis pointing to the right -- if the x_motion is positive
            # Draw Skis
            pygame.draw.line(screen, BLUE, [people_coordinates[i][0] - 3, people_coordinates[i][1] + 15],
                             [people_coordinates[i][0] - 10, people_coordinates[i][1] + 25], 2)  # Left
            pygame.draw.line(screen, BLUE, [people_coordinates[i][0] + 5, people_coordinates[i][1] + 15],
                             [people_coordinates[i][0] - 2, people_coordinates[i][1] + 25], 2)  # Right
        else:  # Skis pointing to the left -- if the x_motion is negative
            pygame.draw.line(screen, BLUE, [people_coordinates[i][0] - 10, people_coordinates[i][1] + 15],
                             [people_coordinates[i][0] - 3, people_coordinates[i][1] + 25], 2)  # Left
            pygame.draw.line(screen, BLUE, [people_coordinates[i][0] - 2, people_coordinates[i][1] + 15],
                             [people_coordinates[i][0] + 5, people_coordinates[i][1] + 25], 2)  # Right
        # Draw Body
        pygame.draw.line(screen, BLACK, [people_coordinates[i][0] - 1, people_coordinates[i][1]],
                         [people_coordinates[i][0] - 1, people_coordinates[i][1] + 16], 2)
        # Draw Arms
        pygame.draw.line(screen, BLACK, [people_coordinates[i][0] - 6, people_coordinates[i][1] + 7],
                         [people_coordinates[i][0] + 5, people_coordinates[i][1] + 9], 2)
        # Draw Legs
        pygame.draw.line(screen, BLACK, [people_coordinates[i][0] - 1, people_coordinates[i][1] + 16],
                         [people_coordinates[i][0] - 5, people_coordinates[i][1] + 18], 2)  # Left
        pygame.draw.line(screen, BLACK, [people_coordinates[i][0] - 1, people_coordinates[i][1] + 16],
                         [people_coordinates[i][0] + 5, people_coordinates[i][1] + 18], 2)  # Right

        people_coordinates[i][1] += people_coordinates[i][3]  # Adding the y_motion to the coordinate
        people_coordinates[i][0] += people_coordinates[i][2]  # Adding the x_motion to the coordinate

        if people_coordinates[i][1] >= screen_max_y:  # Respawn at the top
            people_coordinates[i][1] = random.randrange(trees_y_upperlim, trees_y_lowerlim)
            people_coordinates[i][0] = random.randrange(trees_left_xlim, trees_right_xlim)

        if people_coordinates[i][0] >= trees_right_xlim:  # Move back to the left, changes the x_motion coordinate
            people_coordinates[i][2] *= -1

        if people_coordinates[i][0] <= trees_left_xlim:  # Move back to the right, changes the x_motion coordinate
            people_coordinates[i][2] *= -1

        if people_coordinates[i][1] >= screen_max_y:  # Respawn at the top
            people_coordinates[i][1] = random.randrange(trees_y_upperlim, trees_y_lowerlim)
            people_coordinates[i][0] = random.randrange(trees_left_xlim, trees_right_xlim)

    # Draw Lift Lines --------------------
    pygame.draw.polygon(screen, BLACK, [(430, 600), (445, 210), (460, 210), (450, 600)], 2)
    # Draw Lift Poles --------------------
    pygame.draw.line(screen, LODGE_BASE, (445, 210), (460, 210), 4)
    pygame.draw.line(screen, LODGE_BASE, (452.5, 210), (452.5, 230), 4)

    pygame.draw.line(screen, LODGE_BASE, (441, 350), (456, 350), 4)
    pygame.draw.line(screen, LODGE_BASE, (448.5, 350), (448.5, 385), 4)

    pygame.draw.line(screen, LODGE_BASE, (436, 500), (451, 500), 4)
    pygame.draw.line(screen, LODGE_BASE, (443.5, 500), (443.5, 545), 4)

    # Draw Trees -----------------------------
    # pygame.draw.polygon(screen, GREEN, [(202, 298), (202, 295), (198, 295), (205, 280), (210, 280), (217, 295),
    #                                    (213, 295), (213, 298)], 0)
    # pygame.draw.line(screen, LODGE_BASE, (207.5, 298), (207.5, 303), 5)

    mult = 0.8
    for k, v in left_trees.items():
        pygame.draw.polygon(screen, GREEN,
                            [(v[0], v[1]), (v[0], v[1] - (6 * mult)),
                             (v[0] - (8 * mult), v[1] - (6 * mult)),
                             (v[0] + (6 * mult), v[1] - (36 * mult)),
                             (v[0] + (16 * mult), v[1] - (36 * mult)),
                             (v[0] + (30 * mult), v[1] - (6 * mult)),
                             (v[0] + (22 * mult), v[1] - (6 * mult)),
                             (v[0] + (22 * mult), v[1])], 0)
        pygame.draw.line(screen, LODGE_BASE, (((v[0] + v[0] + (22 * mult)) / 2), v[1]),
                         (((v[0] + v[0] + (22 * mult)) / 2), v[1] + (10 * mult)), int(10 * mult))

    for k, v in right_trees.items():
        pygame.draw.polygon(screen, GREEN,
                            [(v[0], v[1]), (v[0], v[1] - (6 * mult)),
                             (v[0] - (8 * mult), v[1] - (6 * mult)),
                             (v[0] + (6 * mult), v[1] - (36 * mult)),
                             (v[0] + (16 * mult), v[1] - (36 * mult)),
                             (v[0] + (30 * mult), v[1] - (6 * mult)),
                             (v[0] + (22 * mult), v[1] - (6 * mult)),
                             (v[0] + (22 * mult), v[1])], 0)
        pygame.draw.line(screen, LODGE_BASE, (((v[0] + v[0] + (22 * mult)) / 2), v[1]),
                         (((v[0] + v[0] + (22 * mult)) / 2), v[1] + (10 * mult)), int(10 * mult))

    # Draw Snow --------------------------
    # Placing this last to be in the foreground over the trees

    """
    # Original Snow loop -- uses item in list vs. index variable, so it works with a copy and doesn't modify list
    
     for coordinates in snow_coordinates:
        coordinates[1] += 1
        pygame.draw.circle(screen, SNOW, coordinates, 2)

        if coordinates[1] > screen_max_y:
            coordinates[1] = random.randrange(-20, -5)
            coordinates[0] = random.randrange(screen_max_x)
    """
    for i in range(len(snow_coordinates)):
        pygame.draw.circle(screen, SNOW, snow_coordinates[i], 2)
        snow_coordinates[i][1] += 1
        if snow_coordinates[i][1] > screen_max_y:
            snow_coordinates[i][1] = random.randrange(-20, -5)  # reset it just above the top to simulate new falling
            snow_coordinates[i][0] = random.randrange(screen_max_x)

    ''' # Latest Attempt to draw trees, trying to use dictionaries now
    x_offset = 0
    y_offset = 0
    initial_x = 202
    initial_y = 298
    mult = 0.8

    for i in range(2):
        pygame.draw.polygon(screen, GREEN,
                            [(initial_x, initial_y), (initial_x, initial_y - (6*mult)), (initial_x - (8*mult), initial_y - (6*mult)),
                             (initial_x + (6*mult), initial_y - (36*mult)), (initial_x + (16*mult), initial_y - (36*mult)),
                             (initial_x + (30*mult), initial_y - (6*mult)), (initial_x + (22*mult), initial_y - (6*mult)),
                             (initial_x + (22*mult), initial_y)], 0)
        pygame.draw.line(screen, LODGE_BASE, (((initial_x + initial_x + (22*mult)) / 2), initial_y),
                         (((initial_x + initial_x + (22*mult)) / 2), initial_y + (10*mult)), int(10*mult))
        x_offset -= 30
        y_offset -= 30
        initial_x = initial_x + x_offset
        initial_y = initial_y + y_offset

    x_offset = 0
    y_offset = 0
    initial_x = 120
    initial_y = 285
    mult = 0.8

    for i in range(3):
        pygame.draw.polygon(screen, GREEN,
                            [(initial_x, initial_y), (initial_x, initial_y - (6 * mult)),
                             (initial_x - (8 * mult), initial_y - (6 * mult)),
                             (initial_x + (6 * mult), initial_y - (36 * mult)),
                             (initial_x + (16 * mult), initial_y - (36 * mult)),
                             (initial_x + (30 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y)], 0)
        pygame.draw.line(screen, LODGE_BASE, (((initial_x + initial_x + (22 * mult)) / 2), initial_y),
                         (((initial_x + initial_x + (22 * mult)) / 2), initial_y + (10 * mult)), int(10 * mult))
        x_offset -= 30
        y_offset -= 30
        initial_x = initial_x + x_offset
        initial_y = initial_y + y_offset
        x_offset = 0
        y_offset = 0

    x_offset = 0
    y_offset = 0
    initial_x = 100
    initial_y = 415
    mult = 0.8

    for i in range(3):
        pygame.draw.polygon(screen, GREEN,
                            [(initial_x, initial_y), (initial_x, initial_y - (6 * mult)),
                             (initial_x - (8 * mult), initial_y - (6 * mult)),
                             (initial_x + (6 * mult), initial_y - (36 * mult)),
                             (initial_x + (16 * mult), initial_y - (36 * mult)),
                             (initial_x + (30 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y)], 0)
        pygame.draw.line(screen, LODGE_BASE, (((initial_x + initial_x + (22 * mult)) / 2), initial_y),
                         (((initial_x + initial_x + (22 * mult)) / 2), initial_y + (10 * mult)), int(10 * mult))
        x_offset -= 30
        y_offset += 30
        initial_x = initial_x + x_offset
        initial_y = initial_y + y_offset

    x_offset = 0
    y_offset = 0
    initial_x = 300
    initial_y = 500
    mult = 0.8

    for i in range(3):
        pygame.draw.polygon(screen, GREEN,
                            [(initial_x, initial_y), (initial_x, initial_y - (6 * mult)),
                             (initial_x - (8 * mult), initial_y - (6 * mult)),
                             (initial_x + (6 * mult), initial_y - (36 * mult)),
                             (initial_x + (16 * mult), initial_y - (36 * mult)),
                             (initial_x + (30 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y - (6 * mult)),
                             (initial_x + (22 * mult), initial_y)], 0)
        pygame.draw.line(screen, LODGE_BASE, (((initial_x + initial_x + (22 * mult)) / 2), initial_y),
                         (((initial_x + initial_x + (22 * mult)) / 2), initial_y + (10 * mult)), int(10 * mult))
        x_offset -= 30
        y_offset -= 30
        initial_x = initial_x + x_offset
        initial_y = initial_y + y_offset
    '''
    ''' # Multiplication attempt of drawing trees -----------------
    pygame.draw.polygon(screen, GREEN,
                        [(initial_x, initial_y), (initial_x, initial_y - 6), (initial_x - 8, initial_y - 6),
                         (initial_x + 6, initial_y - 36), (initial_x + 16, initial_y - 36),
                         (initial_x + 30, initial_y - 6), (initial_x + 22, initial_y - 6),
                         (initial_x + 22, initial_y)], 0)
    pygame.draw.line(screen, LODGE_BASE, (((initial_x + initial_x + 22) / 2), initial_y),
                     (((initial_x + initial_x + 22) / 2), initial_y + 10), 10)

    '''
    ''' # Original Pattern of drawing trees -----------------
    pygame.draw.polygon(screen, GREEN, [(initial_x, initial_y), (initial_x, initial_y-3), (initial_x - 4, initial_y-3),
                                        (initial_x+3, initial_y-18), (initial_x+8,  initial_y-18),
                                        (initial_x+15, initial_y-3), (initial_x+11, initial_y-3),
                                        (initial_x+11, initial_y)], 0)
    pygame.draw.line(screen, LODGE_BASE, (((initial_x+initial_x+11)/2), initial_y),
                                         (((initial_x+initial_x+11)/2), initial_y+5), 5)

    '''
    # ALL CODE TO DRAW SHOULD BE ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(FRAME_RATE)

pygame.quit()
