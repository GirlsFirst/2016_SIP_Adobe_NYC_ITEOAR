"""
Manage platforms
"""
import pygame

from spritesheet_functions import SpriteSheet

# Define platforms from spritesheet

HOME_PLATFORM = (49,166,81,20)
SHELF_PLATFORM = (0,36,400,20)

class Platform(pygame.sprite.Sprite):
	'''
	Platforms player interacts with
	'''

	def __init__(self, sprite_sheet_data):
		'''
		Constructs platforms
		'''
		pygame.sprite.Sprite.__init__(self)

		sprite_sheet = SpriteSheet("platforms.png")
		# Use sprite sheet image for platforms
		self.image = sprite_sheet.get_image(sprite_sheet_data[0],
											sprite_sheet_data[1],
											sprite_sheet_data[2],
											sprite_sheet_data[3])

		self.image = pygame.transform.scale2x(self.image)

		self.rect = self.image.get_rect()
