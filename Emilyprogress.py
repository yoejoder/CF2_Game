# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
# comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
# dog bone image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Ftoy-bone-icon-chewing-puppy-treat-symbol_34264712.htm&psig=AOvVaw08b2UQ-5aNgRRAzTd7OiFH&ust=1713572817492000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCND3h7CCzYUDFQAAAAAdAAAAABAE

import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Collision Game")

background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (screen_width + 50, screen_height))
background_height = background.get_height()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
y1 = 0
y2 = background_height

numberFood = 4
foodCounter = 0
NEWFOOD = 500
FOODSIZE = 90

boneImage = pygame.image.load('bone.png')
boneImage = pygame.transform.scale(boneImage, (100, 50))

player = pygame.Rect(screen_width/2, screen_height - 100, 50, 50)
playerImage = pygame.image.load('spaceship.png')
playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
cometImage = pygame.image.load('comet.png')

foods = []
for i in range(numberFood):
    foods.append(pygame.Rect(random.randint(0, screen_width - FOODSIZE), random.randint(0, screen_height - FOODSIZE),
                             FOODSIZE, FOODSIZE))

moveLeft = False
moveRight = False

MOVESPEED = 1
lives = 5

font = pygame.font.SysFont(None, 36)

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
        if event.type == KEYUP:
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_x:
                player.top = random.randint(0,screen_height - player.height)
                player.left = random.randint(0, screen_width - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, screen_width - FOODSIZE), random.randint(0, screen_height - FOODSIZE),
                                 FOODSIZE, FOODSIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y1 += 2 
    y2 += 2

    if y1 >= background_height:
        y1 = -background_height
    if y2 >= background_height:
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))

    # Move the player
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < screen_width:
        player.right += MOVESPEED

    # draw the food
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)
            lives -= 1
        screen.blit(pygame.transform.scale(cometImage, (FOODSIZE, FOODSIZE-10)), food)

    screen.blit(playerStretchedImage, player)
    screen.blit(boneImage, (400, 400))

    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(lives_text, (10, 10))

    pygame.display.update()
