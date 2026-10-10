import pygame
import random
import sys

pygame.init()

pygame.display.set_caption("snake")
clock = pygame.time.Clock() #define time

#set up startdisplay

font1 = pygame.font.SysFont("arial", 50)
font2 = pygame.font.SysFont("arial", 25)
# initial state

game_state = "start"

#establish height and width
width = 600
height = 400
window = pygame.display.set_mode((width, height))

move_delay = 100
move_timer = 0

#establish colors

black = (0,0,0)
green = (0,255,0)
red = (225,0,0)

#snake
block_size = 20

snake_body = [
    [300, 200],
    [280, 200],
    [260, 200]
]

#apple 
apple_pos =[
     random.randrange(0,width, block_size),
     random.randrange(0, height, block_size),
]

change_x = block_size
change_y = 0

game_is_underway = True

while game_is_underway:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if game_state == "start":
                if event.key == pygame.K_SPACE:
                    game_state = "play"
        
            elif game_state == "play":
                if event.key == pygame.K_LEFT and change_x == 0:
                    change_x = -block_size
                    change_y = 0
                elif event.key == pygame.K_RIGHT and change_x==0:
                    change_x = block_size
                    change_y = 0
                elif event.key == pygame.K_UP and change_y == 0:
                    change_x = 0
                    change_y = -block_size
                elif event.key == pygame.K_DOWN and change_y == 0:
                    change_x = 0
                    change_y = block_size

    if game_state == "start":
        window.fill(black)
        start_text = font1.render(  #creating the start text
            "push SPACE to start", True, (255, 255, 255)
        )
        window.blit(   #position the start text
            start_text, (width//2 - start_text.get_width()//2, height//2)
        )
        controll_text= font2.render(   #creating the controll text
            "controll with arrow keys", True, (225, 225, 225)
        )
        window.blit( #position the controll text
            controll_text, (width//2 - controll_text.get_width()//2, height//2 + start_text.get_height() - 130)
        )
        welcome_text = font1.render(   #create welcome text
            "Welcome to Snake!", True, (255, 255, 255)
        )
        window.blit(   #position the welcome text
            welcome_text, (width//2 - welcome_text.get_width()//2, height//2 + start_text.get_height() - 220)
        )


    elif game_state == "play":
        if move_timer >= move_delay:
            move_timer = 0
            new_head = [snake_body[0][0] + change_x, snake_body[0][1]+change_y]
            snake_body.insert(0,new_head) #adds a new body
            if new_head == apple_pos:
                apple_pos =[
                random.randrange(0,width, block_size),
                random.randrange(0, height, block_size),
            ]
            else:
                snake_body.pop()

            if(
                snake_body[0][0] < 0
                or snake_body [0][0] >= width
                or snake_body [0][1] < 0
                or snake_body [0][1] >= height
            ):
                game_is_underway = False #ends the game

            for block in snake_body [1:]:
                if snake_body[0] == block:
                    game_is_underway = False #ends the game

            #green background
            window.fill(green)

            #draw snake
            for block in snake_body:
                pygame.draw.rect(window, black, [block[0], block[1], block_size, block_size])

            pygame.draw.rect(
                window, red, [apple_pos[0], apple_pos[1], block_size, block_size]
            )
    dt = clock.tick(200) #set timespeed (200fps)
    move_timer += dt

    #display update
    pygame.display.update()
