
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

# --------------- Main Program Loop --------------- #

while not done:

    # ---------- Main Event Loop ---------- #
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close note, this is not pygame.quit() which is a function
            print("User asked to quit.")
            done = True  # Flag that we are done, so we exit this loop
        '''
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
        '''
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.line(screen, RED, [50, 0], [50, 50], 2)
    # ALL CODE TO DRAW SHOULD BE ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(60)

pygame.quit()





