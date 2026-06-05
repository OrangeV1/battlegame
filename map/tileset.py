from entities.spriteProvider import SpriteProvider
import yaml

class Tileset:
    def __init__(self, img: str, anim_frames: int, tiles: dict = {}):
        self.img = img
        self.tiles = tiles
        self.anim_time = anim_frames
        self.frames = self.anim_time
        self.frame_time = 0
        self.frame = 0
        self.sp = SpriteProvider()
        self.current_tiles = []
        self.sp.loadSheet(self.img)
        self.anim_tiles = []
        for key in tiles.keys():
            tiles[key] = self.sp.getSprites(tiles[key])
        for tile in tiles.keys():
            if len(tiles[tile]) > 1:
                self.anim_tiles.append(tile)
    
    def set_tile(self, num: int, frames: list):
        self.tiles[num] = self.sp.getSprites(frames)
        if len(frames) > 1:
            self.anim_tiles.append(num)

    def load_tiles(self, file: str):
        self.current_map = open(file).read().split("\n")
        for i in range(len(self.current_map)):
            self.current_map[i] = self.current_map[i].split(";")
            while "" in self.current_map[i]:
                self.current_map[i].remove("")
    
    def update(self):
        self.frame_time += 1
        if self.frame_time > self.anim_time:
            self.frame += 1
            self.frame_time = 0
            if self.frame > 2 ** 20:
                self.frame = 0
        settings = yaml.safe_load(open("./settings.yaml"))
        x = settings["cameraX"]
        y = settings["cameraY"]
        for i in range(0 + y, len(self.current_map)):
            for j in range(0 + x, len(self.current_map[i])):
                try:
                    if int(self.current_map[i][j]) in self.anim_tiles:
                        image = self.sp.scaleImage(self.tiles[int(self.current_map[i][j])][self.frame % len(self.tiles[int(self.current_map[i][j])])])
                    else:
                        image = self.sp.scaleImage(self.tiles[int(self.current_map[i][j])][0])
                    rect = image.get_rect()
                    #Get pixel coordinates (column/row * tileSize * SCALE)
                    rect.x, rect.y = (j - x) * rect.width, (i - y) * rect.height
                    #Draw the image to the screen
                    self.screen.screen.blit(image, rect)
                except: pass
