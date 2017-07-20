
# Libraries
import pygame
import math

# Initialize the game engine
pygame.init()

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# SET PI
PI = 3.141592653


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
    # radius = 100
    # origin_x = 0
    # origin_y = 100

    """
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 1)
    pygame.draw.line(screen, GREEN, [200, 0], [100, 100], 1)
    pygame.draw.line(screen, GREEN, [100, 100], [200, 200], 1)
    pygame.draw.line(screen, GREEN, [0, 200], [100, 100], 1)
    pygame.draw.line(screen, GREEN, [100, 0], [100, 100], 1)
    pygame.draw.line(screen, GREEN, [100, 100], [100, 200], 1)
    pygame.draw.line(screen, GREEN, [0, 100], [100, 100], 1)
    pygame.draw.line(screen, GREEN, [200, 100], [100, 100], 1)
    # pygame.draw.line(screen, GREEN, [200, 0], [100, 100], 5)
    """

    # Draw on the screen several lines from (0, 10) to (100, 110)
    # 5 pixels wide using a while loop
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)
        y_offset = y_offset + 10

    # Draw on the screen several lines from (0,10) to (100,110)
    # 5 pixels wide using a for loop -- same as above but more concise
    for y_offset in range(0, 100, 10):
        pygame.draw.line(screen, RED, [0, 10 + y_offset], [100, 110 + y_offset], 5)

    # For this code, make sure to have a line that says
    # "import math" at the top of your program. Otherwise
    # it won't know what math.sin is.

    for i in range(200):
        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x, y], [x + 5, y], 5)

    # Draw some X's
    for x_offset in range(30, 300, 30):
        pygame.draw.line(screen, BLACK, [x_offset, 100], [x_offset - 10, 90], 2)
        pygame.draw.line(screen, BLACK, [x_offset, 90], [x_offset - 10, 100], 2)

    # Draw Rectangles/ Ellipses
    pygame.draw.rect(screen, GREEN, [350, 250, 100, 50], 1)
    pygame.draw.ellipse(screen, GREEN, [350, 250, 100, 50], 0)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(screen, GREEN, [100, 100, 250, 200], PI / 2, PI, 1)
    pygame.draw.arc(screen, BLACK, [100, 100, 250, 200], 0, PI / 2, 1)
    pygame.draw.arc(screen, RED, [100, 100, 250, 200], 3 * PI / 2, 2 * PI, 1)
    pygame.draw.arc(screen, BLUE, [100, 100, 250, 200], PI, 3 * PI / 2, 1)

    # This draws a triangle using the polygon command
    pygame.draw.polygon(screen, BLACK, [[500, 100], [400, 200], [600, 200]], 5)

    # ALL CODE TO DRAW SHOULD BE ABOVE THIS COMMENT
    pygame.display.flip()
    # Limit to 20 frames per second
    clock.tick(60)

pygame.quit()





