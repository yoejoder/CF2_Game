# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
#

import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Collision Game")

background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (WINDOWWIDTH + 50, WINDOWHEIGHT))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

numberFood = 10
foodCounter = 0
NEWFOOD = 400
FOODSIZE = 50

player = pygame.Rect(WINDOWWIDTH/2, WINDOWHEIGHT - 100, 50, 50)
playerImage = pygame.image.load('spaceship.png')
playerStretchedImage = pygame.transform.scale(playerImage, (40, 40))
cometImage = pygame.image.load('comet.png')

foods = []
for i in range(numberFood):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),
                             FOODSIZE, FOODSIZE))

# Movement Variables
moveLeft = False
moveRight = False
# moveUp = False
# moveDown = False

MOVESPEED = 1
lives = 5

font = pygame.font.SysFont(None, 36)

# Running the game loop
while True:
    # Checking for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = True
                moveLeft = False
            # if event.key == K_UP or event.key == K_w:
            #     moveDown = False
            #     moveUp = True
            # if event.key == K_DOWN or event.key == K_s:
            #     moveDown = True
            #     moveUp = False
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            # if event.key == K_UP or event.key == K_w:
            #     moveUp = False
            # if event.key == K_DOWN or event.key == K_s:
            #     moveDown = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_x:
                player.top = random.randint(0,WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE),
                                 FOODSIZE, FOODSIZE))

    windowSurface.blit(background, (0, 0))

    # Move the player
    # if moveDown and player.bottom < WINDOWHEIGHT:
    #     player.top += MOVESPEED
    # if moveUp and player.top > 0:
    #     player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # draw the food
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            lives -= 1
        windowSurface.blit(pygame.transform.scale(cometImage, (FOODSIZE, FOODSIZE-10)), food)

    windowSurface.blit(playerStretchedImage, player)

    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    windowSurface.blit(lives_text, (10, 10))

    pygame.display.update()
