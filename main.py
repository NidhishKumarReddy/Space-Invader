import pygame
import random

# Initialize the pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Alien
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0, 736)
alienY = random.randint(50, 150)
alienX_change = 0

def alien(x, y):
    screen.blit(alienImg, (x, y))

# Game Running function
running = True
while running:
    
    # RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #if keystroke is pressed check whether its rigth or left
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
    elif playerX >= 736:
        playerX = 736

    player(playerX, playerY)
    alien(alienX, alienY)
    pygame.display.update()
