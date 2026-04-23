from pygame.rect import Rect

class Collider():
    def __init__(self, screen, x, y, width, height):
        self.rect = Rect(x, y, width, height)
        screen.tm.collision_group.append(self.rect)

    def update(self):
        pass