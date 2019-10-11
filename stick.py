##################################################
#                                                #
#                 STICK OBJECT                   #
#                                                #
##################################################
import pygame 
from game_object import GameObject 
import settings 

class Stick(GameObject): 
    def __init__(self, x, y, width, height):
        self.name = 'Player stick'
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.speed = 7 
        self.direction = 0 


    def __str__(self):
        return self.name

    def draw(self, screen, color):
        # draw a rectangle
        pygame.draw.rect(screen, color, [self.x, self.y, self.width, self.height])
    
    def move(self):
        if self.x < 0:
            self.x = 0
        elif self.x > settings.SIZE[0] - self.width: 
            self.x = settings.SIZE[0] - self.width
        else:
            self.x += self.speed * self.direction
        
