import pygame
from settings import *
from sprites import *
from os import path
from utils import *

class SplashScreen():
  def __init__(self, main):
    self.main = main

  def new(self):
    self.all_sprites = pygame.sprite.Group()
    self.all_texts = pygame.sprite.Group()
    self.all_images = pygame.sprite.Group()
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

    # Set texts
    titleText = Text(TITLE, GOLD, 50, WIDTH / 2, 70, (self.all_sprites, self.all_texts), DEFAULT_FONT)
    instructionText = Text("Premere SPAZIO per iniziare la partita", BLUE, 35, WIDTH / 2, 140, (self.all_sprites, self.all_texts), DEFAULT_FONT)

    # Set Images
    lordImg = Image(TEXTURE_FOLDER, "player.jpg", WIDTH / 2, HEIGHT / 2 + 50, (self.all_sprites, self.all_images))
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
    self.all_texts = pygame.sprite.Group()
    self.all_images = pygame.sprite.Group()
    self.all_mobs = pygame.sprite.Group()
    self.player_bullets = pygame.sprite.Group()
    self.enemy_bullets = pygame.sprite.Group()

    self.playerObj = Player((self.all_sprites), self)
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

    # Mob timer
    self.n_mob = 2
    self.timeNewMob = 6000
    self.NEW_MOB = pygame.USEREVENT+2
    pygame.time.set_timer(self.NEW_MOB, self.timeNewMob)
    self.newMob()

    self.RELOAD = pygame.USEREVENT+3

    # Score
    self.PGBULLET = 0
    x = 100
    y = 25                                                                                        
    self.tartanBackground = Image(TEXTURE_FOLDER, "tartan.jpg", x, y + 15, (self.all_sprites, self.all_images), 70, 150)
    self.scoreText = Text("Score 1000", GOLD, 17, x, y, (self.all_sprites, self.all_texts), DEFAULT_FONT) 
    self.silverBulletText = Text(f"Silver bullet {self.PGBULLET}", SILVER, 15, x, y + 30, (self.all_sprites, self.all_texts), DEFAULT_FONT) 

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
      elif e.type == self.NEW_MOB:
        self.newMob()
      elif e.type == self.RELOAD:
        self.playerObj.bullet_charged = True

  def update(self):
    self.silverBulletText.update_text(f"Silver bullet {self.PGBULLET}", SILVER, 15, 100, 55, (self.all_sprites, self.all_texts), DEFAULT_FONT)
    self.all_sprites.update()
  
  def draw(self):
    self.main.screen.blit(self.BACKGROUND_FRAMES[self.backgroundIndex], (0,0))
    self.all_sprites.draw(self.main.screen)
    self.all_images.draw(self.main.screen)
    self.all_texts.draw(self.main.screen)
    pygame.display.flip()
  
  def newMob(self):
    for _ in range (self.n_mob):
      EnemyPipe((self.all_mobs, self.all_sprites), self)
    
  def newBullet(self, x, y, enemy = False):
    Bullet((self.all_sprites, self.player_bullets), (x, y), enemy)

  
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
