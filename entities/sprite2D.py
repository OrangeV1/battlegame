import pygame
from entities.spriteProvider import SpriteProvider

class Sprite2D:
    def __init__(self, screen, rect = (0, 0, 80, 80)):
        self.screen = screen
        self.sp = SpriteProvider()
        self.image = pygame.Surface((16, 16))
        self.rect = pygame.Rect(rect)
    
    def checkCollision(self, rect: pygame.Rect, colliders):
        """
        Check if the given rectangle collides with the list of tiles with collision
        """
        return rect.collidelist(colliders) != -1

    def draw(self):
        """
        Draw self.image to the screen
        """
        self.screen.screen.blit(self.image, self.rect)
    
    def update(self):
        """
        Generic update function meant to be overriden by child classes, draws the sprite to the screen on every frame 
        """
        self.draw()