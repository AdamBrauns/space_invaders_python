import pygame
import random

# Initialize the pygame
pygame.init()

# Create the screen with width and height
screen = pygame.display.set_mode((800, 600))

# Background 
background = pygame.image.load('images/background.png')

# Create title and icon
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('images/ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/player2.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('images/enemy.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 4
enemyY_change = 40

def player(x, y):
    # Blit is used to draw on screen
    screen.blit(playerImg, (x, y))

def enemy(x, y):
    # Blit is used to draw on screen
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while True:
    # RGB - Red, Green, Blue (goes up to 255)
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking the boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 736 comes from 800 - 64 (player width)
        playerX = 736

    enemyX += enemyX_change
    
    if enemyX <= 0:
        enemyX_change = abs(enemyX_change)
        enemyY += enemyY_change
    elif enemyX >= 736: # 736 comes from 800 - 64 (player width)
        enemyX_change = -1 * abs(enemyX_change)
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()