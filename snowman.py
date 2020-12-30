import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((600,600),0,32)

SKY = (135, 206, 235)
WHITE = (255, 255, 255)

DISPLAY.fill(SKY)

while True:
    pygame.draw.circle(DISPLAY, WHITE, (200, 350), 50)
    pygame.draw.circle(DISPLAY, WHITE, (200, 500), 100)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()