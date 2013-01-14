#08_06_rasp_game_final

import pygame
from pygame.locals import *
from sys import exit
import random

score = 0

screen_width = 600
screen_height = 400

spoon_x = 300
spoon_y = screen_height - 100

class Raspberry:
    x = 0
    y = 0
    dy = 0

    def __init__(self):
        self.x = random.randint(10, screen_width)
        self.y = 0
        self.dy = random.randint(3, 10)

    def update(self):
        self.y += self.dy
        if self.y > spoon_y:
            self.y = 0
            self.x = random.randint(10, screen_width)
        self.x += random.randint(-5, 5)
        if self.x < 10:
            self.x = 10
        if self.x > screen_width - 20:
            self.x = screen_width - 20
        screen.blit(raspberry_image, (self.x, self.y))

    def is_caught(self):
        return self.y >= spoon_y and self.x >= spoon_x and self.x < spoon_x + 50

clock = pygame.time.Clock()
rasps = [Raspberry(), Raspberry(), Raspberry()]

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Raspberry Catching')
                                 
spoon = pygame.image.load('spoon.jpg').convert()
raspberry_image = pygame.image.load('raspberry.jpg').convert()

def update_spoon():
    global spoon_x
    global spoon_y
    spoon_x, ignore = pygame.mouse.get_pos()
    screen.blit(spoon, (spoon_x, spoon_y))
    
def check_for_catch():
    global score
    for r in rasps:
        if r.is_caught():
            score += 1

def display(message):
    font = pygame.font.Font(None, 36)
    text = font.render(message, 1, (10, 10, 10))
    screen.blit(text, (0, 0))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    screen.fill((255, 255, 255))
    for r in rasps:
        r.update()
    update_spoon()
    check_for_catch()
    display("Score: " + str(score))
    pygame.display.update()
    clock.tick(30)


