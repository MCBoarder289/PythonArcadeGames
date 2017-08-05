"""
Chapter 10 Lab

Moving a cloud with the mouse to cover a skier with the keyboard

"""

import pygame

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


def draw_cloud(screen, x, y):
    """
    Draws a cloud, given screen parameter and the x, y position.
    Uses 3 ellipses to create the cloud image

    :param screen:
    :param x:
    :param y:
    :return:
    """
    x_offset = 0
    y_offset = 0
    for i in range(2):
        pygame.draw.ellipse(screen, CLOUDS, [x + x_offset, 
                                             y + y_offset,  
                                             70 + x_offset, 70 - y_offset], 0)
        x_offset += 20
        y_offset += 25

    x_offset = -20
    y_offset = 25

    pygame.draw.ellipse(screen, CLOUDS, [x + x_offset,  
                                         y + y_offset,  
                                         70 + x_offset, 70 - y_offset], 0)


def draw_skier(screen, x, y):
    """
    Draws a Skier given an x y position

    :param screen:
    :param x:
    :param y:
    :return:
    """
    pygame.draw.circle(screen, BLACK, [x, y], 4)
    if direction == "Left":  # Skis pointing to the left -- if the x_motion is positive
        # Draw Skis
        pygame.draw.line(screen, BLUE, [x - 3, y + 15],
                         [x - 10, y + 25], 2)  # Left
        pygame.draw.line(screen, BLUE,[ x + 5, y + 15],
                             [x - 2, y + 25], 2)  # Right
    else:  # Skis pointing to the right -- if the x_motion is negative
        pygame.draw.line(screen, BLUE, [x - 10, y + 15],
                         [x - 3, y + 25], 2)  # Left
        pygame.draw.line(screen, BLUE, [x - 2, y + 15],
                         [x + 5, y + 25], 2)  # Right
    # Draw Body
    pygame.draw.line(screen, BLACK, [x - 1, y],
                     [x - 1, y + 16], 2)
    # Draw Arms
    pygame.draw.line(screen, BLACK, [x - 6, y + 7],
                     [x + 5, y + 9], 2)
    # Draw Legs
    pygame.draw.line(screen, BLACK, [x - 1, y + 16],
                     [x - 5, y + 18], 2)  # Left
    pygame.draw.line(screen, BLACK, [x - 1, y + 16],
                     [x + 5, y + 18], 2)  # Right

# Setup
pygame.init()

# Set the width and height of the screen [width,height]
size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("User Control Test")

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Current position
skier_x = 10
skier_y = 10

# Skier starting direction
direction = "Left"

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# -------- Main Program Loop -----------
while not done:
    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        
            # Figure out if it was an arrow key. If so
            # adjust speed.
        
            if event.key == pygame.K_LEFT:
                x_speed = -3
                direction = "Left"  # Resets the direction the skis are drawn
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
                direction = "Right"  # Resets the direction the skis are drawn
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3

        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT

    # Set position of mouse for mouse controlled objects
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    
    if skier_x + x_speed <= 0+10:
        skier_x = 0+10
    elif skier_x + x_speed >= size[0]-10:
        skier_x = size[0]-10
    else:
        skier_x = skier_x + x_speed  # Original code, if statements to prevent going beyond screen added by me

    if skier_y + y_speed <= 0+4:
        skier_y = 0+4
    elif skier_y + y_speed >= size[1]-27:
        skier_y = size[1]-27
    else:
        skier_y = skier_y + y_speed 

    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)

    draw_skier(screen, skier_x, skier_y)
    draw_cloud(screen, mouse_x, mouse_y)

    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # Limit to 20 frames per second
    clock.tick(60)

# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit()
