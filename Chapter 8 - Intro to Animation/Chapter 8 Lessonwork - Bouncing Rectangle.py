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

pygame.display.set_caption("Bouncing Rectangle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# ---------------  Absolute Variables/ Starting positions ------------------------

screen_max_x = size[0] - 1  # 699 is max because 700 pixels starting at 0
screen_max_y = size[1] - 1  # 499 is max because 500 pixels starting at 0

# Rectangle position
rect_x = 50
rect_y = 50

rect_width = 50
rect_height = 50

# Rectangle Vector (Direction and Speed)
rect_change_x = 5
rect_change_y = 5

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # Movement direction and speed
    rect_x += rect_change_x
    rect_y += rect_change_y

    # If it hits the edge, it will bounce off the screen in the opposite direction:
    if rect_x + rect_width >= screen_max_x or rect_x <= 0:
        rect_change_x *= -1

    if rect_y + rect_height >= screen_max_y or rect_y <= 0:
        rect_change_y *= -1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, rect_width, rect_height], 0)  # Original White Rect
    pygame.draw.rect(screen, RED, [rect_x + 10, rect_y + 10, rect_width - 20, rect_height - 20], 0)  # Red Rect inside

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
