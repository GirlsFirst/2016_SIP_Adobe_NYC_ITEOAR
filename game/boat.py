import pygame
import random

import constants
# import platforms


class level():

	background = None
	world_shift = 0
	level_limit = -1000

	def __init__(self, player):
		self.player = player

	def draw(self,screen):
		screen.fill(constants.BLUE)
		screen.blit(self.background,(self.world_shift // 3,0))

	def shift_world(self, shift_x):
		self.world_shift += shift_x

class boat(level):
	def __init__(self,player):
		level.__init__(self,player)

		self.background = pygame.image.load("water.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -2500

	

