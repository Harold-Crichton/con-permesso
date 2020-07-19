import pygame
from settings import * 
from utils import *
from random import SystemRandom
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
            self.game.newBullet(self.game, self.rect.midtop)

        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc / 2
        
        if self.pos.x < self.rect.width / 2:
            self.pos.x = self.rect.width / 2
        elif self.pos.x > WIDTH - self.rect.width / 2:
            self.pos.x = WIDTH - self.rect.width / 2
        
        self.rect.midbottom = self.pos


class EnemyPipe(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SystemRandom().randint(0, WIDTH - self.rect.width)
        self.speed = 1
        self.health = 50
        self.update()

    def update(self):
        self.rect.y += self.speed

    def setSpeed(self, speed):
        self.speed = speed

    def setHealth(self, health):
        self.health = health


class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, position, enemy = False):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        if enemy:
            self.image.fill(GOLD)
        else:
            self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(position)
        self.rect.center = self.pos
