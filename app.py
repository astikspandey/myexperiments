
import pygame
from pygame.locals import *

pygame.init()

##################Load Window##################
pygame.image.load("safeimagekit-pixel-art.png")
windowsSize = pygame.display.set_mode((800,600)) 
pygame.display.set_caption("Hello Astik")


##################Defining Font attributes##################
myFont = pygame.font.SysFont("Segoe UI", 90)
helloWorld = myFont.render("Hello World", 1, (255, 0, 255))



