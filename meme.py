# SOURCES
# arduino + python help: https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756
# 3d Rocket Model: https://www.myminifactory.com/object/3d-print-gcreate-official-rocket-ship-55463
# galaxy image source: https://www.peakpx.com/en/hd-wallpaper-desktop-awntk 
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
# comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
# background music link: https://www.youtube.com/watch?v=fnOv8MvTukQ
# asteroid image source: https://www.cleanpng.com/png-planet-cartoon-green-moon-466868/ 
# dog bone image: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.freepik.com%2Fpremium-vector%2Ftoy-bone-icon-chewing-puppy-treat-symbol_34264712.htm&psig=AOvVaw08b2UQ-5aNgRRAzTd7OiFH&ust=1713572817492000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCND3h7CCzYUDFQAAAAAdAAAAABAE
# dog head image: https://www.google.com/imgres?imgurl=https%3A%2F%2Fthumbs.dreamstime.com%2Fz%2Fshiba-inu-puppy-face-set-cute-cartoon-icon-logo-happy-dog-tongue-sticking-out-simple-vector-illustration-128772666.jpg&tbnid=dfbviOVtMiBMMM&vet=10CBwQxiAoBGoXChMI8Jj2hbLbhQMVAAAAAB0AAAAAEAc..i&imgrefurl=https%3A%2F%2Fwww.dreamstime.com%2Fshiba-inu-puppy-face-set-cute-cartoon-icon-logo-happy-dog-tongue-sticking-out-simple-vector-illustration-image128772666&docid=a6ygET3GYbyWxM&w=1600&h=1690&itg=1&q=brown%20shiba%20inu%20clip%20art&ved=0CBwQxiAoBGoXChMI8Jj2hbLbhQMVAAAAAB0AAAAAEAc
# comet hit sound effect: https://www.youtube.com/watch?v=wOh41654QFg
# asteroid hit sound effect: https://www.youtube.com/watch?v=h3cZFqppGRE
# bone pickup sound effect: https://www.youtube.com/watch?v=iJe4k2AMOk4

import pygame, sys, random, math
from pygame.locals import *

WIDTH = 800
HEIGHT = 800
FPS = 60
LIVES = 900
timeAlive = 0

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
pygame.display.set_caption("Cosmic Canine")
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
            player_image = pygame.image.load('spaceshipleft.png')
            self.image = pygame.transform.scale(player_image, (40, 40))
        elif keystate[pygame.K_RIGHT]:
            self.speedx = 5
            player_image = pygame.image.load('spaceshipright.png')
            self.image = pygame.transform.scale(player_image, (40, 40))
        else:
            player_image = pygame.image.load('spaceship_up.png')
            self.image = pygame.transform.scale(player_image, (30, 55))
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
        self.speedy = random.randrange(5,6)
        self.speedx = random.randrange(-2,3)
    
    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(5,6)
            self.speedx = random.randrange(-2,3)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = pygame.transform.scale(asteroid_image, (100,95))
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85 / 2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(2,4)
        self.speedx = random.randrange(-1,2)
        self.rot = 0
        self.rotate_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    # def rotate(self):
        # present = pygame.time.get_ticks()
         #if present - self.last_update > 50:
            # self.last_update = present
            # self.rot = (self.rot + self.rotate_speed) % 360
            # new_image = pygame.transform.rotate(self.image_orig, self.rot)
            # old_center = self.rect.center
            # self.image = new_image
            # self.rect = self.image.get_rect()
            # self.rect.center = old_center

    def update(self):
        # self.rotate()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 100 or self.rect.left < -100 or self.rect.right > WIDTH + 100:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-200,-100)
            self.speedy = random.randrange(2,4)
            self.speedx = random.randrange(-1,2)

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
        if self.rect.top > HEIGHT + 25 or self.rect.left < -25 or self.rect.right > WIDTH + 25:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100,-40)
            self.speedy = random.randrange(1,2)

# load all game sounds
hit_sound = pygame.mixer.Sound('hit.wav')
clang_sound = pygame.mixer.Sound('clang.wav')
# for VERY LOUD CLANGS load 'clang.wav' (funny)
bone_sound =  pygame.mixer.Sound('bone.wav')
hit_sound.set_volume(.5)
clang_sound.set_volume(1)
bone_sound.set_volume(1)

# load all game graphics
background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (WIDTH + 50, HEIGHT))
background_height = background.get_height()
player_image = pygame.image.load('spaceship_up.png')
comet_image = pygame.image.load('comet.png')
bone_image = pygame.image.load('bone.png')
asteroid_image = pygame.image.load('asteroid.png').convert_alpha()

y1 = 0
y2 = background_height

all_sprites = pygame.sprite.Group()
comets = pygame.sprite.Group()
bones = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(12):
    c = Comet()
    all_sprites.add(c)
    comets.add(c)
for i in range(1):
    b = Bone()
    all_sprites.add(b)
    bones.add(b)
for i in range(60):
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)


pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

font = pygame.font.SysFont(None, 36)

# game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    timeAlive += 1
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.powerup()

    if timeAlive % 500 == 0:
        for i in range(2):  
            c = Comet()
            all_sprites.add(c)
            comets.add(c)

    # update
    all_sprites.update()

    asteroid_comet_hits = pygame.sprite.groupcollide(asteroids, comets, False, True, pygame.sprite.collide_circle)
    for asteroid_comet in asteroid_comet_hits:
        c = Comet()
        all_sprites.add(c)
        comets.add(c)

    asteroid_hits = pygame.sprite.spritecollide(player, asteroids, True, pygame.sprite.collide_circle)
    for asteroid in asteroid_hits:
        clang_sound.play()
        a = Asteroid()
        all_sprites.add(a)
        asteroids.add(a)

    if asteroid_hits:
        LIVES -= 2


    bone_hits = pygame.sprite.spritecollide(player, bones, True)
    for bone in bone_hits:
        bone_sound.play()
        b = Bone()
        all_sprites.add(b)
        bones.add(b)
    
    if bone_hits:
        LIVES += 2


    # check to see if a comet hit the player
    comet_hits = pygame.sprite.spritecollide(player, comets, True)
    for comet in comet_hits:
        hit_sound.play()
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