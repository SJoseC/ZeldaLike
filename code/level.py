import pygame
from settings import *
from tile import Tile
from player import Player


#Creation of the Level class
class Level:
    def __init__(self):
        
        #Get the display surface
        self.display_surface = pygame.display.get_surface()

        #Sprite group setup. The 
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()

        #Sprite setup
        self.create_map()

    #Definition of the X and Y position coordinates on the worldmap
    def create_map(self):
        for row_index,row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                X = col_index * TILESIZE
                Y = row_index * TILESIZE
                if col == 'X':
                    Tile((X,Y),[self.visible_sprites])

    #The run method will "draw" the game sprites
    def run(self):
        pass
