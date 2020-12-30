import pygame, sys
from pygame.locals import *

pygame.init()
DISPLAY = pygame.display.set_mode((600,600),0,32)

SKY = (135, 206, 235)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (139,69,19)
ORANGE = (255,153,0)

DISPLAY.fill(SKY)

while True:
    # Drawing the body of the snowman
    pygame.draw.circle(DISPLAY, WHITE, (200, 500), 100) # Draws the bottom
    pygame.draw.circle(DISPLAY, WHITE, (200, 350), 50) # Draws the stomach
    pygame.draw.circle(DISPLAY, WHITE, (200, 275), 25) # Draws the head
    
    # Drawing the hat of the snowman
    pygame.draw.line(DISPLAY, BLACK, (150, 250), (250, 250))
    pygame.draw.rect(DISPLAY, BLACK, (175, 200, 50, 50))

    # Drawing the left arm
    pygame.draw.line(DISPLAY, BROWN, (75, 275), (150, 350))
    # Drawing the right arm
    pygame.draw.line(DISPLAY, BROWN, (250, 350), (325, 275))

    # Drawing the buttons of the snowman
    pygame.draw.circle(DISPLAY, BLACK, (200, 325), 10)
    pygame.draw.circle(DISPLAY, BLACK, (200, 350), 10)
    pygame.draw.circle(DISPLAY, BLACK, (200, 375), 10)

    # Drawing the eyes of the snowman
    pygame.draw.circle(DISPLAY, BLACK, (190, 270), 5) # Left eye
    pygame.draw.circle(DISPLAY, BLACK, (210, 270), 5) # Right eye

    # Drawing the nose of the snowman
    pygame.draw.circle(DISPLAY, ORANGE, (200, 275), 7)

    # Making the program display the image until the user chooses to close it
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.image.save(DISPLAY, "snowman.jpg")
            pygame.quit()
            sys.exit()
    pygame.display.update()