import pygame
from entities.spriteProvider import SpriteProvider
from entities.sprite2D import Sprite2D

class Entity(Sprite2D):
    def __init__(self, screen):
        super().__init__(screen)
        self.SPEED = 10 #Speed constant
        #Position and velocity
        self.pos = pygame.math.Vector2()
        self.velocity = pygame.math.Vector2()
        self.sp.loadSheet("player/spritesheet")
        self.image = self.sp.scaleImage(self.sp.getSprites([(0, 16, 16, 16)])[0])