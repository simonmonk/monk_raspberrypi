import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((256, 256))
pygame.display.set_caption('Caption')

ball_tile = pygame.image.load('ball.jpg').convert()

graph_rect = ball_tile.get_rect()

rows = int(256 / graph_rect.height) + 1
columns = int(256 / graph_rect.width) + 1

for y in xrange(rows):
    for x in xrange(columns):
        if x == 0 and y > 0:
            graph_rect = graph_rect.move([-(columns -1) * graph_rect.width, graph_rect.height])
            if x > 0:
                graph_rect = graph_rect.move([graph_rect.width, 0])
            screen.blit(ball_tile, graph_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit();
