import pygame
from settings import *
from screens import *

class Main():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(TITLE)
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.is_running = True
        self.run()

    def run(self):
        # splashObj = SplashScreen(self)
        gameObj = Game(self)
        gameOverObj = GameOver(self) 
        # splashObj.new()
        while self.is_running:
            gameObj.new()
            if gameObj.is_playing:
                gameOverObj.new()

if __name__ == "__main__":
    mainOBj = Main()
    pygame.quit()
