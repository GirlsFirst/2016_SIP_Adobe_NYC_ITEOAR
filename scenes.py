import pygame 

import constantVars

class Scene():

	enemyList = 0

	backgroundImage = None

	#how far world is scrolled left/right
	worldShift = 0
	levelLimit = -1000

	def __init__(self,player):
		self.enemyList = pygame.sprite.Group()
		self.player = player

	def update(self):
		self.enemyList.update()

	def draw(self, screen):
		screen.fill(constantVars.WHITE)
		screen.blit(self.backgroundImage, (self.worldShift // 3,0))

		self.enemyList.draw(screen)

	def shiftWorld(self,shiftX):
		
		#keep track of shift amount
		self.worldShift += shiftX

		#go through sprite list and shift
		for enemy in self.enemyList:
			enemy.rect.x += shiftX

class homeLevel(level):

	def __init__(self,player):

		level.__init__(self,player)

		self.backgroundImage = pygame.image.load("homebg.jpg").convert()
		self.backgroundImage.set_colorkey(constantVars.WHITE)
		self.levelLimit = -2500

		