##################################################
#                                                #
#                  PONG GAME                     #
#                                                #
##################################################

import pygame 
import settings, colors 
from player import Player

# Variables 
SIZE = (800, 600)
FPS = 30

game_over = False 


if __name__ == '__main__': 
    pygame.init()

    screen = pygame.display.set_mode(settings.SIZE)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()
    
    player = Player()
    # main game loop
    while not game_over: 
        # do event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 
       

        screen.fill(colors.BLACK)
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

        pygame.display.flip()
        clock.tick(settings.FPS) 

