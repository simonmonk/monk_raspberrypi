from raspirobotboard import *
import pygame
import sys
from pygame.locals import *

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                rr.forward()
                rr.set_led1(True)
                rr.set_led2(True)
            elif event.key == K_DOWN:
                rr.set_led1(True)
                rr.set_led2(True)
                rr.reverse()
            elif event.key == K_RIGHT:
                rr.set_led1(False)
                rr.set_led2(True)
                rr.right()
            elif event.key == K_LEFT:
                rr.set_led1(True)
                rr.set_led2(False)
                rr.left()
            elif event.key == K_SPACE:
                rr.stop()
                rr.set_led1(False)
                rr.set_led2(False)
