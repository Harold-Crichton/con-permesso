import pygame
from settings import * 
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((20,40))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH / 2, HEIGHT - 25)
        self.rect.midbottom = self.pos
    
    def update(self):
        self.speedx = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speedx = -5  
        elif keys[pygame.K_RIGHT]:
            self.speedx = 5
        self.rect.x += self.speedx
        if(self.rect.left < 0):
            self.rect.left = 0
        elif (self.rect.right > WIDTH):
            self.rect.right = WIDTH


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

class EndLine(pygame.sprite.Sprite):
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.Surface((WIDTH,10))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT - 20)