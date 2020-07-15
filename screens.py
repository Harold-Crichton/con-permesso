import pygame
from settings import *
from sprites import *

class SplashScreen():
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

class Game():
  def __init__(self, main):
    self.is_playing = True
    self.main = main

  def new(self):
    self.is_playing = True
    self.all_sprites = pygame.sprite.Group()
    self.playerObj = Player((self.all_sprites))
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

  def update(self):
    self.all_sprites.update()

  def draw(self):
    self.main.screen.fill(BLACK)
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