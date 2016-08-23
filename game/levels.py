import pygame

import constants
import platforms
import player

# levelNow = 0

class Level():

	# Sprites used in levels
	platform_list = None
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
		self.enemy_list = pygame.sprite.Group()
		self.player = player

	def update(self):
		'''
		Update everything on current level'''
		self.platform_list.update()
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

		for enemy in self.enemy_list:
			enemy.rect.x += shift_x

# Create platforms for the level
class Level_01(Level):

	#levelNow = 1

	def __init__(self, player):
		# '''
		# Create level 1
		# '''

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("House Level.png")
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -4200

		# player.image = "girl"

		# levelNow =



		# Type of platform, (x,y) location of specified platform
		# (0,0) is on upper-left
		level = [[platforms.SHELF_PLATFORM, 700, 150],
				 [platforms.SHELF_PLATFORM, 700, 410],
				 [platforms.HOME_PLATFORM, 400, 500],
				 [platforms.HOME_PLATFORM, 400, 270],
				 [platforms.SHELF_PLATFORM, 1950, 150],
				 [platforms.SHELF_PLATFORM, 1950, 410],
				 [platforms.HOME_PLATFORM, 1650, 280],
				 [platforms.HOME_PLATFORM, 2900, 500]
				  ]

		# Type of platform, (x,y) location of specified platform
		# (0,0) is on upper-left
		level = [[platforms.SHELF_PLATFORM, 700, 150],
				 [platforms.SHELF_PLATFORM, 700, 410],
				 [platforms.HOME_PLATFORM, 400, 500],
				 [platforms.HOME_PLATFORM, 400, 270],
				 [platforms.SHELF_PLATFORM, 1950, 150],
				 [platforms.SHELF_PLATFORM, 1950, 410],
				 [platforms.HOME_PLATFORM, 1650, 280],
				 [platforms.HOME_PLATFORM, 2900, 280],
				 [platforms.SHELF_PLATFORM, 3175, 150],
				 [platforms.SHELF_PLATFORM, 3175, 410],
				 [platforms.HOME_PLATFORM, 4150, 500]
				  ]


		# Go through the array above and add platforms
		for platform in level:
			block = platforms.Platform(platform[0])
			block.rect.x = platform[1]
			block.rect.y = platform[2]
			block.player = self.player
			self.platform_list.add(block)

		# Add a custom moving platform
		# block = platforms.MovingPlatform(platforms.STONE_PLATFORM_MIDDLE)
		# block.rect.x = 1350
		# block.rect.y = 280
		# block.boundary_left = 1350
		# block.boundary_right = 1600
		# block.change_x = 1
		# block.player = self.player
		# block.level = self
		# self.platform_list.add(block)


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

		# levelNow = 2


class Level_03(Level):

	#levelNow = 3
	def __init__(self, player):
		'''
		Create level 3
		'''

		# Call the parent constructor
		Level.__init__(self, player)

		self.background = pygame.image.load("Boat Level.png").convert()
		self.background.set_colorkey(constants.WHITE)
		self.level_limit = -4200

		# levelNow = 3