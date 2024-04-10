import pygame, sys
from pygame.locals import *


pygame.init()

windowSurface = pygame.display.set_mode((500,400),0,32)
pygame.display.set_caption('Hello World!')


Black = (0,0,0)
White = (255,255,255)
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)

basicFont = pygame.font.sysFont(None,48)

text = basicFont.render('Hello World!', True, White, Blue)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

