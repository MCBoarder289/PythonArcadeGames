
# Libraries
import pygame

# Initialize the game engine
pygame.init()

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the width and height of the screen

size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Mike's Cool Game")

# Need to explain what to do when you click the window, etc. will crash otherwise
# Call this the "main program loop"

# Loop until the user clicks the close button
done = False  # This is the loop control

# Used to manage how fast the screen updates
clock = pygame.time.Clock()  # Control for how fast game runs

# --------------- Main Program Loop -------------------- #

while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.quit():  # If user clicked close
            done = True  # Flag that we are done, so we exit this loop

    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # ALL CODE TO DRAW SHOULD BE ABOVE THIS COMMENT

    # Limit to 20 frames per second
    clock.tick(20)





