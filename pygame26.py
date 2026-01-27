import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('cowabunga!')

win_size = (400, 400)

screen = pygame.display.set_mode(win_size, pygame.RESIZABLE)

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == VIDEORESIZE:
        win_size = event.size
        screen = pygame.display.set_mode(win_size, pygame.RESIZABLE)
    pygame.display.update()

pygame.display.update()
clock.tick(60)