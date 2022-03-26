import pygame, sys

# Pygame setup
pygame.init()

screen_width = 300
screen_height = 200

screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
box = pygame.Rect(10,50,50,50)
screen.fill('black')
pygame.draw.rect(screen,"red",box)

while True:
	#Check exit
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	#Get input
	keys = pygame.key.get_pressed()
	if keys[pygame.K_RIGHT]:
		box.x += 5
	elif keys[pygame.K_LEFT]:
		box.x += -5

	#Clear Screen
	screen.fill('black')
	#draw rect
	pygame.draw.rect(screen,"red",box)

	#Update
	pygame.display.update() #https://www.pygame.org/docs/ref/display.html#pygame.display.update
	clock.tick(60)