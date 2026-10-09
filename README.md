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

#snake
block_size = 20

snake_body = [
    [300, 200]
    [280, 200]
    [260, 200]
]

game_is_underway = True

while game_is_underway:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and change_x == 0:
                change_x = -block_size
                change_y = 0
            elif 

    


#green background
window.fill(green)

#draw snake
for block in snake_body:
    pygame.draw.rect(window, black, [block[1],block_size, block_size])


#display update
pygame.display.update()
