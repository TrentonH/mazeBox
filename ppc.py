__author__ = 'Trenton'
import math, random, sys
import pygame
from pygame.locals import *
# help from https://www.youtube.com/watch?v=Idu8XfwKUao
# exit the program
def events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
			pygame.quit()
			sys.exit()

# define display surface
W, H = 1920, 1080
HW, HH = W / 2, H / 2
AREA = W * H

# initialise display
pygame.init()
CLOCK = pygame.time.Clock() # this is for updateing
DS = pygame.display.set_mode((W, H))
pygame.display.set_caption("Pixel Perfect Collision")
FPS = 120

# define some colors
BLACK = (0, 0, 0, 255)
WHITE = (255, 255, 255, 255)

obstacle = pygame.image.load("Triforce.png").convert_alpha()
obstacle_mask = pygame.mask.from_surface(obstacle)
obstacle_rect = obstacle.get_rect()
ox = HW - obstacle_rect.center[0]
oy = HH - obstacle_rect.center[1]

green_blob = pygame.image.load("greenblob-59x51.png").convert_alpha()
orange_blob = pygame.image.load("orangeblob-59x51.png").convert_alpha()
blob_mask = pygame.mask.from_surface(green_blob)
blob_rect = green_blob.get_rect()
blob_color = green_blob

# main loop
while True:
	events()

	mx, my = pygame.mouse.get_pos()

	offset = (int(mx - ox), int(my - oy))
	result = obstacle_mask.overlap(blob_mask, offset)
	if result:
		blob_color = orange_blob
	else:
		blob_color = green_blob

	DS.blit(obstacle, (ox, oy))
	DS.blit(blob_color, (mx, my))

	pygame.display.update()
	CLOCK.tick(FPS)
	DS.fill(BLACK)