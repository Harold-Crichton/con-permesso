import pygame
from settings import *
from sprites import *
from os import path
from utils import *

class SplashScreen():
  def __init__(self, main):
    self.main = main
    self.new()

  def new(self):
    self.all_sprites = pygame.sprite.Group()
    self.is_playing = True

    # Set backgrounds
    n_backgrounds = 3
    self.BACKGROUND_FRAMES = []
    for i in range(0, n_backgrounds):
      img = path.join(BACKGROUNDS_FOLDER, f'background{i}.png')
      self.BACKGROUND_FRAMES.append(pygame.image.load(img))
    self.DO_ANIM = pygame.USEREVENT+1
    pygame.time.set_timer(self.DO_ANIM, 500)
    self.backgroundIndex = 0

    self.run()

  def run(self):
    while self.is_playing:
      self.eventHandler()
      self.update()
      self.draw()
      self.main.clock.tick(FPS)

  def eventHandler(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.main.is_running = False
        self.is_playing = False
      elif e.type == self.DO_ANIM:
        self.backgroundIndex += 1
        if self.backgroundIndex == len(self.BACKGROUND_FRAMES):
          self.backgroundIndex = 0
      elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_SPACE:
          self.is_playing = False

  def update(self):
    self.all_sprites.update()

  def draw(self):
    self.main.screen.blit(self.BACKGROUND_FRAMES[self.backgroundIndex], (0,0))
    self.all_sprites.draw(self.main.screen)
    pygame.display.flip()

class Game(): 
  def __init__(self, main):
    self.is_playing = True
    self.main = main

  def new(self):
    self.is_playing = True
    self.all_sprites = pygame.sprite.Group()
    self.playerObj = Player((self.all_sprites))
    self.endLineObj = EndLine((self.all_sprites))
    self.musicObj = Music("music1.ogg")
    
    # Set backgrounds
    n_backgrounds = 3
    self.BACKGROUND_FRAMES = []
    for i in range(0, n_backgrounds):
      img = path.join(BACKGROUNDS_FOLDER, f'background{i}.png')
      self.BACKGROUND_FRAMES.append(pygame.image.load(img))
    self.DO_ANIM = pygame.USEREVENT+1
    pygame.time.set_timer(self.DO_ANIM, 500)
    self.backgroundIndex = 0

    self.run()

  def run(self):
    while self.is_playing:
      self.eventHandler()
      self.update()
      self.draw()
      self.main.clock.tick(FPS)

  def eventHandler(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.main.is_running = False
        self.is_playing = False
      elif e.type == self.DO_ANIM:
        self.backgroundIndex += 1
        if self.backgroundIndex == len(self.BACKGROUND_FRAMES):
          self.backgroundIndex = 0

  def update(self):
    self.all_sprites.update()

  def draw(self):
    self.main.screen.blit(self.BACKGROUND_FRAMES[self.backgroundIndex], (0,0))
    self.all_sprites.draw(self.main.screen)
    pygame.display.flip()
  
class GameOver():
  def __init__(self, main):
    self.is_playing = True
    self.main = main

  def new(self):
    pass

  def run(self):
    pass

  def eventHandler(self):
    pass

  def update(self):
    pass

  def draw(self):
    pass