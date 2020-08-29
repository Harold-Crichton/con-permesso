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
    self.is_running = True

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
    while self.is_running:
      self.eventHandler()
      self.update()
      self.draw()
      self.main.clock.tick(FPS)

  def eventHandler(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.main.is_playing = False
        self.is_running = False
      elif e.type == self.DO_ANIM:
        self.backgroundIndex += 1
        if self.backgroundIndex == len(self.BACKGROUND_FRAMES):
          self.backgroundIndex = 0
      elif e.type == pygame.KEYDOWN:
        if e.key == pygame.K_SPACE:
          self.is_running = False
      
  def update(self):
    self.all_sprites.update()

  def draw(self):
    self.main.screen.blit(self.BACKGROUND_FRAMES[self.backgroundIndex], (0,0))
    self.all_sprites.draw(self.main.screen)
    pygame.display.flip()

class Game(): 
  def __init__(self, main):
    self.is_running = True
    self.main = main

  def new(self):
    self.is_running = True
    # Groups
    self.all_sprites = pygame.sprite.Group()
    self.all_texts = pygame.sprite.Group()
    self.all_images = pygame.sprite.Group()
    self.all_enemies = pygame.sprite.Group()
    self.player_bullets = pygame.sprite.Group()
    self.enemies_bullets = pygame.sprite.Group()
    #Obj
    self.playerObj = Player((self.all_sprites), self)
    self.musicObj = Music("music1.ogg")
    # Backgrounds
    self.BACKGROUND_FRAMES = []
    self.backgroundIndex = 0 # Number of background loaded
    # Events
    self.DO_ANIM = pygame.USEREVENT + 1 # Change background
    self.NEW_ENEMY = pygame.USEREVENT + 2 # Spawn a new enemy
    self.RELOAD = pygame.USEREVENT + 3 # Reload time for Player's shoot 
    # Enemy's timer
    self.n_enemies = 2
    self.timeNewEnemy = 6000
    # Levels
    self.enemiesKilled = 0
    self.nextLevel = 15
    # Tartan
    self.tartanBackground = None
    # Score
    self.scoreText = None
    self.playerHealthText = None 
    # Initialize
    pygame.time.set_timer(self.DO_ANIM, 500)
    pygame.time.set_timer(self.NEW_ENEMY, self.timeNewEnemy)
    self.setBackground()
    self.setScore()
    self.newEnemy()
    # Start
    self.run()

  def run(self):
    while self.is_running:
      self.eventHandler()
      self.update()
      self.draw()
      self.main.clock.tick(FPS)

  def eventHandler(self):
    for e in pygame.event.get():
      # Go to GameOver screen
      if e.type == pygame.QUIT:
        self.main.is_playing = False
        self.is_running = False
      # Change background
      elif e.type == self.DO_ANIM:
        self.backgroundIndex += 1
        if self.backgroundIndex == len(self.BACKGROUND_FRAMES):
          self.backgroundIndex = 0
      # Spawn a new enemy
      elif e.type == self.NEW_ENEMY:
        self.newEnemy()
      # Reload time for Player's shoot 
      elif e.type == self.RELOAD:
        self.playerObj.bullet_charged = True

  def update(self):
    self.playerHealthText.update_text(f"Health {int(self.playerObj.health)}", SILVER, 15, 100, 55, (self.all_sprites, self.all_texts), DEFAULT_FONT)
    self.all_sprites.update()

    # To do boss
    if self.enemiesKilled >= self.nextLevel:
      pass
  
  def draw(self):
    self.main.screen.blit(self.BACKGROUND_FRAMES[self.backgroundIndex], (0,0))
    self.all_sprites.draw(self.main.screen)
    self.all_images.draw(self.main.screen)
    self.all_texts.draw(self.main.screen)
    pygame.display.flip()
  
  def newEnemy(self):
    for _ in range (self.n_enemies):
      Enemy((self.all_enemies, self.all_sprites), self)
    
  def newBullet(self, x, y, enemy = False):
    # Find the new bullet's group
    bullets_group = None
    if enemy == True:
      bullets_group = self.enemies_bullets
    else:
      bullets_group = self.player_bullets
    Bullet((self.all_sprites, bullets_group), (x, y), enemy)
  
  def setBackground(self):
    n_backgrounds = 4
    for i in range(0, n_backgrounds):
      img = path.join(BACKGROUNDS_FOLDER, f'background{i}.png')
      self.BACKGROUND_FRAMES.append(pygame.image.load(img))
  
  def setScore(self):
    x = 100
    y = 25                                                                                        
    self.tartanBackground = Image(TEXTURE_FOLDER, "tartan.jpg", x, y + 15, (self.all_sprites, self.all_images), 70, 150)
    self.scoreText = Text("Score 1000", GOLD, 17, x, y, (self.all_sprites, self.all_texts), DEFAULT_FONT) 
    self.playerHealthText = Text(f"Health {int(self.playerObj.health)}", SILVER, 15, x, y + 30, (self.all_sprites, self.all_texts), DEFAULT_FONT)

  
class GameOver():
  def __init__(self, main):
    self.is_running = True
    self.main = main

  def new(self):
    # Groups
    self.all_sprites = pygame.sprite.Group()
    self.background_image = loadImage(GAMEOVER_FOLDER, "background.jpg")
    self.run()

  def run(self):
    while self.is_running:
      self.eventHandler()
      self.update()
      self.draw()
      self.main.clock.tick(FPS)

  def eventHandler(self):
    for e in pygame.event.get():
      if e.type == pygame.QUIT:
        self.main.is_playing = False
        self.is_running = False

  def update(self):
    self.all_sprites.update()

  def draw(self):
    self.main.screen.blit(self.background_image, (0,0))
    self.all_sprites.draw(self.main.screen)
    pygame.display.flip()
