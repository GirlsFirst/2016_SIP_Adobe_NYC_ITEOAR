import pygame

import constantVars

class SpriteSheet(object):
	#grab images
	sprite_sheet = None

	def __init__(self, filename):

		#load sprite sheet
		self.sprite_sheet = pygame.image.load(filename).convert()

	def getImage(self,width,height):

		#create blank image
		image = pygame.Surface([width,height]).convert()

		#copy sprite from larger sheet
		image.blit(self.sprite_sheet, (0,0), (x,y,width,height))

		#set white as transparent
		image.set_colorkey(constantVars.WHITE)

		return image