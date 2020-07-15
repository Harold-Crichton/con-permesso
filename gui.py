import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, msg, color, size, x ,y, groups, font):
        super().__init__(groups)

        self.surface = font.render(msg, False, color)
        self.rect = self.surface.get_rect()
        self.rect.midtop = (x, y)