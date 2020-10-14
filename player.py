import pygame

class player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = pygame.Rect(height-60,width/2-25,50,50)

    def draw(self,screen):
        pygame.draw.rect(screen,(255,255,255),self.player)