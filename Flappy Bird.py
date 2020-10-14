import pygame
import random
import time
import sys
pygame.init()

#windows settings
title = "Flappy Bird"
size = width, height = 500, 700

#colors
background = (0, 222, 255)
green = (60, 200, 20)
black = (0, 0, 0)

#initialization
tubes = []
clock = pygame.time.Clock()
window = pygame.display.set_mode(size)
pygame.display.set_caption(title)
font = pygame.font.Font("freesansbold.ttf", 62) 
text = font.render("Flappy Bird", True, green, background) 
textRect = text.get_rect()  
textRect.center = (width // 2, height // 2)

class Tube:
	def __init__(self, x,topEnd):
		self.x = x
		self.y = 0
		self.width = 80
		self.height = topEnd
		self.vel = 2
		self.color = green

	def traverse(self):
		self.x -= self.vel

	def show(self):
		pygame.draw.rect(window, self.color, (self.x - self.width, self.y, self.width, self.height))
		pygame.draw.rect(window, black, (self.x - self.width, self.y - 5, self.width, self.height + 5), 2)
		pygame.draw.rect(window, self.color, (self.x - self.width, self.height + 200, self.width, height))
		pygame.draw.rect(window, black, (self.x - self.width, self.height + 200, self.width, height), 2)
		if self.x < 0:
			self.x = 3600
			self.topEnd = random.randint(80, height - 80)


class Bird:
	def __init__(self, x, y, vel, gravity):
		self.x = x
		self.y = y
		self.vel = vel
		self.gravity = gravity


def setup():
	for i in range(15):
		tubeEnd = random.randint(80, height - 280)
		tube = Tube(tubePos[i], tubeEnd)
		tubes.append(tube)


def redrawGameWin():
	window.fill(background)
	for i in tubes:
		i.show()
		i.traverse()
	pygame.display.update()


def introScreen():
	while True:
		window.fill(background)
		window.blit(text, textRect)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					return

tubePos = dict(zip(range(15), range(width, width + 3600, 250)))
run = True
intro = False
setup()
introScreen()

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	redrawGameWin()
	clock.tick(60)

pygame.quit()
sys.exit()