import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        
        #Import assets and animation

        self.image = pygame.Surface((74,56))
        self.image.fill('red')
        self.rect = self.image.get_rect(topleft = pos)

