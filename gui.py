import pygame

class Text(pygame.sprite.Sprite):
    def __init__(self, msg, color, size, x ,y, groups, font):
        super().__init__(groups)
        self.update_text( msg, color, size, x ,y, groups, font)
        
    def update_text(self, msg, color, size, x ,y, groups, font):
        self.font = pygame.font.Font(font, size)
        self.image = font.render(msg, False, color)
        self.rect = self.image.get_rect()
        self.rect.lefttop = (x, y)