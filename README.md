import pygame
import random
import sys

pygame.init()

#establish height and width
width = 600
height = 400
window = pygame.display.set.mode((width,height))

#establish colors

black = (0,0,0)
green = (0,255,0)
red = (225,0,0)

game_is_underway = True

while game_is_underway:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#green background

window.fill(green)

#display update
pygame.display.update
