from entities.trigger import Trigger
from map.tileset import Tileset

class upLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 4.5, 0
        self.rect.width *= 3
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("start")
        self.screen.player1.pos.y = 80 * 6.5

class tileManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            0: [],
            1: [(1 * 16, 0, 16, 16)],
            2: [(17 * 16, 4 * 16, 16, 16)],
            3: [(5 * 16, 12 * 16, 16, 16), (6 * 16, 12 * 16, 16, 16), (7 * 16, 12 * 16, 16, 16), (8 * 16, 12 * 16, 16, 16)],
            5: [(16 * 16, 4 * 16, 16, 16)],
            6: [(18 * 16, 4 * 16, 16, 16)]
        }
        super().__init__("tiles/32xtileset", 7, tiles)
        self.frames = 3
        self.load_tiles("./assets/maps/d1/tiles.csv")

class objectManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            4: [(8 * 16, 5 * 16, 16, 16)]
        }
        super().__init__("tiles/16xtiles", 7, tiles)
        self.load_tiles("./assets/maps/d1/tiles.csv")