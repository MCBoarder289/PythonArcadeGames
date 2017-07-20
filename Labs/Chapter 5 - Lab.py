
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

# Set the width and height of the screen

size = (800, 600)
screen = pygame.display.set_mode(size)

# For Random Clouds, setting up random plots
# cloud_num = random.randrange(1, 4) -- Will force 2 clouds, can't figure out naming 1...n variable names
cloud_xlim = 720
cloud_ylim = 100
cloud_heightlim = 100
cloud_widthlim = 180

cloud1x = random.randrange(10, cloud_xlim)
cloud1y = random.randrange(10, cloud_ylim)
cloud1width = random.randrange(100, cloud_widthlim)
cloud1height = random.randrange(50, cloud_heightlim)

cloud2x = random.randrange(10, cloud_xlim)
cloud2y = random.randrange(10, cloud_ylim)
cloud2width = random.randrange(100, cloud_widthlim)
cloud2height = random.randrange(50, cloud_heightlim)


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
    
    # Cloud 1
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud1x + x_offset, cloud1y + y_offset, 70 + x_offset, 70 - y_offset], 0)
        x_offset += 20
        y_offset += 25
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud1x + x_offset, cloud1y + y_offset, 70 + x_offset, 70 - y_offset], 0)
        x_offset -= 20
        y_offset += 25

    # Cloud 2
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud2x + x_offset, cloud2y + y_offset, 70 - x_offset, 70 - y_offset], 0)
        x_offset -= 35
        y_offset += 25
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [cloud2x + x_offset, cloud2y + y_offset, 70 + x_offset, 70 - y_offset], 0)
        x_offset += 20
        y_offset += 25

    # pygame.draw.ellipse(screen, CLOUDS, [cloud2x, cloud2y, cloud2width, cloud2height], 0)

    # ALL CODE TO DRAW SHOULD BE ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(FRAME_RATE)

pygame.quit()
