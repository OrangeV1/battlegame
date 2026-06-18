from map.tileset import Tileset
from pygame import Rect
from yaml import safe_load, safe_dump

class cameraHelper():
    def __init__(self, screen):
        self.screen = screen
        self.player = self.screen.player1
        self.update_pos()
        # self.colliders = [self.lRect, self.uRect, self.rRect, self.dRect]
    
    def update_pos(self):
        with open("./settings.yaml") as s:
            s = safe_load(s)
            self.cameraX = s["cameraX"]
            self.cameraY = s["cameraY"]
            self.scale = s["scale"]
            self.tileSize = s["tileSize"]
        scale = self.tileSize * self.scale
        self.lRect = Rect(self.cameraX * scale - 16, self.cameraY * scale, 16, 80 * 8)
        self.uRect = Rect(self.cameraX * scale, self.cameraY * scale - 16, 80 * 12, 16)
        self.rRect = Rect(self.cameraX * scale + 80 * 12, self.cameraY * scale, 16, 80 * 8)
        self.dRect = Rect(self.cameraX * scale, self.cameraY * scale + 80 * 8, 80 * 12, 16)

    def update_cam(self, x, y):
        with open("./settings.yaml") as s:
            settings = safe_load(s)
        settings["cameraX"] += x
        settings["cameraY"] += y
        with open("./settings.yaml", "w") as s:
            safe_dump(settings, s, default_flow_style=False)
        self.screen.events["refreshCamera"] = 1
        self.update_pos()

    def update(self):
        #if self.player.rect.collidelist(self.colliders):
        if self.player.rect.colliderect(self.lRect):
            self.update_cam(-12, 0)

class tileManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            0: [],
            163: [(1 * 16, 0 * 16, 16, 16)],
            17: [(17 * 16, 4 * 16, 16, 16)],
            102: [(5 * 16, 12 * 16, 16, 16)],
            59: [(16 * 16, 4 * 16, 16, 16)],
            61: [(18 * 16, 4 * 16, 16, 16)],
            232: [(0 * 16, 5 * 16, 16, 16)],
            35: [(3 * 16, 8 * 16, 16, 16)],
            37: [(8 * 16, 8 * 16, 16, 16)],
            20: [(4 * 16, 7 * 16, 16, 16)],
            52: [(4 * 16, 9 * 16, 16, 16)],
            51: [(3 * 16, 9 * 16, 16, 16)],
            53: [(8 * 16, 9 * 16, 16, 16)],
            19: [(3 * 16, 7 * 16, 16, 16)],
            85: [(0 * 16, 13 * 16, 16, 16)],
            69: [(0 * 16, 12 * 16, 16, 16)],
            84: [(0 * 16, 11 * 16, 16, 16)],
            21: [(8 * 16, 7 * 16, 16, 16)],
            68: [(0 * 16, 10 * 16, 16, 16)],
            146: [(0 * 16, 1 * 16, 16, 16)],
            148: [(2 * 16, 1 * 16, 16, 16)],
            131: [(1 * 16, 2 * 16, 16, 16)],
            130: [(0 * 16, 0 * 16, 16, 16)],
            132: [(2 * 16, 0 * 16, 16, 16)],
            162: [(0 * 16, 2 * 16, 16, 16)],
            164: [(2 * 16, 2 * 16, 16, 16)]
        }
        super().__init__("tiles/32xtileset", 0, tiles)
        self.frames = 0
        self.load_tiles("./assets/maps/temp/tiles.csv")

class objectManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            4: [(6 * 16, 2 * 16, 16, 16)],
            36: [(4 * 16, 5 * 16, 16, 16)],
            119: [(31 * 16, 2 * 16, 16, 16)]
        }
        super().__init__("tiles/16xtiles", 0, tiles)
        self.load_tiles("./assets/maps/temp/tiles.csv")