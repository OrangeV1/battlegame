from entities.trigger import Trigger
from map.tileset import Tileset
from entities.collider import Collider
from yaml import safe_load

class upLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 5.5, 0
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("u1")
        self.screen.player1.pos.y = 80 * 6.5 - 10

class leftLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 0, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("l1")
        self.screen.player1.pos.x = 80 * 10.5 - 10

class rightLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 11.5, 80 * 3.5
        self.rect.width *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("r1")
        self.screen.player1.pos.x = 80 * 0.5 + 10

class downLevelTrigger(Trigger):
    def __init__(self, screen):
        super().__init__(screen)
        self.rect.x, self.rect.y = 80 * 4.5, 80 * 7.5
        self.rect.width *= 3
        self.rect.height *= 0.5
    
    def whenCollided(self):
        self.screen.tm.loadMap("temp")
        self.screen.player1.pos.x = 80 * 100 + 10
        self.screen.player1.pos.y = 80 * 26 + 10

class Rtree1(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 10, scale * 5, scale * 2, scale * 2)

class Ltree1(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, 0, scale * 5, scale * 1, scale * 3)

class Rtree2(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 8, scale *7, scale * 4, scale * 1)

class Ltree2(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 1, scale * 7, scale * 3, scale * 1)

class Lwall1(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, 0, 0, scale * 2, scale * 3)

class Lwall2(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 4, 0, scale * 1, scale * 3)

class Rwall1(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 7, 0, scale * 1, scale * 3)

class Rwall2(Collider):
    def __init__(self, screen):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
            scale = settings["scale"] * 16
        super().__init__(screen, scale * 10, 0, scale * 2, scale * 3)

class tileManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            0: [],
            1: [(1 * 16, 0, 16, 16)],
            2: [(17 * 16, 4 * 16, 16, 16)],
            3: [(5 * 16, 12 * 16, 16, 16), (6 * 16, 12 * 16, 16, 16), (7 * 16, 12 * 16, 16, 16), (8 * 16, 12 * 16, 16, 16)],
            6: [(16 * 16, 4 * 16, 16, 16)],
            7: [(18 * 16, 4 * 16, 16, 16)]
        }
        super().__init__("tiles/32xtileset", 7, tiles)
        self.frames = 3
        self.load_tiles("./assets/maps/start/tiles.csv")

class objectManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            4: [(6 * 16, 2 * 16, 16, 16)],
            5: [(8 * 16, 5 * 16, 16, 16), (9 * 16, 5 * 16, 16, 16), (10 * 16, 5 * 16, 16, 16)]
        }
        super().__init__("tiles/16xtiles", 7, tiles)
        self.load_tiles("./assets/maps/start/tiles.csv")