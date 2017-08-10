"""

Chapter 11 Lab Work

"""

import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GREY = (189, 183, 181)

# Define Functions


def draw_asteroid(screen, x, y):
    pygame.draw.polygon(screen, GREY, [(0 + x, 0 + y), (15 + x, -5 + y), (20 + x, 10 + y),
                                       (18 + x, 12 + y), (8 + x, 5 + y), (3 + x, 2 + y)])

pygame.init()

# Set the width and height of the screen [width, height]
size = (800, 800)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 11 Lab")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Loading background image / sounds
background_image = pygame.image.load("corona_stretch.png").convert()  # https://opengameart.org/content/ulukais-space-skyboxes

player_left = pygame.image.load("shipsheetparts_player_left.png").convert()  # https://opengameart.org/content/space-ship-building-bits-volume-1
player_left.set_colorkey(WHITE)
player_right = pygame.image.load("shipsheetparts_player_right.png").convert()
player_right.set_colorkey(WHITE)
player_up = pygame.image.load("shipsheetparts_player_up.png").convert()
player_up.set_colorkey(WHITE)
player_down = pygame.image.load("shipsheetparts_player_down.png").convert()
player_down.set_colorkey(WHITE)

player_image = player_up
player_x = 100
player_y = 100

# Speed in pixels per frame
x_speed = 0
y_speed = 0

# Asteroid x,y positions
x = 0
y = 0

x_max = size[0] + 20  # +20 is to render them off screen)
y_max = size[1]

asteroid_speed = 10

asteroid_coordinates = []

for i in range(20):
    x = x_max  # x coordinate of asteroid
    y = random.randrange(5, y_max - 5)  # y coordinate of asteroid
    z = random.randrange(2, 10)  # speed of asteroid
    asteroid_coordinates.append([x, y, z])

shoot_sound = pygame.mixer.Sound("laser5.ogg")

# Background movement

bg_speed = 1
bg_x_position = 0

# Hide the mouse cursor
pygame.mouse.set_visible(0)

# Load Space Ambient Music
# Available from:
# https://opengameart.org/content/space-ambient
pygame.mixer.music.load('ville_seppanen-1_g.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot_sound.play()

            if event.key == pygame.K_LEFT:
                player_image = player_left
                x_speed = -3

            if event.key == pygame.K_RIGHT:
                player_image = player_right
                x_speed = 3

            if event.key == pygame.K_UP:
                player_image = player_up
                y_speed = -3

            if event.key == pygame.K_DOWN:
                player_image = player_down
                y_speed = 3

        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0

        elif event.type == pygame.constants.USEREVENT:
            # This event is triggered when the song stops playing.
            #
            # Next, play "Alone" by Saito Koji
            # Available from:
            # http://freemusicarchive.org/music/Saito_Koji/Again/01-Alone
            pygame.mixer.music.load('Saito_Koji_-_01_-_Alone.mp3')
            pygame.mixer.music.play()

    # --- Game logic should go here

    if player_x + x_speed <= 0:
        player_x = 0
    elif player_x + x_speed >= size[0] - 14:
        player_x = size[0] - 14
    else:
        player_x = player_x + x_speed  # Original code, if statements to prevent going beyond screen added by me

    if player_y + y_speed <= 0:
        player_y = 0
    elif player_y + y_speed >= size[1] - 27:
        player_y = size[1] - 27
    else:
        player_y = player_y + y_speed  # Original code, if statements to prevent going beyond screen added by me

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.

    # Scrolling Background code: https://www.youtube.com/watch?v=US3HSusUBeI

    # Relative X is the modulus of x over the width of the background
    rel_x = bg_x_position % background_image.get_rect().width
    screen.blit(background_image, [rel_x - background_image.get_rect().width, 0])
    if rel_x < size[1]:
        screen.blit(background_image, [rel_x, 0])

    bg_x_position = bg_x_position - bg_speed

    # screen.blit(background_image, [bg_x_position, 0])

    # Copy player image to screen:
    screen.blit(player_image, [player_x, player_y])

    # Drawing Asteroids

    for i in range(len(asteroid_coordinates)):
        draw_asteroid(screen, asteroid_coordinates[i][0], asteroid_coordinates[i][1])
        asteroid_coordinates[i][0] -= asteroid_coordinates[i][2]

        if asteroid_coordinates[i][0] <= - 20:  # Re-spawn to the right
            asteroid_coordinates[i][1] = random.randrange(5, y_max - 5)
            asteroid_coordinates[i][0] = x_max + 20

    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()

