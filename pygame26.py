import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('its aigis time!')
monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

win_size = (1920, 1080)

screen = pygame.display.set_mode(win_size, 0, 32)

display = pygame.Surface((960, 540))


aigis = pygame.image.load('pygame-apcsp26/images/aigis.png')

grass = pygame.image.load('pygame-apcsp26/images/grass.png')

moving_right = False
moving_left = False

aigis_location = [50,50]
aigis_vertical_location = 0

aigis_rect = pygame.Rect(aigis_location[0], aigis_location[1], aigis.get_width(), aigis.get_height())
ouch = pygame.Rect(0,1000,1920,50)

fullscreen = False

while True:
    screen.fill((255,255,255))

    screen.blit(aigis,aigis_location)

    aigis_vertical_location += 0.07
    aigis_location[1] += aigis_vertical_location

    if moving_right == True:
        aigis_location[0] += 3
    if moving_left == True:
        aigis_location[0] -= 3

    aigis_rect.x = aigis_location[0]
    aigis_rect.y = aigis_location[1]

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    pygame.display.update()
    if event.type == KEYDOWN:
        if event.key == K_RIGHT:
            moving_right = True
        if event.key == K_LEFT:
            moving_left = True
    if event.type == KEYUP:
        if event.key == K_RIGHT:
            moving_right = False
        if event.key == K_LEFT:
            moving_left = False 

    surf = pygame.transform.scale(display, win_size)
    screen.blit(display, win_size)
    pygame.display.update()
    clock.tick(60)