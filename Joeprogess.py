'''
SOURCES:
space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
galaxy image source: https://www.peakpx.com/en/hd-wallpaper-desktop-awntk 
spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
background music link: https://www.youtube.com/watch?v=fnOv8MvTukQ
arduino + python help: https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756
3d Rocket Model: https://www.myminifactory.com/object/3d-print-gcreate-official-rocket-ship-55463
'''
import pygame
import serial #install pyserial
import sys
import random

WIDTH, HEIGHT = 800, 800
FPS = 60
LIVES = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpacePup")
clock = pygame.time.Clock()
arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

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
        if arduino.in_waiting > 0:
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
            playerImage = pygame.image.load('spaceship.png')
            self.image = pygame.transform.scale(playerImage, (50, 75))

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(comet_image, (25, 55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(4, 6)
        self.speedx = random.randrange(-2, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(4, 6)


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
            self.speedy = random.randrange(4,6)

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



background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (WIDTH + 50, HEIGHT))
background_height = background.get_height()
player_image = pygame.image.load('spaceship_up.png').convert()
comet_image = pygame.image.load('comet_up.png').convert()
bone_image = pygame.image.load('bone.png').convert()
asteroid_image = pygame.image.load('asteroid.png')


y1 = 0
y2 = background_height

score = 0

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bones = pygame.sprite.Group()
asteroids = pygame.sprite.Group()


player = Player()
all_sprites.add(player)
for i in range(10):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
for i in range(1):
    b = Bone()
    all_sprites.add(b)
    bones.add(b)
for i in range(6):
    a = Asteroid()
    all_sprites.add(a)
    asteroids.add(a)

pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont(None, 36)

running = True
start_time = pygame.time.get_ticks()

while running:
    clock.tick(FPS)

    elapsed_time = (pygame.time.get_ticks() - start_time) / 10  
    score = int(elapsed_time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            




    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        LIVES -= 1
    if LIVES <= 0:
        running = False

    bone_hits = pygame.sprite.spritecollide(player, bones, True)
    for bone in bone_hits:
        b = Bone()
        all_sprites.add(b)
        bones.add(b)
    
    if bone_hits:
        LIVES += 2

    asteroid_hits = pygame.sprite.spritecollide(player, asteroids, True)
    for asteroid in asteroid_hits:
        a = Asteroid()
        all_sprites.add(a)
        asteroids.add(a)

    if asteroid_hits:
        LIVES -= 2


    all_sprites.draw(screen)
    lives_text = font.render(f"Lives: {LIVES}", True, WHITE)
    screen.blit(lives_text, (10, 10))
    pygame.display.flip()

    y1 += 5
    y2 += 5

    if y1 >= background_height:
        y1 = -background_height
    if y2 >= background_height:
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (600, 10))

print(f'Your Score: {score}')
arduino.close()
pygame.quit()
sys.exit()
