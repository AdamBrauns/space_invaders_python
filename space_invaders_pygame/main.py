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
playerX_change = 0

def player(x, y):
    # Blit is used to draw on screen
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while True:
    # RGB - Red, Green, Blue (goes up to 255)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 736 comes from 800 - 64 (player width)
        playerX = 736

    player(playerX, playerY)
    pygame.display.update()