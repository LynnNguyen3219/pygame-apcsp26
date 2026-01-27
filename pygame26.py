import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('cowabunga!')
monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

win_size = (400, 400)

screen = pygame.display.set_mode(win_size, pygame.RESIZABLE)

fullscreen = False

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    if event.type == VIDEORESIZE:
        if not fullscreen:
            screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
    pygame.display.update()
    if event.type == KEYDOWN:
        if event.key == K_f:
            fullscreen = not fullscreen
        if fullscreen:
            screen = pygame.display.set_mode(monitor_size, pygame.FULLSCREEN)
        else:
            screen = pygame.display.set_mode((screen.get_width(), screen.get_height()), pygame.RESIZABLE)

pygame.display.update()
clock.tick(60)