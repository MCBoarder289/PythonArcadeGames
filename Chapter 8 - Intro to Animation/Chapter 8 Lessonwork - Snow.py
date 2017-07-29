"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Snow Example")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------  Absolute Variables/ Starting positions ------------------------

screen_max_x = size[0] - 1  # 699 is max because 700 pixels starting at 0
screen_max_y = size[1] - 1  # 499 is max because 500 pixels starting at 0

# Creating Random Snow Coordinates
snow_coordinates = []
for i in range(50):
    x = random.randrange(0, screen_max_x)
    y = random.randrange(0, screen_max_y)
    snow_coordinates.append([x, y])


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here
    """
    # Original Snow loop -- uses item in list vs. index variable, so it works with a copy and doesn't modify list
    
    for coordinates in snow_coordinates:
        coordinates[1] += 1
        pygame.draw.circle(screen, WHITE, coordinates, 2)

        if coordinates[1] > screen_max_y:
            coordinates[1] = random.randrange(-20, -5)  # reset it just above the top so that the falling appears
            coordinates[0] = random.randrange(screen_max_x)
            
    """
    # New Snow Loop, using index variables to actually change the list
    for i in range(len(snow_coordinates)):
        pygame.draw.circle(screen, WHITE, snow_coordinates[i], 2)
        snow_coordinates[i][1] += 1
        if snow_coordinates[i][1] > screen_max_y:
            snow_coordinates[i][1] = random.randrange(-20, -5)  # reset it just above the top to simulate new falling
            snow_coordinates[i][0] = random.randrange(screen_max_x)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
