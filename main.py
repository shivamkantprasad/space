import pygame
import sys
import player

class main:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.music.load('BackGround.mp3')
        pygame.mixer.music.play(-1)
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load("space.png")
        self.player = player.player(self.width,self.height)
        self.BackGround = pygame.transform.scale(self.BackGround,(width,height))

    def run(self):
        while True:
            self.clock.tick(60)
            self.handleInput()
            self.player.moveBullets()
            self.draw()

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.screen.blit(self.BackGround, (0, 0))
        self.player.drawBullets(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()

    def handleInput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                sys.exit()
        self.player.handelInput(input)


run = main(500,500)
run.run()