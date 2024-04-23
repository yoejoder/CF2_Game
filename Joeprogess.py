# import pygame
# import sys

# pygame.init()

# screen_width = 800
# screen_height = 750
# screen = pygame.display.set_mode((screen_width, screen_height))

# background = pygame.image.load('space.jpg')
# background = pygame.transform.scale(background, (screen_width, screen_height * 2))
# background_height = background.get_height()

# y1 = 0
# y2 = background_height

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     y1 += 2 
#     y2 += 2

#     if y1 >= background_height:
#         y1 = -background_height
#     if y2 >= background_height:
#         y2 = -background_height

#     screen.blit(background, (0, y1))
#     screen.blit(background, (0, y2))

#     pygame.display.flip()
#     pygame.time.Clock().tick(60)


# # space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# # spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE


import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 400, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Flappy Bird with Shapes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Game variables
bird_x = 50
bird_y = 300
bird_width = 30
bird_height = 30
bird_y_change = 0

gravity = 0.5
jump_height = -10
ground_height = SCREEN_HEIGHT - 70
score = 0

# Obstacle variables
obstacle_width = 70
obstacle_height = random.randint(150, 400)
obstacle_color = GREEN
obstacle_speed = 2
obstacle_gap = 200
obstacle_list = []
obstacle_frequency = 1500  # milliseconds
last_obstacle = pygame.time.get_ticks()

# Font for score
font = pygame.font.Font(None, 36)

def draw_bird(bird_y):
    pygame.draw.rect(screen, RED, (bird_x, bird_y, bird_width, bird_height))

def draw_obstacles(obstacles):
    for obstacle in obstacles:
        pygame.draw.rect(screen, obstacle_color, obstacle[0])
        pygame.draw.rect(screen, obstacle_color, obstacle[1])

def create_obstacle():
    obstacle_height = random.randint(200, 400)
    bottom_obstacle = pygame.Rect(SCREEN_WIDTH, ground_height - obstacle_height, obstacle_width, obstacle_height)
    top_obstacle = pygame.Rect(SCREEN_WIDTH, 0, obstacle_width, ground_height - obstacle_height - obstacle_gap)
    return (bottom_obstacle, top_obstacle)

def move_obstacles(obstacles):
    for obstacle in obstacles:
        obstacle[0].x -= obstacle_speed
        obstacle[1].x -= obstacle_speed
    obstacles = [obstacle for obstacle in obstacles if obstacle[0].x > -obstacle_width]
    return obstacles

def check_collision(obstacles):
    for obstacle in obstacles:
        if bird_rect.colliderect(obstacle[0]) or bird_rect.colliderect(obstacle[1]):
            return True
    return False

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_y_change = jump_height

    # Bird movement
    bird_y_change += gravity
    bird_y += bird_y_change
    bird_rect = pygame.Rect(bird_x, bird_y, bird_width, bird_height)

    # Ground collision
    if bird_y + bird_height > ground_height:
        bird_y = ground_height - bird_height
        bird_y_change = 0

    # Create new obstacles
    time_now = pygame.time.get_ticks()
    if time_now - last_obstacle > obstacle_frequency:
        obstacle_list.append(create_obstacle())
        last_obstacle = time_now

    # Draw bird
    draw_bird(bird_y)

    # Move and draw obstacles
    obstacle_list = move_obstacles(obstacle_list)
    draw_obstacles(obstacle_list)

    # Check for collisions
    if check_collision(obstacle_list):
        running = False

    # Display score
    score_display = font.render(str(score), True, BLACK)
    screen.blit(score_display, (SCREEN_WIDTH // 2, 50))

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(30)

# Quit Pygame
pygame.quit()
sys.exit()
