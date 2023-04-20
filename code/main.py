import pygame, sys
from settings import *
from level import Level

#Creation of the class Game
class Game:
    def __init__(self):

        #General setup of the screen and the internal clock of the game
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.level = Level()
        pygame.display.set_caption('The Nymph Trials')

    #Declaration of the method Run to open the game window and keep it open with a main loop
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)

#Cast of the class Game and the method Run
if __name__ == '__main__':
    game = Game()
    game.run()
                    