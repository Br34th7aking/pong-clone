##################################################
#                                                #
#                  PONG GAME                     #
#                                                #
##################################################

import pygame 
import settings, colors 
from player import Player
from ball import Ball
import random

# Variables 
SIZE = (800, 600)
FPS = 30

game_over = False 
pygame.font.init()
font = pygame.font.Font('font/PixelEmulator.ttf', 20)
titl_font = pygame.font.Font('font/PixelEmulator.ttf', 50)

def reset(ball, player, screen):
    ball.is_moving = False 
    ball.center_x = player.stick.x + player.stick.width // 2
    ball.center_y = player.stick.y - 5
    player.lives -= 1
    paused = True 
    
    while paused: 

        message = font.render('Press Space to start', True, colors.WHITE)
        screen.blit(message, [200, 300])
        pygame.display.flip()
        if player.lives < 1:
        # current game is over. 
        # restart the game
            game_over_msg = font.render('GAME OVER!!!', True, colors.WHITE)
            screen.blit(game_over_msg, [200, 250])
            restart_msg = font.render('Press Space to restart the game', True, colors.WHITE)
            screen.blit(restart_msg, [100, 300])
            player.lives = 3
            player.score = 0
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_SPACE: 
                    paused = False 
                    screen.fill(colors.BLACK)

if __name__ == '__main__': 
    pygame.init()

    screen = pygame.display.set_mode(settings.SIZE)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    
    player = Player()
    ball = Ball(player.stick.x + player.stick.width // 2, player.stick.y - 5)
    
    # main game loop
    while not game_over: 
        if player.lives <= 0:
            game_over = True 
        # do event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
       
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE and not ball.is_moving:
                    ball.is_moving = True 
                    ball.direction_x = random.choice([-1, 1]) # start moving either left or right 
                    ball.direction_y = -1 # start moving up 


        screen.fill(colors.BLACK)
        score = font.render(f'Score: {player.score}', True, colors.WHITE)
        lives = font.render(f'Lives: {player.lives}', True, colors.WHITE)
        screen.blit(score, [50, 50])
        screen.blit(lives, [600, 50])
        # draw 
        # draw the stick
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_RIGHT]: 
            player.stick.direction = 1
            player.stick.move()
        elif keystate[pygame.K_LEFT]: 
            player.stick.direction = -1
            player.stick.move()
        player.stick.draw(screen, colors.BLUE)
        # draw the ball
        ball.update(player)
        
        if ball.center_y > player.stick.y + player.stick.width: 
            reset(ball, player, screen)

        ball.draw(screen, colors.RED)
        pygame.display.flip()
        clock.tick(settings.FPS) 
    
