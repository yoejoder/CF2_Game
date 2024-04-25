# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# galaxy image source: https://www.peakpx.com/en/hd-wallpaper-desktop-awntk 
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
# comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
# background music link: https://www.youtube.com/watch?v=fnOv8MvTukQ

import pygame, sys, random, math
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()
FPS = 60
WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("SpaceFlee")

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (WIDTH + 50, HEIGHT))
background_height = background.get_height()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
y1 = 0
y2 = background_height

numberComet = 0
CometCounter = 0
NEWCOMET = 500
COMETSIZE = 90

player = pygame.Rect(WIDTH/2, HEIGHT - 100, 50, 50)
playerImage = pygame.image.load('spaceship.png')
playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
cometImage = pygame.image.load('comet.png')
comet_height = cometImage.get_height()

Comets = []
for i in range(numberComet):
    Comets.append(pygame.Rect(random.randint(0, WIDTH - COMETSIZE), random.randint(0, HEIGHT - COMETSIZE), COMETSIZE, COMETSIZE))

# Movement Variables
moveLeft = False
moveRight = False
CometDown = True


MOVESPEED = 5
lives = 5

pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

font = pygame.font.SysFont(None, 36)

# Running the game loop
while True:
    mainClock.tick(FPS)
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
            # if event.key == K_x:
                # player.top = random.randint(0,HEIGHT - player.height)
                # player.left = random.randint(0, WIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            Comets.append(pygame.Rect(event.pos[0], event.pos[1], COMETSIZE, COMETSIZE))

    CometCounter += 1
    if CometCounter >= NEWCOMET:
        CometCounter = 0
        Comets.append(pygame.Rect(random.randint(0, WIDTH - COMETSIZE), 0 - COMETSIZE*0.5, COMETSIZE, COMETSIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    

    y1 += 5
    y2 += 5


    if y1 >= background_height:
        # y1 = -comet_height
        y1 = -background_height
    if y2 >= background_height:
        # y2 = -comet_height
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))
    # screen.blit(cometImage, (0, y1))
    # screen.blit(cometImage, (0, y2))

    # Move the player
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
        playerImage = pygame.image.load('spaceshipleft.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
    elif moveRight and player.right < WIDTH:
        player.right += MOVESPEED
        playerImage = pygame.image.load('spaceshipright.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
    else:
        playerImage = pygame.image.load('spaceship.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (40, 70))

    # draw the Comet
    for Comet in Comets[:]:
        if player.colliderect(Comet):
            Comets.remove(Comet)
            lives -= 1
        screen.blit(pygame.transform.scale(cometImage, (COMETSIZE, COMETSIZE-10)), Comet)

    screen.blit(playerStretchedImage, player)

    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(lives_text, (10, 10))
    
    if lives == 0:
        pygame.quit()
        sys.exit()

    pygame.display.update()
