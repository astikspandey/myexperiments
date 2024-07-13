import pygame
import sys


def setup_display(pygame, width, height):
    # Set up display
    # width, height = 600, 400
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Platformer")
    return screen

# Initialize Pygame
pygame.init()
a = 0

# Set up display
width, height = 1200, 800
# screen = pygame.display.set_mode((width, height))
# pygame.display.set_caption("Platformer")

screen = setup_display(pygame, width, height)
# Set up colors
white = (255, 255, 255)
red = (255, 0, 0)
purple = (255,0,255)
green = (0,255,255)
black = (0,0,0)
torquise = (0,155,255)

# Set up player
player_size = 50
player_x = width // 2 - player_size // 2
player_y = 250
player_speed = 10
is_jumping = "false"
jump_count = 10

# Game loops
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    if not is_jumping:
        if keys[pygame.K_UP]:
            is_jumping = True
    else:
        if jump_count >= -15:
            neg = 1
            if jump_count < 0:
                neg = -1
            player_y -= (jump_count ** 2) * 0.5 * neg
            jump_count -= 1
        else:
                is_jumping = False
                jump_count = 15
    if player_x == purple:
        player_x=red
    if screen.get_at((int(player_x + player_size // 2), int(player_y + player_size + 1))) == purple:
        is_jumping = False
        jump_count = 10
    else:
        player_y += 5
    player_y -= 1
 # Fill the screen with white

    screen.fill(white)

    # Draw the player
    pygame.draw.rect(screen, black, (player_x - 5, player_y - 5, player_size + 10,player_size + 10))
    pygame.draw.rect(screen, red, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, torquise, (player_x + player_size // 10, player_y + player_size // 10, player_size // 5, player_size // 5))
    pygame.draw.rect(screen, torquise, (player_x + 35, player_y + player_size // 10, player_size // 5, player_size // 5))
    pygame.draw.rect(screen, black, (player_x + 15, player_y + 25, player_size // 2.5, player_size // 5))
    
    pygame.draw.rect(screen, purple, (250, 500, 100, 50))
    pygame.draw.rect(screen, purple, (0, 700, 1200, 500))
    
    # Update the display

    pygame.display.flip()

    # Set the frames per second
    pygame.time.Clock().tick(30)

