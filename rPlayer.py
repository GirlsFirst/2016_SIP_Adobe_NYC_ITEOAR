import pygame

import constantVars

class player(pygame.sprite.Sprite):

	#speed vector of player
	speedX = 0
	speedY = 0

	#holds images for walk animation
	walkingFramesLeft = []
	walkingFramesRight = []

	#direction player is facing
	direction = "R"

	#sprites we can bump against??
	# level = None

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)

		image = pygame.image.load("walkR1.jpg").convert()
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesRight.append(image)
		image = pygame.image.load("walkR2.jpg").convert()
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesRight.append(image)
		image = pygame.image.load("walkR3.jpg").convert()
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesRight.append(image)
		image = pygame.image.load("walkR4.jpg").convert()
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesRight.append(image)

		image = pygame.image.load("walkR1.jpg").convert()
		image = pygame.transform.flip(image, True, False)
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesLeft.append(image)
		image = pygame.image.load("walkR2.jpg").convert()
		image = pygame.transform.flip(image, True, False)
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesLeft.append(image)
		image = pygame.image.load("walkR3.jpg").convert()
		image = pygame.transform.flip(image, True, False)
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesLeft.append(image)
		image = pygame.image.load("walkR4.jpg").convert()
		image = pygame.transform.flip(image, True, False)
		image.set_colorkey(constantVars.WHITE)
		self.walkingFramesLeft.append(image)

		self.image = self.walkingFramesRight[0]

		self.rect = self.image.get_rect()

	def update(self):

		#gravity
		self.calc_grav()

		#move left/right
		self.rect.x += self.speedX
		pos = self.rect.x + level.worldShift
		if self.direction == "R":
			frame = (pos//30) % len(self.walkingFramesRight)
			self.image = self.walkingFramesRight[frame]
		else:
			frame = (pos//30) % len(self.walkingFramesLeft)
			self.iamge = self.walkingFramesLeft[frame]

		#move up and down
		self.rect.y += self.speedY

	def calc_grav(self):

		#calc effect of gravity
		if self.speedY == 0:
			self.speedY = 1
		else:
			self.speedY += .5

		#is on ground?
		if self.rect.y >= constantVars.screenHeight - self.rect.height and self.speedY >= 0:
			self.speedY = 0
			self.rect.y = constantVars.screenHeight - self.rect.height

	def jump(self):
		self.speedY = -10

	def goLeft(self):
		self.speedX = -10
		self.direction = "L"

	def goRight(self):
		self.speedX = 10
		self.direction = "R"

	def stop(self):
		self.speedX = 0