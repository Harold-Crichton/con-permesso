import pygame
from os import path

HEIGHT = 400
WIDTH = 400
FPS = 60

# Source Folders
TEXTURE_FOLDER = path.join(path.dirname(__file__), "src", "textures")
SOUNDS_FOLDER = path.join(path.dirname(__file__), "sounds")
BACKGROUNDS_FOLDER = path.join(TEXTURE_FOLDER, "backgrounds")
BOSSES_FOLDER = path.join(TEXTURE_FOLDER, "bosses")
PIPES_FOLDER = path.join(TEXTURE_FOLDER, "pipes")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GOLD = (201, 176, 55)