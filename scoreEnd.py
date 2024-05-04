import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Score Freezing Example")

# Set up the clock for controlling the frame rate
clock = pygame.time.Clock()

# Colors and font
white = (255, 255, 255)
black = (0, 0, 0)
font = pygame.font.Font(None, 72)  # Default font and size

# Game variables
running = True
score = 0
freeze_score = False
start_ticks = pygame.time.get_ticks()  # Start tick for calculating the score

# Game loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                freeze_score = True  # Freeze the score when space bar is pressed

    # Calculate score based on time if not frozen
    if not freeze_score:
        current_ticks = pygame.time.get_ticks()
        score = (current_ticks - start_ticks) // 10  # Score is time in seconds

    # Fill the screen with black
    screen.fill(black)

    # Render the score and display it
    score_text = font.render(f"Score: {score}", True, white)
    score_rect = score_text.get_rect(center=(width // 2, height // 2))
    screen.blit(score_text, score_rect)

    # Update the display
    pygame.display.update()

    # Cap the frame rate
    clock.tick(60)

pygame.quit()
sys.exit()
