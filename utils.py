import pygame
from os import path
from settings import *

class Text(pygame.sprite.Sprite):
    def __init__(self, msg, color, size, x ,y, groups, font):
        super().__init__(groups)
        self.update_text(msg, color, size, x ,y, groups, font)
        
    def update_text(self, msg, color, size, x ,y, groups, fontName):
        self.font = pygame.font.Font(fontName, size)
        self.image = self.font.render(msg, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

class Music():
    def __init__(self, name):
        self.name = path.join(SOUNDS_FOLDER, name)
        pygame.mixer.init()
        pygame.mixer.music.load(self.name)
        pygame.mixer.music.play(0)

# // -------------------------
#           IMAGE 
# --------------------------// 
        
class Image(pygame.sprite.Sprite):
    def __init__(self, dir, name, x ,y, groups, sizeH = None, sizeW = None):
        super().__init__(groups)
        self.image = loadImage(dir, name, sizeH, sizeW)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

def loadImage(dir, name, sizeH = None, sizeW = None):
    image = pygame.image.load(path.join(dir, name))
    if sizeH != None and sizeW != None:
        image = pygame.transform.scale(image, (sizeW, sizeH))
    return image