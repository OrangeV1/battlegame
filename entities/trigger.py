from entities.sprite2D import Sprite2D
class Trigger(Sprite2D):
    def __init__(self, screen):
        super().__init__(screen)
    
    def whenCollided(self):
        """
        Generic function that gets triggered when a collision between the player and the trigger occurs; should be overriden by child classes
        """
        pass

    def playerCollided(self):
        """
        Checks if the trigger has collided with the player
        """
        return self.rect.colliderect(self.screen.player1)
    
    def update(self):
        super().update()
        #Run a function when trigger collides with the player
        if self.playerCollided():
            self.whenCollided()