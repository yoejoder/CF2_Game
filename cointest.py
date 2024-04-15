import pygame
import random
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

CIRCLE_RADIUS = 20
PLAYER_SPEED = 5
point_total = 0

def random_position():
    return random.randint(CIRCLE_RADIUS, SCREEN_WIDTH - CIRCLE_RADIUS), random.randint(CIRCLE_RADIUS, SCREEN_HEIGHT - CIRCLE_RADIUS)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Coin Test")

clock = pygame.time.Clock()

player_x, player_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2

num_yellow_circles = 5
yellow_circles = [pygame.Rect(random_position(), (CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)) for _ in range(num_yellow_circles)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > CIRCLE_RADIUS:
        player_x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - CIRCLE_RADIUS:
        player_x += PLAYER_SPEED
    if keys[pygame.K_UP] and player_y > CIRCLE_RADIUS:
        player_y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_y < SCREEN_HEIGHT - CIRCLE_RADIUS:
        player_y += PLAYER_SPEED

    player_rect = pygame.Rect(player_x - CIRCLE_RADIUS, player_y - CIRCLE_RADIUS, CIRCLE_RADIUS * 2, CIRCLE_RADIUS * 2)
    for yellow_circle in yellow_circles:
        if player_rect.colliderect(yellow_circle):
            point_total += 1
            yellow_circle.topleft = random_position()

    screen.fill(BLACK)

    for yellow_circle in yellow_circles:
        pygame.draw.circle(screen, YELLOW, yellow_circle.center, CIRCLE_RADIUS)

    pygame.draw.circle(screen, WHITE, (player_x, player_y), CIRCLE_RADIUS)

    font = pygame.font.Font(None, 36)
    text_surface = font.render("Points: " + str(point_total), True, WHITE)
    screen.blit(text_surface, (10, 10))

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
