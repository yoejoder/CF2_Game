import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

WINDOWWIDTH = 800
WINDOWHEIGHT = 800
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Collision Game")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

numberFood = 20

foodCounter = 0
NEWFOOD = 300
FOODSIZE = 40

player = pygame.Rect(300, 700, 50, 50)
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
score = 0
lives = 3

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

    windowSurface.fill(BLACK)

    # Move the player
    # if moveDown and player.bottom < WINDOWHEIGHT:
    #     player.top += MOVESPEED
    # if moveUp and player.top > 0:
    #     player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # Draw the food
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            score -= 1
        windowSurface.blit(pygame.transform.scale(cometImage, (FOODSIZE, FOODSIZE-10)), food)

    windowSurface.blit(playerStretchedImage, player)

    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    windowSurface.blit(lives_text, (10, 10))

    # collision detection
    for food in foods:
        if player.colliderect(food):
            foods.remove(food)
            lives -= 1
            if lives == 0:
                lives = 3
                score = 0

    pygame.display.update()
