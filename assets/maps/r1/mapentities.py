from entities.trigger import Trigger
from map.tileset import Tileset

class leftLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 0, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.x = 80 * 10.5 - 10

class tileManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            0: [],
            1: [(1 * 16, 0, 16, 16)],
            2: [(17 * 16, 4 * 16, 16, 16)],
            3: [(4 * 16, 12 * 16, 16, 16)],
            5: [(16 * 16, 4 * 16, 16, 16)],
            6: [(18 * 16, 4 * 16, 16, 16)]
        }
        super().__init__("tiles/32xtileset", 7, tiles)
        self.load_tiles("./assets/maps/r1/tiles.csv")

class objectManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            4: [(8 * 16, 5 * 16, 16, 16)],
            7: [(11 * 16, 5 * 16, 16, 16)],
            8: [(31 * 16, 2 * 16, 16, 16)]
        }
        super().__init__("tiles/16xtiles", 7, tiles)
        self.load_tiles("./assets/maps/r1/tiles.csv")