import pygame
from settings import *

#Creation of the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups):

        #Initialization of the Player class and asignation of it's sprite
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)