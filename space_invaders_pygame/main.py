import pygame

# Initialize the pygame
pygame.init()

# Create the screen with width and height
screen = pygame.display.set_mode((800, 600))

# Create title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("images/ufo.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False