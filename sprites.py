import pygame
from settings import * 
from utils import *
from random import SystemRandom
from time import perf_counter
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, groups, game):
        super().__init__(groups)
        self.game = game
        self.pos = vec(WIDTH / 2, HEIGHT - 25)
        self.health = 100
        
        self.image = loadImage(TEXTURE_FOLDER, "player.jpg", 110, 95)

        self.rect = self.image.get_rect()
        self.rect.midbottom = self.pos
        self.bullet_charged = True

        # Constants
        self.SPEED = 2
        self.FRICTION = -0.12
        self.RELOAD_TIME = 500

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
                self.game.newBullet(self.game, self.rect.midtop)
                self.bullet_charged = False
                self.game.PGBULLET += 1
                pygame.time.set_timer(self.game.RELOAD, self.RELOAD_TIME)

        self.acc += self.vel * self.FRICTION
        self.vel += self.acc
        self.pos += self.vel + self.acc / 2
        
        if self.pos.x < self.rect.width / 2:
            self.pos.x = self.rect.width / 2
        elif self.pos.x > WIDTH - self.rect.width / 2:
            self.pos.x = WIDTH - self.rect.width / 2
        
        self.rect.midbottom = self.pos

        hits = pygame.sprite.spritecollide(self, self.game.enemy_bullets, False)
        hits += pygame.sprite.spritecollide(self, self.game.all_mobs, False)
        for hit in hits:
            self.health -= hit.damage
            hit.kill()
        if self.health <= 0:
            self.kill()
            self.game.is_playing = False

class Enemy(pygame.sprite.Sprite):
    def __init__(self, groups, game):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = SystemRandom().randint(0, WIDTH - self.rect.width)
        self.speed = 1
        self.health = 50
        self.damage = 25
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

        hits = pygame.sprite.spritecollide(self, self.game.player_bullets, False)
        for hit in hits:
            self.health -= hit.damage
            hit.kill()
        if self.health <= 0:
            self.game.enemyKilled += 1
            self.kill()

    def setSpeed(self, speed):
        self.speed = speed

    def setHealth(self, health):
        self.health = health

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, position, enemyBullet = False):
        super().__init__(groups)
        self.pos = vec(position[1][0], position[1][1])

        self.circle_size = 14
        self.image = pygame.Surface((self.circle_size,self.circle_size))
        self.circle = pygame.draw.circle(self.image, (WHITE if not enemyBullet else GOLD), (self.circle_size // 2, self.circle_size // 2), 7)

        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # Constants
        self.SPEED = 1 * (-1 if not enemyBullet else 1)
        self.damage = 25

        # Movement
        self.acc = vec(0, 0)
        self.vel = vec(0, 0)

    def update(self):
        self.acc = vec(0, self.SPEED)

        self.vel += self.acc
        self.pos += self.vel + self.acc / 2

        self.rect.center = self.pos

        if self.rect.top < 0 or self.rect.top > HEIGHT:
            self.kill()
