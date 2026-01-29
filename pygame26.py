import pygame, sys, os

clock = pygame.time.Clock()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('its aigis time!')
monitor_size = (pygame.display.Info().current_w, pygame.display.Info().current_h)

win_size = (1920, 1080)

screen = pygame.display.set_mode(win_size, 0, 32)

aigis = pygame.image.load('pygame-apcsp26/images/aigis.png')

moving_right = False
moving_left = False

aigis_location = [50,50]
aigis_vertical_location = 0

aigis_rect = pygame.Rect(aigis_location[0], aigis_location[1], aigis.get_width(), aigis.get_height())
ouch = pygame.Rect(0,1000,10000,100)

fullscreen = False

while True:
    screen.fill((255,255,255))

    screen.blit(aigis,aigis_location)

    if aigis_location[1] > win_size[1]-aigis.get_height():
        aigis_vertical_location = -aigis_vertical_location
    else:
        aigis_vertical_location += 0.1
    aigis_location[1] += aigis_vertical_location

    if moving_right == True:
        aigis_location[0] += 4
    if moving_left == True:
        aigis_location[0] -= 4

    aigis_rect.x = aigis_location[0]
    aigis_rect.y = aigis_location[1]

    if aigis_rect.colliderect(ouch):
        pygame.draw.rect(screen, (255,0,0), ouch)
    else:
        pygame.draw.rect(screen, (0,0,0), ouch)

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

pygame.display.update()
clock.tick(60)