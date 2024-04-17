import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 750
screen = pygame.display.set_mode((screen_width, screen_height))

background = pygame.image.load('space.jpg')
background = pygame.transform.scale(background, (screen_width, screen_height * 2))
background_height = background.get_height()

y1 = 0
y2 = background_height

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    y1 += 2 
    y2 += 2

    if y1 >= background_height:
        y1 = -background_height
    if y2 >= background_height:
        y2 = -background_height

    screen.blit(background, (0, y1))
    screen.blit(background, (0, y2))

    pygame.display.flip()
    pygame.time.Clock().tick(60)


# space image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fspace%2520background%2F&psig=AOvVaw3J25w2RRPNARpyiLT2cJOu&ust=1713304119399000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCPDPh62ZxYUDFQAAAAAdAAAAABAE
# spaceship image source: https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.istockphoto.com%2Fillustrations%2Fspaceship&psig=AOvVaw2vckoaUA3y9-mDd2MJoRlV&ust=1713304202156000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCOi2tNSZxYUDFQAAAAAdAAAAABAE


