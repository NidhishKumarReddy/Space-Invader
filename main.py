import pygame
import random
import math

# Initialize the pygame
pygame.init()

# Create Screen
screen = pygame.display.set_mode((800,600))

# Background
background = pygame.image.load('background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

score = 0
# Player
playerImg = pygame.image.load('spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))

# Alien
alienImg = pygame.image.load('alien.png')
alienX = random.randint(0, 735)
alienY = random.randint(50, 150)
alienX_change = 4
alienY_change = 40

def alien(x, y):
    screen.blit(alienImg, (x, y))

# Bullet
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(alienX, alienY, bulletX, bulletY):
    distance = math.sqrt((math.pow(alienX - bulletX, 2)) + (math.pow(alienY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Game Running function
running = True
while running:
    
    # RGB
    screen.fill((0, 0, 0))

    # Background
    screen.blit(background,(0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its rigth or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    
    # Checking for boundaries of spaceship so it doesn't go out of window
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Alien Movement
    alienX += alienX_change

    if alienX <= 0:
        alienX_change = 4
        alienY += alienY_change
    elif alienX >= 736:
        alienX_change = -4
        alienY += alienY_change

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Collision
    collision = isCollision(alienX, alienY, bulletX, bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        alienX = random.randint(0, 735)
        alienY = random.randint(50, 150)
    
    player(playerX, playerY)
    alien(alienX, alienY)

    pygame.display.update()
