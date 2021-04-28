import pygame
import sys
import player
import alien


class main:
    def __init__(self, width, height):
        pygame.init()
        pygame.mixer.music.load('BackGround.mp3')
        pygame.mixer.music.play(-1)
        self.framCrounter = 0
        self.downTimer = -1
        self.alienDirection = [1, 0]
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.BackGround = pygame.image.load("space.png")
        self.player = player.player(self.width, self.height)
        self.BackGround = pygame.transform.scale(self.BackGround, (width, height))
        self.alien = self.spawnAlien()
        self.alienBullets = []
        self.loseSound = pygame.mixer.Sound("loose.wav")
        self.winsound = pygame.mixer.Sound("winsound.ogg")

    def reset(self):
        self.framCrounter = 0
        self.downTimer = -1
        self.alienDirection = [1, 0]
        self.clock = pygame.time.Clock()
        self.alien = self.spawnAlien()
        self.alienBullets = []
        self.player.bullets = []

    def spawnAlien(self):
        alienList = []
        for x in range(int(self.width / 70 - 1)):
            for y in range(3):
                alienList.append(alien.alien((x * 70 + 10), (y * 70 + 10)))
        return alienList

    def moveAlien(self):
        if self.framCrounter % 2 == 0:
            newDirection = -1
            self.downTimer -= 1
            if self.downTimer == 0:
                self.alienDirection[1] = 0
                for x in self.alien:
                    if x.rect.x <= 1:
                        newDirection = [1, 0]
                    elif x.rect.x + x.rect.width >= self.width - 1:
                        newDirection = [-1, 0]
                if newDirection == -1:
                	newDirection = [1, 0]
            for x in self.alien:
                x.move(self.alienDirection)
                if x.rect.x <= 0 and self.downTimer < -1:
                    newDirection = [0, 1]
                    self.downTimer = 35
                if x.rect.x + x.rect.width >= self.width and self.downTimer < -1:
                    newDirection = [0, 1]
                    self.downTimer = 35
            if newDirection != -1:
                self.alienDirection = newDirection

    def killAlien(self):
        for x in range(len(self.alien) - 1, -1, -1):
            if self.alien[x].collied(self.player.bullets)[0]:
                self.player.bullets.remove(self.alien[x].collied(self.player.bullets)[1])
                self.alien.pop(x)

    def drawAlien(self):
        for x in self.alien:
            x.Draw(self.screen, self.alienBullets)

    def draw(self):
        self.screen.fill((30, 30, 30))
        self.screen.blit(self.BackGround, (0, 0))
        self.player.drawBullets(self.screen)
        self.player.draw(self.screen)
        self.drawAlien()
        pygame.display.flip()

    def handleInput(self):
        input = pygame.event.get()
        for event in input:
            if event.type == pygame.QUIT:
                sys.exit()
        self.player.handelInput(input)

    def alienShoot(self):
        if len(self.alien) > 0:
            for x in self.alien:
                self.alienBullets = x.shoot(self.player.player.center,self.alienBullets)

    def alienBulletsMove(self):
        if len(self.alien) > 0:
            self.alienBullets = self.alien[0].moveBullets(self.alienBullets)

    def lose(self):
        if self.player.die(self.alienBullets):
            self.reset()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.loseSound)
            pygame.time.wait(716)
            pygame.mixer.music.unpause()

    def win(self):
        if len(self.alien) == 0:
            self.reset()
            pygame.mixer.music.pause()
            pygame.mixer.Sound.play(self.winsound)
            pygame.time.wait(2166)
            pygame.mixer.music.unpause()

    def run(self):
        while True:
            self.clock.tick(60)
            self.framCrounter += 1
            self.handleInput()
            self.player.moveBullets()
            self.moveAlien()
            self.killAlien()
            self.alienShoot()
            self.alienBulletsMove()
            self.lose()
            self.win()
            self.draw()


run = main(500, 500)
run.run()
