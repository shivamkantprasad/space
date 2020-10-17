import pygame
from util import *
import math


class alien:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 50, 50)
        self.alienIMG = pygame.image.load("Turtle.png")
        self.alienIMG = pygame.transform.scale(self.alienIMG, (self.rect.width, self.rect.height))
        self.bullets = []
        self.ShootCoolDown = 200
        self.exploadsound = pygame.mixer.Sound("expload.wav")

    def Draw(self, screen, bullets):
        # pygame.draw.rect(screen,(255,255,255),self.rect)
        screen.blit(self.alienIMG, self.rect)
        self.drawBullets(screen, bullets)

    def move(self, direction):
        self.rect.x += direction[0]
        self.rect.y += direction[1]

    def collied(self, bullets):
        for x in bullets:
            distance = listsub(self.rect.center, x)
            distance = math.sqrt(distance[0]**2 + distance[1]**2)
            if distance <= 30:
                pygame.mixer.Sound.play(self.exploadsound)
                return [True, x]
        return [False]

    def shoot(self,playerPos,bullets):
        self.ShootCoolDown -= 1
        if abs(self.rect.centerx - playerPos[0]) < 50 and self.ShootCoolDown <= 0:
            bullets.append([self.rect.centerx,self.rect.centery-20])
            self.ShootCoolDown = 200
        return bullets

    def moveBullets(self,bullets):
        if len(bullets) > 0:
            for x in bullets:
                x[1] += 4
        return bullets

    def drawBullets(self, screen, bullets):
        if len(bullets) > 0:
            for x in bullets:
                pygame.draw.circle(screen, (255, 60, 60), x, 10)