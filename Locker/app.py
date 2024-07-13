
import pygame
from pygame.locals import *

pygame.init()

### Size of the game ### 

windowsSize = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Hello Astik")


#defining font attributes
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("Hello World", 1, (255, 0, 255))



