'''
Used to control player sprite
'''
import pygame

import constants
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

	# Set speed vector of player
	change_x = 0
	change_y = 0

	# Holds images to present illusion of animation
	walking_frames_l = []
	walking_frames_r = []
	walking_frames_bl = []
	walking_frames_br = []

	# What direction is the player facing?
	direction = "R"

	# List of sprites bumpable against
	level = None

	def __init__(self):

		# Call the parent's constructor
		pygame.sprite.Sprite.__init__(self)

		sprite_sheet1 = SpriteSheet("spriteStand.png")
		image = sprite_sheet1.get_image(34, 19, 32, 73)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_r.append(image)
		sprite_sheet2 = SpriteSheet("spriteWalkL2.png")
		image = sprite_sheet2.get_image(34, 19, 32, 73)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_r.append(image)
		sprite_sheet3 = SpriteSheet("spriteWalkL1.png")
		image = sprite_sheet3.get_image(34, 19, 32, 73)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_r.append(image)
		sprite_sheet4 = SpriteSheet("spriteWalkR2.png")
		image = sprite_sheet4.get_image(34, 19, 32, 73)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_r.append(image)
		sprite_sheet5 = SpriteSheet("spriteWalkR1.png")
		image = sprite_sheet5.get_image(34, 19, 32, 73)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_r.append(image)

		# Load all the right facing images and flip to left
		image = sprite_sheet1.get_image(34, 19, 32, 73)
		image = pygame.transform.flip(image, True, False)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_l.append(image)
		image = sprite_sheet2.get_image(34, 19, 32, 73)
		image = pygame.transform.flip(image, True, False)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_l.append(image)
		image = sprite_sheet3.get_image(34, 19, 32, 73)
		image = pygame.transform.flip(image, True, False)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_l.append(image)
		image = sprite_sheet4.get_image(34, 19, 32, 73)
		image = pygame.transform.flip(image, True, False)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_l.append(image)
		image = sprite_sheet5.get_image(34, 19, 32, 73)
		image = pygame.transform.flip(image, True, False)
		image = pygame.transform.scale(image,(48,110))
		self.walking_frames_l.append(image)

		# Set the image the player starts with
		self.image = self.walking_frames_r[0]

		# Set a reference to rect
		self.rect = self.image.get_rect()


	def update(self):
		'''
		Move player
		'''
		# Gravity
		self.calc_grav()

		# Move left/right
		self.rect.x += self.change_x
		pos = self.rect.x + self.level.world_shift
		if self.direction == "R":
			frame = (pos // 30) % len(self.walking_frames_r)
			self.image = self.walking_frames_r[frame]
		else:
			frame = (pos // 30) % len(self.walking_frames_l)
			self.image = self.walking_frames_l[frame]

		# See if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			# If move right, set player right side to left side of object hit
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				# Vice versa
				self.rect.left = block.rect.right

		# Move up/down
		self.rect.y += self.change_y

		# Check and see if we hit anything
		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:

			# Reset our position based on the top/bottom of object
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom

			# Stop our vertical movement
			self.change_y = 0


	def calc_grav(self):
		'''
		Calculate gravity 9.81 meters per second squared
		'''
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .5

		# If on ground
		if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

	def jump(self):
		'''
		Makes user jump
		'''
		# See if platform below
		self.rect.y += 2
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 2

		# If it is ok to jump, set speed upwards
		if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
			self.change_y = -13

	# Player-controlled movements
	def go_left(self):
		'''
		left arrow
		'''
		self.change_x = -10
		self.direction = "L"

	def go_right(self):
		'''
		right arrow
		'''
		self.change_x = 10
		self.direction = "R"

	def stop(self):
		'''
		stops player movement
		'''
		self.change_x = 0

   