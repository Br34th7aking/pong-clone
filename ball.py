##################################################
#                                                #
#                  BALL OBJECT                   #
#                                                #
##################################################
import pygame 
from game_object import GameObject 
import settings 

class Ball(GameObject): 
    def __init__(self, x, y, radius=10):
        self.name = 'Ball'
        self.center_x = x
        self.center_y = y
        self.radius = radius 
        self.speed = 4 
        self.direction_x = 0 
        self.direction_y = 0 
        self.is_moving = False 

    def __str__(self):
        return self.name

    def draw(self, screen, color):
        # draw a circle
        pygame.draw.circle(screen, color, [self.center_x, self.center_y], self.radius)
    
    def update(self, player):
        # draw the self
        self.center_x += self.speed * self.direction_x 
        self.center_y += self.speed * self.direction_y

        if self.center_x < 0 or self.center_x > settings.SIZE[0] - self.radius:
            self.direction_x = -self.direction_x 
        if self.center_y < 0 or self.center_y > settings.SIZE[1] - self.radius:
            self.direction_y = -self.direction_y
        if self.check_collision(player.stick):
            self.direction_y = -self.direction_y
            if player.stick.direction == -self.direction_x: 
                self.direction_x = -self.direction_x

    def check_collision(self, stick):
        if self.center_x > stick.x and self.center_x < stick.x + stick.width \
            and self.center_y >= stick.y:
            return True
    
        return False 
