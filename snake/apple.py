import pygame
import random

class Apple():

    def __init__(self, sn_setting, screen):
        self.screen = screen

        coordinate_x = random.randint(0,sn_setting.max_square_x)
        coordinate_y = random.randint(0, sn_setting.max_square_y)
        self.coordinat=(coordinate_x,coordinate_y)

        self.image = pygame.image.load('images\Apple_20.bmp')
        self.rect = ((coordinate_x * sn_setting.size_square,
                     coordinate_y * sn_setting.size_square),
                     (sn_setting.size_square,sn_setting.size_square))

    def blitme(self):
        self.screen.blit(self.image,self.rect)
