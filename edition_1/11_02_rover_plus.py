from raspirobotboard import *
import pygame
import sys
from pygame.locals import *

rr = RaspiRobot()

pygame.init()
screen = pygame.display.set_mode((640, 480))
font = pygame.font.SysFont("arial", 64)

pygame.display.set_caption('RaspiRobot')
pygame.mouse.set_visible(0)

dir_stop, dir_forward, dir_back, dir_left, dir_right = range(5)
bot_direction = dir_stop


def update_distance():
    dist = get_range()
    if dist == 0:
        return
    message = 'Distance: ' + str(dist) + ' in'
    text_surface = font.render(message, True, (127, 127, 127))
    screen.fill((255, 255, 255))
    screen.blit(text_surface, (100, 100))
    
    w = screen.get_width() - 20
    proximity = ((100 - dist) / 100.0) * w
    if proximity < 0:
        proximity = 0
    pygame.draw.rect(screen, (0, 255, 0), Rect((10, 10),(w, 50)))    
    pygame.draw.rect(screen, (255, 0, 0), Rect((10, 10),(proximity, 50)))
    pygame.display.update()

def get_range():
    try:
        dist = rr.get_range_inch()
    except:
        dist = 0
    return dist

def collision_check():
    dist = get_range()
    if dist > 0 and dist < 10 and bot_direction == dir_forward:
        go_stop()

def go_stop():
    global bot_direction
    bot_direction = dir_stop
    rr.stop()
    rr.set_led1(False)
    rr.set_led2(False)
    
def go_forward():
    global bot_direction
    bot_direction = dir_forward
    rr.forward()
    rr.set_led1(True)
    rr.set_led2(True)

def go_back():
    global bot_direction
    bot_direction = dir_back
    rr.set_led1(True)
    rr.set_led2(True)
    rr.reverse()

def go_right():
    global bot_direction
    bot_direction = dir_right
    rr.set_led1(False)
    rr.set_led2(True)
    rr.right()

def go_left():
    global bot_direction
    bot_direction = dir_left
    rr.set_led1(True)
    rr.set_led2(False)
    rr.left()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                go_forward()
            elif event.key == K_DOWN:
                go_back()
            elif event.key == K_RIGHT:
                go_right()
            elif event.key == K_LEFT:
                go_left()
            elif event.key == K_SPACE:
                go_stop()
    collision_check()
    update_distance()
    time.sleep(0.1)
