import pygame
import random
import sys


pygame.init()
pygame.display.set_caption("snake")
clock = pygame.time.Clock() #define time

#set up startdisplay

font1 = pygame.font.Font(None, 50)
font2 = pygame.font.Font(None, 25)
# initial state

game_state = "select gamemode"

#establish height and width
width = 600
height = 400
window = pygame.display.set_mode((width, height))

multyplayer = False

move_delay = 100
move_timer = 0
#scores
score = 0
record_score = 0
score_player_1 = 0
score_player_2 = 0
winner = "no one"

sanke_dead = False
snake_2_dead = False


#establish colors

black = (0,0,0)
green = (0,255,0)
red = (225,0,0)

#snake
block_size = 20

snake_body_1 = [
    [300, 200],
    [280, 200],
    [260, 200]
]

snake_body_2 = [
    [300, 300],
    [280, 300],
    [260, 300]
]


#apple 
apple_pos_1 = [
    random.randrange(0,width, block_size),
    random.randrange(0, height, block_size),
]

apple_pos_2 = [
    random.randrange(0,width, block_size),
    random.randrange(0, height, block_size),
]

change_x_1 = block_size
change_y_1 = 0

change_x_2 = block_size
change_y_2 = 0


game_is_underway = True

while game_is_underway:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:

            if game_state == "select gamemode":
                if event.key  == pygame.K_1:
                    multyplayer = False
                    game_state  = "start"
                elif event.key == pygame.K_2:
                    multyplayer = True
                    game_state  = "start"


            elif game_state == "start":   
                if event.key == pygame.K_SPACE:
                    game_state = "play"

            elif game_state == "menu":
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_SPACE:
                    move_timer = 0
                    game_state = "play"
                    score = 0
                    score_player_1 = 0
                    score_player_2 = 0
                    snake_2_dead = 0
                    sanke_dead = 0

            
            elif game_state == "play" and sanke_dead == False:
                if event.key == pygame.K_LEFT and change_x_1 == 0:
                    change_x_1 = -block_size
                    change_y_1 = 0
                elif event.key == pygame.K_RIGHT and change_x_1 ==0:
                    change_x_1 = block_size
                    change_y_1 = 0
                elif event.key == pygame.K_UP and change_y_1 == 0:
                    change_x_1 = 0
                    change_y_1 = -block_size
                elif event.key == pygame.K_DOWN and change_y_1 == 0:
                    change_x_1 = 0
                    change_y_1 = block_size
  
            if multyplayer == True and game_state == "play" and snake_2_dead == False:
                if event.key == pygame.K_a and change_x_2 == 0:
                    change_x_2 = -block_size
                    change_y_2 = 0
                elif event.key == pygame.K_d and change_x_2 == 0:
                    change_x_2 = block_size
                    change_y_2 = 0
                elif event.key == pygame.K_w and change_y_2 == 0:
                    change_x_2 = 0
                    change_y_2 = -block_size
                elif event.key == pygame.K_s and change_y_2 == 0:
                    change_x_2 = 0
                    change_y_2 = block_size

    if game_state == "select gamemode":
        window.fill(black)
        welcome_text = font1.render(   
            "Welcome to Snake!", True, (255, 255, 255)
        )
        singleplayer_text = font1.render(
            "PRESS 1 for SINGLEPLAYER", True, (225, 225, 225)
        )
        multyplayer_text = font1.render(
            "PRESS 2 for MULTIPLAYER (2 P.)", True, (225, 225,225)
        )

        window.blits([
            (welcome_text, (width//2 - welcome_text.get_width()//2, height//2 + welcome_text.get_height() - 220)),
            (singleplayer_text, (width//2 - singleplayer_text.get_width()//2, height//2 - 30)),
            (multyplayer_text, (width//2 - multyplayer_text.get_width()//2, height//2 + singleplayer_text.get_height() - 10))
        ])

    
    if game_state == "start":
        window.fill(black)
        start_text = font1.render(  #creating the start text
            "press SPACE to start", True, (255, 255, 255)
        )
        controll_text= font2.render(   #creating the controll text
            "controll with arrow keys", True, (225, 225, 225)
        )

        window.blits([
            (start_text, (width//2 - start_text.get_width()//2, height//2)),
            (controll_text, (width//2 - controll_text.get_width()//2, height//2 + start_text.get_height() - 130))

        ])

    elif game_state == "play":

        
        if move_timer >= move_delay:
            move_timer = 0
            new_head_1 = [snake_body_1[0][0] + change_x_1, snake_body_1[0][1]+change_y_1]
            snake_body_1.insert(0,new_head_1) #adds a new body
            if new_head_1 == apple_pos_1:
                if multyplayer == False:
                    score += 1
                else:
                    score_player_1 += 1
                
                apple_pos_1 = [
                    random.randrange(0, width, block_size),
                    random.randrange(0, height, block_size),
                ]
            elif multyplayer == True and new_head_1 == apple_pos_2:
                score_player_1 += 1
                apple_pos_2 = [
                    random.randrange(0, width, block_size),
                    random.randrange(0, height, block_size),
                ]
            else:
                snake_body_1.pop()
            if multyplayer == False:
                if record_score < score:
                    record_score += 1


            if(
                snake_body_1[0][0] < 0
                or snake_body_1 [0][0] >= width
                or snake_body_1 [0][1] < 0
                or snake_body_1 [0][1] >= height
            ):
                sanke_dead = True


                
            for block in snake_body_1 [1:]:
                if snake_body_1[0] == block:
                        sanke_dead = True




            if multyplayer == True:#sanake_2
                new_head_2 = [snake_body_2[0][0] + change_x_2, snake_body_2[0][1]+change_y_2]
                snake_body_2.insert(0,new_head_2) #adds a new body
                if new_head_2 == apple_pos_1:
                    apple_pos_1 = [
                        random.randrange(0, width, block_size),
                        random.randrange(0, height, block_size),
                    ]
                    score_player_2 += 1
                elif new_head_2 == apple_pos_2:
                    score_player_2 += 1
                    apple_pos_2 = [
                        random.randrange(0, width, block_size),
                        random.randrange(0, height, block_size),
                    ]
                else:
                    snake_body_2.pop()

                if(
                    snake_body_2[0][0] < 0
                    or snake_body_2 [0][0] >= width
                    or snake_body_2 [0][1] < 0
                    or snake_body_2 [0][1] >= height
                ):
                    snake_2_dead = True

                for block in snake_body_2 [1:]:
                    if snake_body_2[0] == block:
                        if multyplayer == False:
                            sanke_2_dead = True


            if sanke_dead == True:
                game_state = "menu"
                game_state = "menu"
                snake_body_1 = [[300, 200], [280, 200], [260, 200]]
                snake_body_2 = [[300, 300], [280, 300], [260, 300]]
                change_x_1 = block_size
                change_y_1 = 0
                change_x_2 = block_size
                change_y_2 = 0
                apple_pos_1 = [
                    random.randrange(0, width, block_size),
                    random.randrange(0, height, block_size),
                ]
                apple_pos_2 = [
                    random.randrange(0, width, block_size),
                    random.randrange(0, height, block_size),
                ]
                move_timer = 0
            
            #green background
            window.fill(green)

            if multyplayer == False:
                score_render = font2.render(
                    f"current score: {score}", True, (0, 0, 0)
                )
                record_score_render = font2.render(
                    f"best score: {record_score}", True, (0, 0, 0)
                )

                window.blits([
                    (score_render, (10, 10)),
                    (record_score_render, (width - record_score_render.get_width() - 10, 10))
                ])

            if multyplayer == True:
                score_player_1_render = font2.render(
                    f"P.1 score:{score_player_1}", True, (0, 0, 0)
                )
                score_player_2_render = font2.render(
                    f"P.2 score:{score_player_2}", True, (0, 0, 0)
                )

                window.blits([
                    (score_player_1_render, (10, 10)),
                    (score_player_2_render, (width - score_player_2_render.get_width() - 10, 10))
                ])
            #draw snake
            for block in snake_body_1:
                pygame.draw.rect(window, black, [block[0], block[1], block_size, block_size])

            pygame.draw.rect(
                window, red, [apple_pos_1[0], apple_pos_1[1], block_size, block_size]
            ) 

            if multyplayer == True:
                for block in snake_body_2:
                    pygame.draw.rect(window, (0, 0, 255), [block[0], block[1], block_size, block_size])
                pygame.draw.rect(
                    window, red, [apple_pos_2[0], apple_pos_2[1], block_size, block_size]
                )

            if multyplayer == False:
                if sanke_dead == True:
                    game_state = "menu"

            if multyplayer == True:
                if sanke_dead == True and snake_2_dead == True:
                    game_state = "menu"
                
    
    elif game_state == "menu":
        if multyplayer == False:
            window.fill(black)
            
            game_over_text = font1.render(  #creating the start text
                f"GAME OVER your score is {score}", True, (255, 255, 255)
            )

            retry_text = font1.render(
                "Press SPACE for RETRY", True, (225, 225, 225)
            )
            quit_text = font2.render(
                "Press q for QUIT",True, (225, 225, 225)
            )

            window.blits([
                (game_over_text, (width//2 - game_over_text.get_width()//2, height//2 + start_text.get_height() - 220)),
                (retry_text, (width//2 - retry_text.get_width()//2, height//2 + start_text.get_height() - 130)),
                (quit_text, (width//2 - quit_text.get_width()//2, height//2))
            ])
        elif multyplayer == True:
            window.fill(black)

            if score_player_1 > score_player_2:
                winner = "player 1"

            elif score_player_2 > score_player_1:
                winner = "player 2"

            elif score_player_1 == score_player_2:
                winner = "no one"

            game_over_text = font1.render(
                "GAME OVER", True, (225, 225, 225)
            )
            score_resulus_1 = font1.render(
                f"Player 1's results: {score_player_1}", True, (225, 225, 225)
            )
            score_resulus_2 = font1.render(
                f"Player 2's results: {score_player_2}", True, (225, 225, 225)
            )
            retry_text = font1.render(
                "Press SPACE for RETRY", True, (225, 225, 225)
            )
            quit_text = font2.render(
                "Press q for QUIT",True, (225, 225, 225)
            )
            winner_text = font1.render(
                f"WINNER: {winner}", True, (255, 0, 0)
            )

            window.blits([
                (game_over_text, (width//2 - game_over_text.get_width()//2, 50)),
                (score_resulus_1, (width//2 - score_resulus_1.get_width()//2, 110)),
                (score_resulus_2, (width//2 - score_resulus_2.get_width()//2, 155)),
                (retry_text, (width//2 - retry_text.get_width()//2, 250)),
                (quit_text, (width//2 - quit_text.get_width()//2, 310)),
                (winner_text, (width//2 - winner_text.get_width()//2, 200))
            ])
    dt = clock.tick(60) #set timespeed (60fps)
    move_timer += dt

    #display update
    pygame.display.update()
