from stick import Stick

class Player: 
    def __init__(self):
        self.lives = 3
        self.score = 0
        self.stick = Stick(350, 500, 75, 20)

