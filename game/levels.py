import pygame

import constants
import platforms
import goodSprites
import player


class Level():

	# Sprites used in levels
	platform_list = None
	goodSprite_list = None
	enemy_list = None

	background = None

	# How far level world moved left/right
	world_shift = 0
	level_limit = -1000

	def __init__(self, player):
		'''
		Constructs sprites and player
		'''
		self.platform_list = pygame.sprite.Group()
		self.goodSprite_list = pygame.sprite.Group()
		self.enemy_list = pygame.sprite.Group()
		self.player = player

	def update(self):
		'''
		Update everything on current level
		'''
		self.platform_list.update()
		self.goodSprite_list.update()
		self.enemy_list.update()

	def draw(self, screen):
		'''
		Draw everything in the level
		'''
		# Draw background
		# No shift the background as much as the sprites are shifted for depth
		screen.fill(constants.WHITE)
		screen.blit(self.background,(self.world_shift // 3,0))

		# Draw all the sprite lists
		self.platform_list.draw(screen)
		self.goodSprite_list.draw(screen)
		self.enemy_list.draw(screen)

	def shift_world(self, shift_x):
		'''
		Shift when player moves left/right
		'''

		# Keep track of the shift amount
		self.world_shift += shift_x

		# Go through all the sprite lists and shift
		for platform in self.platform_list:
			platform.rect.x += shift_x

		for goodSprite in self.goodSprite_list:
			goodSprite.rect.x += shift_x

		for enemy in self.enemy_list:
			enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):

	def __init__(self, player):
		'''
		Create level 1
		'''

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("House Level.png")
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -4200


		level = [[platforms.SHELF_PLATFORM, 700, 150], #
				 [platforms.SHELF_PLATFORM, 700, 410], #
				 [platforms.HOME_PLATFORM, 400, 500],
				 [platforms.HOME_PLATFORM, 400, 270],
				 [platforms.SHELF_PLATFORM, 1950, 150], #
				 [platforms.SHELF_PLATFORM, 1950, 410], #
				 [platforms.HOME_PLATFORM, 1650, 280],
				 [platforms.HOME_PLATFORM, 2900, 280],
				 [platforms.SHELF_PLATFORM, 3175, 150], #
				 [platforms.SHELF_PLATFORM, 3175, 410], #
				 [platforms.HOME_PLATFORM, 4150, 500]
				  ]


		# Go through the array above and add platforms
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)


		sprites = [[goodSprites.APPLE_SPRITE, 730,380], # apple BOTTOM ------ FIRST BOTTOM
				   [goodSprites.APPLE_SPRITE, 750, 380],
				   [goodSprites.APPLE_SPRITE, 800, 380],
				   [goodSprites.APPLE_SPRITE, 810, 380],
				   [goodSprites.BOTTLE_SPRITE, 1000,365], # bottle BOTTOM
				   [goodSprites.BOTTLE_SPRITE, 1200, 365],
				   [goodSprites.CAN_SPRITE, 1440, 393], # can BOTTOM
				   [goodSprites.CAN_SPRITE, 1004, 133], # can TOP ------ FIRST TOP
				   [goodSprites.CAN_SPRITE, 1130, 133],
				   [goodSprites.BOTTLE_SPRITE, 1420, 105], # bottle TOP
				   [goodSprites.BOTTLE_SPRITE, 1430, 105],
				   [goodSprites.MED_SPRITE, 2600, 378], # medicine BOTTOM ------ SECOND BOTTOM
				   [goodSprites.MED_SPRITE, 2300, 378],
				   [goodSprites.BANDAID_SPRITE, 2123, 372], # bandaid BOTTOM
				   [goodSprites.BANDAID_SPRITE, 2200, 372],
				   [goodSprites.BANDAID_SPRITE, 2140, 372],
				   [goodSprites.BANDAID_SPRITE, 2370, 372],
				   [goodSprites.BANDAID_SPRITE, 2380, 372],
				   [goodSprites.MONEY_SPRITE, 2100, 130], # money TOP ------ SECOND TOP
				   [goodSprites.MONEY_SPRITE, 2370, 130],
				   [goodSprites.BOTTLE_SPRITE, 3350, 365], # ------ THIRD BOTTOM
				   [goodSprites.BOTTLE_SPRITE, 3300, 365],
				   [goodSprites.BOTTLE_SPRITE, 3600, 365],
				   [goodSprites.APPLE_SPRITE, 3900, 380],
				   [goodSprites.CAN_SPRITE, 3700, 133], # ------ THIRD TOP
				   [goodSprites.CAN_SPRITE, 3800, 133],
				   [goodSprites.CAN_SPRITE, 3780, 133],
				   [goodSprites.CAN_SPRITE, 3320, 133]
					]	

		for good in sprites:
			block = goodSprites.Platform(good[0])
			block.rect.x = good[1]
			block.rect.y = good[2]
			block.player = self.player
			self.goodSprite_list.add(block)


class Level_02(Level):


	def __init__(self, player):
		'''
		Create level 2
		'''

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("landLevel.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -4200



class Level_03(Level):


	def __init__(self, player):
		'''
		Create level 3
		'''

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("Boat Level.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -4200