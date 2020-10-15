import pygame
from util import *


class player:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.player = pygame.Rect(width / 2 - 25, height - 60, 50, 50)
        self.bullets = []
        self.bullet_sound = pygame.mixer.Sound("shoot.wav")
        self.playerIMG = pygame.image.load("player.png")
        self.playerIMG = pygame.transform.scale(self.playerIMG,(self.player.width,self.player.height))

    def draw(self, screen):
        # pygame.draw.rect(screen, (255, 255, 255), self.player,1)
        screen.blit(self.playerIMG, self.player)

    def handelInput(self, input):
        for event in input:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.bullets.append([self.player.centerx,self.player.centery-20])
                    pygame.mixer.Sound.play(self.bullet_sound)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.x -= 4
            self.player.x = clamp(self.player.x, 0, self.width - self.player.width)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.x += 4
            self.player.x = clamp(self.player.x, 0, self.width - self.player.width)

    def moveBullets(self):
        if len(self.bullets) > 0:
            for x in self.bullets:
                x[1] -= 4

    def drawBullets(self, screen):
        if len(self.bullets) > 0:
            for x in self.bullets:
                pygame.draw.circle(screen, (60, 60, 255), x, 10)
