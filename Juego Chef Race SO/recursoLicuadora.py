import pygame
from pygame.sprite import Sprite
from pygame.locals import *

class Licuadora(Sprite):
    def __init__(self, cont_size):
        Sprite.__init__(self)
        speed = [0, 2]
        self.cont_size = cont_size
        self.image = pygame.image.load("imagenes/licuadora.png")
        self.rect = self.image.get_rect()
        self.rect.move_ip(cont_size[0] - 90, cont_size[1] - 575)