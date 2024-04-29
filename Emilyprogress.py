# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
# comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
# dog bone image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Ftoy-bone-icon-chewing-puppy-treat-symbol_34264712.htm&psig=AOvVaw08b2UQ-5aNgRRAzTd7OiFH&ust=1713572817492000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCND3h7CCzYUDFQAAAAAdAAAAABAE
# dog head image: https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fz%2Fshiba-inu-puppy-face-set-cute-cartoon-icon-logo-happy-dog-tongue-sticking-out-simple-vector-illustration-128772666.jpg&tbnid=dfbviOVtMiBMMM&vet=10CBwQxiAoBGoXChMI8Jj2hbLbhQMVAAAAAB0AAAAAEAc..i&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Fshiba-inu-puppy-face-set-cute-cartoon-icon-logo-happy-dog-tongue-sticking-out-simple-vector-illustration-image128772666&docid=a6ygET3GYbyWxM&w=1600&h=1690&itg=1&q=brown%20shiba%20inu%20clip%20art&ved=0CBwQxiAoBGoXChMI8Jj2hbLbhQMVAAAAAB0AAAAAEAc

import pygame, sys, random
from pygame.locals import *

pygame.init()
mainClock = pygame.time.Clock()

FPS = 60
screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)
pygame.display.set_caption("Space Pup Pursuit")

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (screen_width + 50, screen_height))
background_height = background.get_height()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
y1 = 0
y2 = background_height

numberComet = 5
CometCounter = 0
NEWCOMET = 100
COMETSIZE = 90

numberBone = 3
BoneCounter = 0
NEWBONE = 170
BONESIZE = 50

boneImage = pygame.image.load('bone.png')
boneImage = pygame.transform.scale(boneImage, (100, 50))

player = pygame.Rect(screen_width/2, screen_height - 100, 50, 50)
playerImage = pygame.image.load('spaceship.png')
playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))

cometImage = pygame.image.load('comet.png')
comet_height = cometImage.get_height()

comets = []
for i in range(numberComet):
    comets.append(pygame.Rect(random.randint(0, screen_width - COMETSIZE), random.randint(0, screen_height - COMETSIZE),
                             COMETSIZE, COMETSIZE))

bones = []
for i in range(numberBone):
    bones.append(pygame.Rect(random.randint(0, screen_width - BONESIZE), random.randint(0, screen_height - BONESIZE),
                             BONESIZE, BONESIZE))

moveLeft = False
moveRight = False
CometDown = True
BoneDown = True

MOVESPEED = 5
lives = 5

pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

font = pygame.font.SysFont(None, 36)

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
            #     player.top = random.randint(0,screen_height - player.height)
            #     player.left = random.randint(0, screen_width - player.width)
        

    CometCounter += 1
    if CometCounter >= NEWCOMET:
        CometCounter = 0
        comets.append(pygame.Rect(random.randint(0, screen_width - COMETSIZE), random.randint(0, screen_height - COMETSIZE),
                                 COMETSIZE, COMETSIZE))

    BoneCounter += 1
    if BoneCounter >= NEWBONE:
        BoneCounter = 0
        bones.append(pygame.Rect(random.randint(0, screen_width - BONESIZE), random.randint(0, screen_height - BONESIZE),
                                 BONESIZE, BONESIZE))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y1 += 5 
    y2 += 5

    if y1 >= background_height:
        y1 = -background_height
    if y2 >= background_height:
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))

    # Move the player
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
        playerImage = pygame.image.load('spaceshipleft.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
    elif moveRight and player.right < screen_width:
        player.right += MOVESPEED
        playerImage = pygame.image.load('spaceshipright.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (60, 60))
    else:
        playerImage = pygame.image.load('spaceship.png')
        playerStretchedImage = pygame.transform.scale(playerImage, (40, 70))

    # draw the comet
    for comet in comets[:]:
        if player.colliderect(comet):
            comets.remove(comet)
            lives -= 1
        screen.blit(pygame.transform.scale(cometImage, (COMETSIZE, COMETSIZE-10)), comet)

    for bone in bones[:]:
        if player.colliderect(bone):
            bones.remove(bone)
            lives += 1
        screen.blit(pygame.transform.scale(boneImage, (BONESIZE, BONESIZE-10)), bone)

    screen.blit(playerStretchedImage, player)

    lives_text = font.render("Lives: " + str(lives), True, WHITE)
    screen.blit(lives_text, (10, 10))

    if lives == 0:
        pygame.quit()
        sys.exit()

    pygame.display.update()
