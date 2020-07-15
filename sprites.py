import pygame
from settings import * 
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((20,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH / 2, HEIGHT - 50)
        self.rect.midbottom = self.pos

class EnemyPipe(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, groups, x, y, enemy = False):
        super().__init__(groups)
        self.image = pygame.Surface((50,50))
        if enemy:
            self.image.fill(GOLD)
        else:
            self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.pos = vec(x, y)
        self.rect.center = self.pos
