# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# galaxy image source: https://www.peakpx.com/en/hd-wallpaper-desktop-awntk 
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
# comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
# background music link: https://www.youtube.com/watch?v=fnOv8MvTukQ
# asteroid image source: https://www.cleanpng.com/png-planet-cartoon-green-moon-466868/ 

import pygame, sys, random, math
from pygame.locals import *

WIDTH = 800
HEIGHT = 800
FPS = 60
LIVES = 5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceFlee")
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_image, (30,55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    # def powerup(self):
        # power = Power(self.rect.centerx, self.rect.top)


class Comet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(comet_image, (25,55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(4,6)
        self.speedx = random.randrange(-2,3)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,8)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(asteroid_image, (100,95))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(2,4)
        self.speedx = random.randrange(-1,2)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,4)

class Bone(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(bone_image, (57,25))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,2)
    
    def update(self):
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,2)



# load all game graphics
background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (WIDTH + 50, HEIGHT))
background_height = background.get_height()
player_image = pygame.image.load('spaceship_up.png').convert()
comet_image = pygame.image.load('comet_up.png').convert()
bone_image = pygame.image.load('bone.png').convert()
asteroid_image = pygame.image.load('asteroid.png')

y1 = 0
y2 = background_height

all_sprites = pygame.sprite.Group()
comets = pygame.sprite.Group()
bones = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(10):
    c = Comet()
    all_sprites.add(c)
    comets.add(c)
for i in range(1):
    b = Bone()
    all_sprites.add(b)
    bones.add(b)
for i in range(4):
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)


pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

font = pygame.font.SysFont(None, 36)

# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.powerup()

    # update
    all_sprites.update()

    asteroid_hits = pygame.sprite.spritecollide(player, asteroids, True)
    for asteroid in asteroid_hits:
        a = Asteroid()
        all_sprites.add(a)
        asteroids.add(a)

    if asteroid_hits:
        LIVES -= 2


    bone_hits = pygame.sprite.spritecollide(player, bones, True)
    for bone in bone_hits:
        b = Bone()
        all_sprites.add(b)
        bones.add(b)
    
    if bone_hits:
        LIVES += 3


    # check to see if a comet hit the player
    comet_hits = pygame.sprite.spritecollide(player, comets, True)
    for comet in comet_hits:
        c = Comet()
        all_sprites.add(c)
        comets.add(c)

    if comet_hits:
        LIVES -= 1
    if LIVES <= 0:
        running = False

    y1 += 4
    y2 += 4

    if y1 >= background_height:
        y1 = -background_height
    if y2 >= background_height:
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))

    all_sprites.draw(screen)

    lives_text = font.render("Lives: " + str(LIVES), True, WHITE)
    screen.blit(lives_text, (10, 10))

    pygame.display.update()

pygame.quit()