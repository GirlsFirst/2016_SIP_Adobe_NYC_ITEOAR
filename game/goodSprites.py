"""
Manage good sprites
"""
import pygame

from spritesheet_functions import SpriteSheet

# Define platforms from spritesheet

MONEY_SPRITE = (61,54,35,24)
APPLE_SPRITE = (152,59,12,74)
BANDAID_SPRITE = (19,90,14,51)
MED_SPRITE = (73,94,30,42)
BOTTLE_SPRITE = (133,83,32,76)
CAN_SPRITE = (25,184,128,100)

class Platform(pygame.sprite.Sprite):
	'''
	Platforms player interacts with
	'''

	def __init__(self, sprite_sheet_data):
		'''
		Constructs platforms
		'''
		pygame.sprite.Sprite.__init__(self)

		sprite_sheet = SpriteSheet("goodSprites.png")
		# Use sprite sheet image for platforms
		self.image = sprite_sheet.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])

		# self.image = pygame.transform.scale2x(self.image)

		if sprite_sheet_data == BANDAID_SPRITE:
			self.image = pygame.transform.scale(self.image,(11,38))

		if sprite_sheet_data == MED_SPRITE:
			self.image = pygame.transform.scale(self.image,(15,21))

		if sprite_sheet_data == BOTTLE_SPRITE:
			self.image = pygame.transform.scale(self.image,(8,19))

		if sprite_sheet_data == CAN_SPRITE:
			self.image = pygame.transform.scale(self.image,(13,10))

		self.rect = self.image.get_rect()
