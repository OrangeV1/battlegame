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
        with open(file[:file.rfind("/")+1]+"mapproperties.yaml") as f:
            f = yaml.safe_load(f)
            with open("./settings.yaml") as s:
                settings = yaml.safe_load(s)
            settings["cameraX"] = f["xOffset"]
            settings["cameraY"] = f["yOffset"]
            with open("./settings.yaml", "w") as s:
                yaml.safe_dump(settings, s, default_flow_style=False)
        self.screen.events["refreshCamera"] = 2

    def refreshcam(self):
        global x, y
        with open("./settings.yaml") as s:
            settings = yaml.safe_load(s)
            x = settings["cameraX"]
            y = settings["cameraY"]
    
    def update(self):
        self.frame_time += 1
        if self.frame_time > self.anim_time:
            self.frame += 1
            self.frame_time = 0
            if self.frame > 2 ** 20:
                self.frame = 0
        if "refreshCamera" in self.screen.events.keys():
            self.refreshcam()
        for i in range(0 + y, y + 8):
            for j in range(0 + x, x + 12):
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
