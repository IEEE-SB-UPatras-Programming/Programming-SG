import pygame, sys
from settings import *
import level

# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()

level_map = [] #overrides levelmap in settings
with open("level0.txt") as file:
	for line in file:
		level_map.append(line.strip('\n'))


mylevel=level.Level(level_map,screen)
#mylevel.world_shift=-1

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	screen.fill('black')

	mylevel.run()

	pygame.display.update()
	clock.tick(60)