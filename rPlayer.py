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
		pos = self.rect.x + 
