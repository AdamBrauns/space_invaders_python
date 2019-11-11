import pygame

# Initialize the pygame
pygame.init()

# Create the screen with width and height
screen = pygame.display.set_mode((800, 600))

# Create title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Player image
playerImg = pygame.image.load('images/player2.png')
playerX = 370
playerY = 480

def player():
    # Blit is used to draw on screen
    screen.blit(playerImg, (playerX, playerY))

# Game Loop
running = True
while True:
    # RGB - Red, Green, Blue (goes up to 255)
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    pygame.display.update()