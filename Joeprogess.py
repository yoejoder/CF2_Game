'''
SOURCES:
space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
galaxy image source: https://www.peakpx.com/en/hd-wallpaper-desktop-awntk 
spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE
comet image link: https://www.google.com/url?sa=i&url=https%3A%2F%2Fm.youtube.com%2Fwatch%3Fv%3DmbZfhJeNx7c&psig=AOvVaw2X7D_DW_XsBBgWmRc-EYCy&ust=1713461913505000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCPj_nJflyYUDFQAAAAAdAAAAABAE
background music link: https://www.youtube.com/watch?v=fnOv8MvTukQ
arduino + python help: https://projecthub.arduino.cc/ansh2919/serial-communication-between-python-and-arduino-663756

'''
import pygame
import serial
import sys
import random

WIDTH, HEIGHT = 800, 800
FPS = 60
LIVES = 5
WHITE = (255, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SpaceFlee")
clock = pygame.time.Clock()
arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(player_image, (30, 55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 50

    def update(self):
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line == "LEFT":
                self.rect.x -= self.speedx
            elif line == "RIGHT":
                self.rect.x += self.speedx
            self.rect.x = max(0, min(WIDTH - self.rect.width, self.rect.x))

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(comet_image, (25, 55))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)

background = pygame.image.load('galaxy.jpg')
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
player_image = pygame.image.load('spaceship_up.png').convert()
comet_image = pygame.image.load('comet_up.png').convert()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)

pygame.mixer.music.load('the-moon.wav')
pygame.mixer.music.play(-1)

font = pygame.font.SysFont(None, 36)

running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        LIVES -= 1
        if LIVES == 0:
            running = False

    screen.fill(WHITE)
    screen.blit(background, (0, 0))
    all_sprites.draw(screen)
    lives_text = font.render(f"Lives: {LIVES}", True, WHITE)
    screen.blit(lives_text, (10, 10))
    pygame.display.flip()

arduino.close()
pygame.quit()
sys.exit()
