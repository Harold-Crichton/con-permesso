import pygame
from settings import *
from screens import *

if __name__ == "__main__":
    splashObj = SplashScreen()
    gameObj = Game()
    gameOverObj = GameOver()
    splashObj.new()
    while is_running:
        gameObj.new()
        if gameObj.is_playing:
            gameOverObj.new()
    pygame.quit()