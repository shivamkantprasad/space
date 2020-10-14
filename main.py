import pygame
import sys
import player

class main:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            self.clock.tick(60)
            self.handleinput()
            self.draw()

    def draw(self):
        self.screen.fill((30, 30, 30))
        pygame.display.flip()

    def handleinput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                sys.exit()


run = main(500,500)
run.run()