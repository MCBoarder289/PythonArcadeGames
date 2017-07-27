"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

# Variables to declare
screen_width = size[0]
screen_height = size[1]
block_width = 5
block_height = 5
space_multiplier = 2

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
    x_row_count = 0
    y_row_count = 0
    for i in range(0, screen_height, space_multiplier * block_height):
        pygame.draw.rect(screen, GREEN, [x_row_count, i, block_width, block_height], 0)

        for j in range(0, screen_width, space_multiplier * block_width):
            pygame.draw.rect(screen, GREEN, [j, y_row_count, block_width, block_height], 0)

        y_row_count += space_multiplier * block_height
        x_row_count += space_multiplier * block_width

    """"
    origin = [0, 0]
    for i in range(0, screen_width, block_size):
        pygame.draw.rect(screen, GREEN, [origin[0], origin[1], block_size, block_size], 0)

        for j in range(0, screen_height, block_size):
            pygame.draw.rect(screen, GREEN, [i, i, block_size, block_size], 0)
            origin[1] += 2*block_size
    """
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

