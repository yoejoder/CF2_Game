import pygame
import serial
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Accelerometer")


arduino = serial.Serial('/dev/cu.usbserial-110', 9600)

square_size = 50
square_x = WIDTH // 2 - square_size // 2
square_y = HEIGHT // 2 - square_size // 2
square_speed = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    if arduino.in_waiting > 0:
        line = arduino.readline().decode('utf-8').strip()
        if line == "LEFT":
            square_x -= square_speed
        elif line == "RIGHT":
            square_x += square_speed

    square_x = max(0, min(WIDTH - square_size, square_x))

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (square_x, square_y, square_size, square_size))

    pygame.display.flip()


arduino.close()
pygame.quit()
sys.exit()
