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
# Shelve + highscore help: https://stackoverflow.com/questions/16726354/saving-the-highscore-for-a-game

import pygame, sys, random, math, serial, shelve
from pygame.locals import *

WIDTH = 800
HEIGHT = 800
FPS = 60
LIVES = 5
timeAlive = 0
score = 0
freeze_score = False
final_score = 0

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
arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

#highscore stuff
with shelve.open('game_data') as db:
    highscore = int(db.get('highscore', 0))


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (50, 75))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 10
        self.move_left = False
        self.move_right = False

    def update(self):
        while arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == "LEFT":
                self.move_left = True
                self.move_right = False
            elif line == "RIGHT":
                self.move_left = False
                self.move_right = True
            elif line == "Forward":  
                self.move_left = False
                self.move_right = False
        self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))
        if self.move_left:
            self.rect.x -= self.speedx
        if self.move_right:
            self.rect.x += self.speedx

        if self.move_left:
            playerImage = pygame.image.load('spaceshipleft.png')
            self.image = pygame.transform.scale(playerImage, (60, 60))
        elif self.move_right:
            playerImage = pygame.image.load('spaceshipright.png')
            self.image = pygame.transform.scale(playerImage, (60, 60))
        else:
            playerImage = pygame.image.load('spaceship_up.png')
            self.image = pygame.transform.scale(playerImage, (50, 75))

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
        # self.rotate_speed = random.randrange(-8,8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
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
clang_sound = pygame.mixer.Sound('softclang.wav')
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
for i in range(8):
    c = Comet()
    all_sprites.add(c)
    comets.add(c)
for i in range(1):
    b = Bone()
    all_sprites.add(b)
    bones.add(b)
for i in range(5):
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)


# State stuff 
STATE_START = 0
STATE_GAME = 1
STATE_END = 2
current_state = STATE_START

pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0)
musicPlaying = True

font1 = pygame.font.SysFont(None, 36)
font2 = pygame.font.SysFont(None, 18)

# game loop
running = True
start_time = pygame.time.get_ticks()
while running:
    elapsed_time = (pygame.time.get_ticks() - start_time) / 10  
    score = int(elapsed_time)
    clock.tick(FPS)
    if current_state == STATE_START:
        while arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == "UP":
                current_state = STATE_GAME

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        y1 += 4
        y2 += 4
        if y1 >= background_height:
            y1 = -background_height
        if y2 >= background_height:
            y2 = -background_height

        screen.blit(background, (0, y1))
        screen.blit(background, (0, y2))
        start_ship = pygame.transform.scale(player_image, (200, 200))
        start_ship_rect = start_ship.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(start_ship, (300, 600))
        start_font = pygame.font.SysFont(None, 27)
        start_text_lines = [
            "Welcome to Cosmic Canine!",
            "Help Luna the space pup navigate through the treacherous galaxy!",
            "Tilt your physical space ship LEFT and RIGHT to control Luna on screen.",
            "Colliding with asteroids and comets takes away lives. Collecting bones gives you lives.",
            "Beware! the longer you survive, more comets will come your way.",
            "Point the spaceship UP to start"
        ]
        y_start = (HEIGHT - sum([start_font.size(line)[1] for line in start_text_lines])) // 2
        for i, line in enumerate(start_text_lines):
            rendered_text = start_font.render(line, True, WHITE)
            text_rect = rendered_text.get_rect(center=(WIDTH // 2, y_start + i * 50))
            screen.blit(rendered_text, text_rect)
        pygame.display.update()

    elif current_state == STATE_GAME:
        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.powerup()


        if LIVES > 0:
            timeAlive += 1
            score = int(elapsed_time)

        if LIVES <= 0:
            freeze_score = True  # Stop the score from updating  # Capture the final score at this point
            current_state = STATE_END

        if not freeze_score:
            current_ticks = pygame.time.get_ticks()
            final_score = int((current_ticks - start_time) / 10)  # Score is time in seconds


        # Progressivly harder as you survive     
        if timeAlive % 500 == 0:
            for i in range(1):  
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
            current_state = STATE_END

        y1 += 4
        y2 += 4

        if y1 >= background_height:
            y1 = -background_height
        if y2 >= background_height:
            y2 = -background_height

        screen.blit(background, (0, y1))
        screen.blit(background, (0, y2))

        all_sprites.draw(screen)

        lives_text = font1.render("Lives: " + str(LIVES), True, WHITE)
        screen.blit(lives_text, (10, 10))

        font = pygame.font.SysFont(None, 36)    
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (600, 10))


        pygame.display.update()

    elif current_state == STATE_END:
        with shelve.open('game_data', writeback=True) as db:
            if final_score > db.get('highscore', 0):
                db['highscore'] = final_score
                highscore = final_score
        while arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == "UP":
                current_state = STATE_START
                LIVES = 5
                timeAlive = 0
                score = 0
                final_score = 0
                start_time = pygame.time.get_ticks()
                current_ticks = 0
                freeze_score=False
                elapsed_time = 0

                # Reinitialize sprites for a new game
                all_sprites = pygame.sprite.Group()
                comets = pygame.sprite.Group()
                bones = pygame.sprite.Group()
                asteroids = pygame.sprite.Group()
                player = Player()
                all_sprites.add(player)
                for _ in range(12):
                    c = Comet()
                    all_sprites.add(c)
                    comets.add(c)
                for _ in range(1):
                    b = Bone()
                    all_sprites.add(b)
                    bones.add(b)
                for _ in range(5):
                    a = Asteroid()
                    all_sprites.add(a)
                    asteroids.add(a)

                y1 = 0
                y2 = background_height

                pygame.mixer.music.play(-1, 0.0)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        y1 += 4
        y2 += 4
        if y1 >= background_height:
            y1 = -background_height
        if y2 >= background_height:
            y2 = -background_height

        screen.blit(background, (0, y1))
        screen.blit(background, (0, y2))

        end_font = pygame.font.SysFont(None, 40)
        end_text_lines = [
            "Game Over!",
            f"Final Score: {final_score}",
            f"High Score: {highscore}",
            "Point the spaceship UP to restart."
        ]
        y_start = (HEIGHT - sum([end_font.size(line)[1] for line in end_text_lines])) // 2
        for i, line in enumerate(end_text_lines):
            rendered_text = end_font.render(line, True, WHITE)
            text_rect = rendered_text.get_rect(center=(WIDTH // 2, y_start + i * 50))
            screen.blit(rendered_text, text_rect)

        pygame.display.update()

pygame.quit()