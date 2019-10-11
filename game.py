##################################################
#                                                #
#                  PONG GAME                     #
#                                                #
##################################################

import pygame 
import settings 

# Variables 
SIZE = (800, 600)

FPS = 30



if __name__ == '__main__': 
    pygame.init()

    game_over = False 


    pygame.display.set_mode(settings.SIZE)
    pygame.display.set_caption(settings.TITLE)
    clock = pygame.time.Clock()

    # main game loop
    while not game_over: 
        # do event handling 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True 

        # draw 
        # draw the stick 
        # draw the ball 

        pygame.display.flip()
        clock.tick(settings.FPS) 

