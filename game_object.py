##################################################
#                                                #
#                 GAME OBJECT                    #
#                                                #
##################################################

class GameObject: 
    def __init__(self):
        raise NotImplementedError('Do not create a raw game object!')

    def __str__(self):
        return self.name

    def draw(self):
        pass


