import pygame

#Creation of the Level class
class Level:
    def __init__(self):
        
        #Get the display surface
        self.display_surface = pygame.display.get_surface()

        #Sprite group setup. The 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

    #The run method will "draw" the game sprites
    def run(self):
        pass
