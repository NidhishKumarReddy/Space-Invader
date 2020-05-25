import pygame

# Initialize the pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Game Running function
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # RGB
    screen.fill((0, 0, 0))
    pygame.display.update()