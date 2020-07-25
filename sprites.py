import pygame
from settings import * 
from utils import *
from random import SystemRandom
from time import perf_counter
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, game):
        super().__init__(groups)
        self.imageObj = Image(TEXTURE_FOLDER, "player.jpg", WIDTH / 2, HEIGHT - 25, (groups), 110, 95)
        self.image = self.imageObj.image
        self.pos = vec(WIDTH / 2, HEIGHT - 25)
        self.rect = self.imageObj.rect
        self.rect.midbottom = self.pos
        self.game = game
        self.bullet_charged = True

        # Constants
        self.SPEED = 2
        self.FRICTION = -0.12

        self.acc = vec(0,0)
        self.vel = vec(0,0)
    
    def update(self):
        self.acc = vec(0,0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.acc.x = -self.SPEED
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.acc.x = self.SPEED
        if keys [pygame.K_SPACE]:
            if(self.bullet_charged):
                self.t_start = perf_counter()
                self.game.newBullet(self.game, self.rect.midtop)
                self.bullet_charged = False
                self.game.PGBULLET += 1
            elif perf_counter() > (self.t_start + 0.5):
                self.bullet_charged = True 

        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc / 2
        
        if self.pos.x < self.rect.width / 2:
            self.pos.x = self.rect.width / 2
        elif self.pos.x > WIDTH - self.rect.width / 2:
            self.pos.x = WIDTH - self.rect.width / 2
        
        self.rect.midbottom = self.pos


class EnemyPipe(pygame.sprite.Sprite):
    def __init__(self, groups, game):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SystemRandom().randint(0, WIDTH - self.rect.width)
        self.speed = 1
        self.health = 50
        self.game = game

        # Timer
        self.t_start = perf_counter()
        
        self.update()

    def update(self):
        self.rect.y += self.speed

        if perf_counter() > (self.t_start + 3):
            self.t_start = perf_counter()
            self.game.newBullet(self.game, self.rect.midbottom, True)

        if(self.rect.top > HEIGHT):
            self.rect.top = 0

    def setSpeed(self, speed):
        self.speed = speed

    def setHealth(self, health):
        self.health = health


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.pos = vec(position[1][0], position[1][1])
        circle = 14
        self.image = pygame.Surface((circle,circle))
        self.circlex = pygame.draw.circle(self.image, WHITE, (int(circle / 2), int(circle / 2)), 7)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # Constants
        self.SPEED = 1
        self.FRICTION = -0.12

        # Movement
        self.acc = vec(0,0)
        self.vel = vec(0,0)
    
    def update(self):
        self.acc = vec(0,0)
        self.acc.y = - self.SPEED
        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc / 2
        self.FRICTION += 0.005
        self.rect.midbottom = self.pos
        
        if self.rect.top < 0:
            self.kill()

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, groups, position):
        super().__init__(groups)
        self.pos = vec(position[1][0], position[1][1])
        circle = 14
        self.image = pygame.Surface((circle,circle))
        self.circlex = pygame.draw.circle(self.image, GOLD, (int(circle / 2), int(circle / 2)), 7)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # Constants
        self.SPEED = 1
        self.FRICTION = -0.12

        # Movement
        self.acc = vec(0,0)
        self.vel = vec(0,0)
    
    def update(self):
        self.acc = vec(0,0)
        self.acc.y = self.SPEED
        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc / 2
        self.FRICTION += 0.003
        self.rect.midbottom = self.pos
        
        if self.rect.top > HEIGHT:
            self.kill()
