#08_02_rasp_game_mouse

import pygame
from pygame.locals import *
from sys import exit

spoon_x = 300
spoon_y = 300

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Raspberry Catching')
                                 
spoon = pygame.image.load('spoon.jpg').convert()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))
    spoon_x, ignore = pygame.mouse.get_pos()
    screen.blit(spoon, (spoon_x, spoon_y))
    
    pygame.display.update()

