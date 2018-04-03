__author__ = 'Trenton'
import math, random, sys
import pygame
from pygame.locals import *
# help from https://www.youtube.com/watch?v=Idu8XfwKUao
# exit the program

def col(obstacle, trainer):
    # define display surface
    W, H = 1200, 600
    HW, HH = W / 2, H / 2
    AREA = W * H

    # initialise display
    pygame.display.set_caption("Pixel Perfect Collision")


    # define some colors
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)

    obstacle_mask = pygame.mask.from_surface(obstacle)
    obstacle_rect = obstacle.get_rect()
    ox = HW - obstacle_rect.center[0]
    oy = HH - obstacle_rect.center[1]

    trainer = pygame.image.load("trainer.png").convert_alpha()
    trainer_mask = pygame.mask.from_surface(trainer)
    trainer_rect = trainer.get_rect()


    # main loop


    mx, my = pygame.mouse.get_pos()

    offset = (int(mx - ox), int(my - oy))
    result = obstacle_mask.overlap(trainer_mask, offset)
    if result:
        return True
    else:
        return False


