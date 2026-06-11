from map.tileset import Tileset

class tileManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            0: [],
            163: [(1 * 16, 0, 16, 16)],
            17: [(17 * 16, 4 * 16, 16, 16)],
            102: [(5 * 16, 12 * 16, 16, 16)],
            59: [(16 * 16, 4 * 16, 16, 16)],
            61: [(18 * 16, 4 * 16, 16, 16)]
        }
        super().__init__("tiles/32xtileset", 0, tiles)
        self.frames = 0
        self.load_tiles("./assets/maps/temp/tiles.csv")

class objectManager(Tileset):
    def __init__(self, screen):
        self.screen = screen
        tiles = {
            4: [(6 * 16, 2 * 16, 16, 16)],
            36: [(4 * 16, 5 * 16, 16, 16)]
        }
        super().__init__("tiles/16xtiles", 0, tiles)
        self.load_tiles("./assets/maps/temp/tiles.csv")