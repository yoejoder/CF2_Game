# import pygame
# import serial
# import sys

# pygame.init()

# WIDTH, HEIGHT = 800, 600
# WHITE = (255, 255, 255)
# RED = (255, 0, 0)

# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Accelerometer")


# arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

# square_size = 50
# square_x = WIDTH // 2 - square_size // 2
# square_y = HEIGHT // 2 - square_size // 2
# square_speed = 50

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     if arduino.in_waiting > 0:
#         line = arduino.readline().decode('utf-8').strip()
#         if line == "LEFT":
#             square_x -= square_speed
#         elif line == "RIGHT":
#             square_x += square_speed

#     square_x = max(0, min(WIDTH - square_size, square_x))

#     screen.fill(WHITE)

#     pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

#     pygame.display.flip()


# arduino.close()
# pygame.quit()
# sys.exit()


import pygame
import serial
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Accelerometer")

# Initialize the serial connection
arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

# Square properties
square_size = 50
square_x = WIDTH // 2 - square_size // 2
square_y = HEIGHT // 2 - square_size // 2
square_speed = 5  # Reduce speed for smoother movement

# Movement control
move_left = False
move_right = False

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Check the serial input
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if line == "LEFT":
            move_left = True
            move_right = False
        elif line == "RIGHT":
            move_right = True
            move_left = False
        elif line == "Forward":  # Ensure to send "STOP" from Arduino when no tilt
            move_left = False
            move_right = False

    # Update square position
    if move_left:
        square_x -= square_speed
    if move_right:
        square_x += square_speed

    # Ensure square stays within window bounds
    square_x = max(0, min(WIDTH - square_size, square_x))

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))
    pygame.display.flip()

# Cleanup
arduino.close()
pygame.quit()
sys.exit()


