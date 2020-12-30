import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((600,600),0,32)

SKY = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139,69,19)

DISPLAY.fill(SKY)

while True:
    # Drawing the body of the snowman
    pygame.draw.circle(DISPLAY, WHITE, (200, 500), 100)
    pygame.draw.circle(DISPLAY, WHITE, (200, 350), 50)
    pygame.draw.circle(DISPLAY, WHITE, (200, 275), 25)
    
    # Drawing the hat of the snowman
    pygame.draw.line(DISPLAY, BLACK, (150, 250), (250, 250))
    pygame.draw.rect(DISPLAY, BLACK, (175, 200, 50, 50))

    # Drawing the left arm
    pygame.draw.line(DISPLAY, BROWN, (75, 275), (150, 350))
    # Drawing the right arm
    pygame.draw.line(DISPLAY, BROWN, (250, 350), (325, 275))

    # Making the program display the image until the user chooses to close it
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()