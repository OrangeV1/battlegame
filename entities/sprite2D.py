import pygame
from entities.spriteProvider import SpriteProvider
from yaml import safe_load

class Sprite2D:
    def __init__(self, screen, rect = (0, 0, 80, 80)):
        self.screen = screen
        self.sp = SpriteProvider()
        self.image = pygame.Surface((16, 16))
        self.rect = pygame.Rect(rect)
    
    def checkCollision(self, rect: pygame.Rect, colliders: list):
        """
        Check if the given rectangle collides with the list of tiles with collision
        """
        return rect.collidelist(colliders) != -1

    def draw(self):
        """
        Draw self.image to the screen
        """
        global cameraX, cameraY, scale, tileSize
        if "refreshCamera" in self.screen.events.keys():
            with open("./settings.yaml") as s:
                s = safe_load(s)
                cameraX = s["cameraX"]
                cameraY = s["cameraY"]
                scale = s["scale"]
                tileSize = s["tileSize"]
        draw_rect = self.rect.copy()
        draw_rect.x -= cameraX * scale * tileSize
        draw_rect.y -= cameraY * scale * tileSize
        if self.screen.screen.get_rect().colliderect(draw_rect): # very basic entity culling
            self.screen.screen.blit(self.image, draw_rect)
    
    def update(self):
        """
        Generic update function meant to be overriden by child classes, draws the sprite to the screen on every frame 
        """
        self.draw()