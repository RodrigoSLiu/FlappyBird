import pygame
import random
import sys

pygame.init()

# windows settings
title = "Flappy Bird"
size = width, height = 500, 700

# colors
background = (0, 222, 255)
green = (60, 200, 20)
red = (255, 0, 0)
black = (0, 0, 0)
transparent = (255, 0, 0)

# initialization
tubes = []
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)
font = pygame.font.Font("freesansbold.ttf", 62)
text = font.render("Flappy Bird", True, black, background)
death = font.render("  You died", True, black, background)
textRect = text.get_rect()
textRect.center = (width // 2, height // 2)
textCounter = 0
points = 0


class Tube:
    def __init__(self, x, topEnd):
        self.topEnd = random.randint(80, height - 80)
        self.x = x
        self.y = 0
        self.width = 80
        self.height = topEnd
        self.vel = 2
        self.color = green

    def traverse(self):
        self.x -= self.vel

    def getRect(self):
        return pygame.Rect(self.x - self.width, self.y, self.width, self.height), (self.x - self.width, self.height +
                                                                                   200, self.width, height)

    def show_tubes(self):
        pygame.draw.rect(window, self.color, (self.x - self.width, self.y, self.width, self.height))
        pygame.draw.rect(window, black, (self.x - self.width, self.y - 5, self.width, self.height + 5), 2)
        pygame.draw.rect(window, self.color, (self.x - self.width, self.height + 200, self.width, height))
        pygame.draw.rect(window, black, (self.x - self.width, self.height + 200, self.width, height), 2)
        if self.x < 0:
            self.x = 3800


class Bird:
    def __init__(self, x, y, color, radius):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vel = 0
        self.lift = 20
        self.gravity = 0.6
        self.rectSize = self.radius * 2
        self.collision = (self.x - self.radius, self.y - self.radius, self.rectSize, self.rectSize)

    def jump(self):
        self.vel -= self.lift
        if self.vel < -10:
            self.vel = -10
            self.y -= self.lift

    def hit(self, sprite):
        collision = pygame.Rect(round(self.x - self.radius), round(self.y - self.radius), self.rectSize, self.rectSize)
        return collision.colliderect(sprite)

    def getPoint(self, tube):
        return self.x == tube.x

    def show_bird(self):
        self.vel += self.gravity
        self.y += self.vel
        if self.y >= height:
            self.y = height
            self.vel = 0
            Screen()
        elif self.y <= 0:
            self.y = 0
        self.collision = (round(self.x - self.radius), round(self.y - self.radius), self.rectSize, self.rectSize)
        pygame.draw.circle(window, self.color, (round(self.x), round(self.y)), self.radius)


def setup():
    for i in range(15):
        tubeEnd = random.randint(80, height - 280)
        tube = Tube(tubePos[i], tubeEnd)
        tubes.append(tube)


def redrawGameWin():
    global points
    pointStr = font.render(str(points), True, black)

    surface = pygame.Surface((100, 30))
    surface.fill((255, 255, 255))
    surface.blit(pointStr, pygame.Rect(0, 0, 10, 10))
    surface.set_alpha(50)
    window.fill(background)

    flappy.show_bird()
    for tube in tubes:
        tube.show_tubes()
        tube.traverse()
        top, bottom = tube.getRect()
        if flappy.hit(top) or flappy.hit(bottom):
            Screen()
            main()
        if flappy.getPoint(tube):
            points += 1
            window.blit(pointStr, (5, 5))
    window.blit(pointStr, (5, 5))
    pygame.display.update()


def Screen():
    global textCounter
    while True:
        window.fill(background)
        window.blit(text, textRect) if textCounter == 0 else window.blit(death, textRect)
        pygame.display.update()
        for key in pygame.event.get():
            if key.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if key.type == pygame.KEYDOWN:
                if key.key == pygame.K_SPACE:
                    textCounter += 1
                    return


def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    flappy.jump()
                if event.key == pygame.K_r:
                    main()
        redrawGameWin()
        clock.tick(60)


tubePos = dict(zip(range(15), range(width, width + 3600, 250)))
flappy = Bird(50, height // 2, red, 20)
intro = False
setup()
Screen()

main()

pygame.quit()
sys.exit()
