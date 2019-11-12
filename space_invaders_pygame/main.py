import pygame
import random
import math
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen with width and height
screen = pygame.display.set_mode((800, 600))

# Background 
background = pygame.image.load('images/background.png')

# Background sound
mixer.music.load('sounds/background.wav')
mixer.music.play(-1) # The param -1 will play it on loop

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
enemyImg = []
enemyX = []
enemyY =[]
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(4)
    enemyY_change.append(40)

# Bullet
bulletImg = pygame.image.load('images/bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
# 'ready' - You can't see the bullet on the screen
# 'fire' - The bullet is currently moving
bulletState = 'ready' 

# Score 
score_value = 0
# pygame only has one free font (freesansbold)
# dafont.com has fonts to download for free
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

# Game Over text
game_over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score = font.render(f'Score: {score_value}', True, (255, 255, 255))
    screen.blit(score, (x, y))    

def game_over_text():
    over_text = game_over_font.render(f'Game Over', True, (255, 255, 255))
    screen.blit(over_text, (225, 250))

def player(x, y):
    # Blit is used to draw on screen
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    # Blit is used to draw on screen
    screen.blit(enemyImg[i], (x, y))

def fire_bullet(x, y):
    global bulletState
    # Blit is used to draw on screen
    bulletState = 'fire'
    screen.blit(bulletImg, (x + 16, y + 10)) # Fire from the middle of the space ship 

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    # 27 was decided by trial and error
    if distance < 27:
        return True
    return False

# Game Loop
running = True
while running:
    # RGB - Red, Green, Blue (goes up to 255)
    screen.fill((0, 0, 0))

    # Background image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

        # If keystroke is pressed check if it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bulletState is 'ready':
                    bullet_sound = mixer.Sound('sounds/laser.wav')
                    bullet_sound.play()
                    # Get the current x cord of the player
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Checking the boundaries of spaceship so it doesn't go out of bounds
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: # 736 comes from 800 - 64 (player width)
        playerX = 736

    # Enemy movement
    for i in range(num_of_enemies):

        # Game Over
        if enemyY[i] > 400: 
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
    
        if enemyX[i] <= 0:
            enemyX_change[i] = abs(enemyX_change[i])
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736: # 736 comes from 800 - 64 (player width)
            enemyX_change[i] = -1 * abs(enemyX_change[i])
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('sounds/explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bulletState = 'ready'
            score_value += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
    
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bulletState = 'ready'
    if bulletState is 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()