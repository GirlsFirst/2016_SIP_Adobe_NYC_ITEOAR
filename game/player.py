"""
Used to control player sprite
"""
import pygame

import constants
# import levels
# from platform_scroller import levelNow

# from platforms import MovingPlatform
from spritesheet_functions import SpriteSheet

class Player(pygame.sprite.Sprite):

    # Set speed vector of player
    change_x = 0
    change_y = 0

    # Holds images to present illusion of animation
    walking_frames_l = []
    walking_frames_r = []

    # What direction is the player facing?
    direction = "R"

    # List of sprites bumpable against
    level = None

    def __init__(self):
        '''
        Constructs player
        '''
        # def player1 (self):
        #     sprite_sheet1 = SpriteSheet("boat0.png")
        #     image = sprite_sheet1.get_image(29,165,230,49)
        #     image = pygame.transform.scale2x(image)
        #     self.walking_frames_r.append(image)
        #     self.walking_frames_l.append(image)
        #     sprite_sheet2 = SpriteSheet("boat1.png")
        #     image = sprite_sheet2.get_image(30,168,228,42)
        #     image = pygame.transform.scale2x(image)
        #     self.walking_frames_r.append(image)
        #     self.walking_frames_l.append(image)
        #     sprite_sheet3 = SpriteSheet("boat2.png")
        #     image = sprite_sheet3.get_image(29,165,230,49)
        #     image = pygame.transform.scale2x(image)
        #     self.walking_frames_r.append(image)
        #     self.walking_frames_l.append(image)
        #     sprite_sheet2 = SpriteSheet("boat1.png")
        #     image = sprite_sheet2.get_image(30,168,228,42)
        #     image = pygame.transform.scale2x(image)
        #     self.walking_frames_r.append(image)
        #     self.walking_frames_l.append(image)

        # def player2 (self):
        sprite_sheet1 = SpriteSheet("spriteStand.png")
        image = sprite_sheet1.get_image(34, 19, 32, 73)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        sprite_sheet2 = SpriteSheet("spriteWalkL2.png")
        image = sprite_sheet2.get_image(34, 19, 32, 73)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        sprite_sheet3 = SpriteSheet("spriteWalkL1.png")
        image = sprite_sheet3.get_image(34, 19, 32, 73)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        sprite_sheet4 = SpriteSheet("spriteWalkR2.png")
        image = sprite_sheet4.get_image(34, 19, 32, 73)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)
        sprite_sheet5 = SpriteSheet("spriteWalkR1.png")
        image = sprite_sheet5.get_image(34, 19, 32, 73)
        image = pygame.transform.scale2x(image)
        self.walking_frames_r.append(image)

        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet1.get_image(34, 19, 32, 73)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet2.get_image(34, 19, 32, 73)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet3.get_image(34, 19, 32, 73)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet4.get_image(34, 19, 32, 73)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)
        image = sprite_sheet5.get_image(34, 19, 32, 73)
        image = pygame.transform.flip(image, True, False)
        image = pygame.transform.scale2x(image)
        self.walking_frames_l.append(image)

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        # Load all the right facing images into list



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

            # if isinstance(block, MovingPlatform):
            #     self.rect.x += block.change_x

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

# class Boat(pygame.sprite.Sprite):
#     """ This class represents the bar at the bottom that the player
#     controls. """

#     # -- Attributes
#     # Set speed vector of player
#     change_x = 0
#     # change_y = 0

#     # This holds all the images for the animated walk left/right
#     # of our player
#     walking_frames_bl = []
#     walking_frames_br = []

#     # What direction is the player facing?
#     direction = "R"

#     # List of sprites we can bump against
#     level = None

#     # -- Methods
#     def __init__(self):
#         """ Constructor function """

#         # Call the parent's constructor
#         pygame.sprite.Sprite.__init__(self)

#         # Load all the right facing images into a list
#         sprite_sheet1 = SpriteSheet("boat0.png")
#         image = sprite_sheet1.get_image(29,165,230,49)
#         self.walking_frames_br.append(image)
#         self.walking_frames_bl.append(image)
#         sprite_sheet2 = SpriteSheet("boat1.png")
#         image = sprite_sheet2.get_image(30,168,228,42)
#         self.walking_frames_br.append(image)
#         self.walking_frames_bl.append(image)
#         sprite_sheet3 = SpriteSheet("boat2.png")
#         image = sprite_sheet3.get_image(29,165,230,49)
#         self.walking_frames_br.append(image)
#         self.walking_frames_bl.append(image)
#         #add one more?


#         # Set the image the player starts with
#         self.image = self.walking_frames_br[0]

#         # Set a referance to the image rect.
#         self.rect = self.image.get_rect()

#     def update(self):
#         """ Move the player. """
#         # Gravity
#         # self.calc_grav()

#         # Move left/right
#         self.rect.x += self.change_x
#         pos = self.rect.x + self.level.world_shift
#         if self.direction == "R":
#             frame = (pos // 30) % len(self.walking_frames_br)
#             self.image = self.walking_frames_br[frame]
#         else:
#             frame = (pos // 30) % len(self.walking_frames_bl)
#             self.image = self.walking_frames_bl[frame]

#         # See if we hit anything
#         # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         # for block in block_hit_list:
#         #     # If we are moving right,
#         #     # set our right side to the left side of the item we hit
#         #     if self.change_x > 0:
#         #         self.rect.right = block.rect.left
#         #     elif self.change_x < 0:
#         #         # Otherwise if we are moving left, do the opposite.
#         #         self.rect.left = block.rect.right

#         # Move up/down
#         # self.rect.y += self.change_y

#         # Check and see if we hit anything
#         # block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#         # for block in block_hit_list:

#         #     # Reset our position based on the top/bottom of the object.
#         #     # if self.change_y > 0:
#         #     #     self.rect.bottom = block.rect.top
#         #     # elif self.change_y < 0:
#         #     #     self.rect.top = block.rect.bottom

#         #     # Stop our vertical movement
#         #     # self.change_y = 0

#         #     if isinstance(block, MovingPlatform):
#         #         self.rect.x += block.change_x

#     # def calc_grav(self):
#     #     """ Calculate effect of gravity. """
#     #     if self.change_y == 0:
#     #         self.change_y = 1
#     #     else:
#     #         self.change_y += .35

#     #     # See if we are on the ground.
#     #     if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
#     #         self.change_y = 0
#     #         self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

#     # def jump(self):
#     #     """ Called when user hits 'jump' button. """

#     #     # move down a bit and see if there is a platform below us.
#     #     # Move down 2 pixels because it doesn't work well if we only move down 1
#     #     # when working with a platform moving down.
#     #     self.rect.y += 2
#     #     platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
#     #     self.rect.y -= 2

#     #     # If it is ok to jump, set our speed upwards
#     #     if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
#     #         self.change_y = -10

#     # Player-controlled movement:
#     def go_left(self):
#         """ Called when the user hits the left arrow. """
#         self.change_x = -6
#         self.direction = "L"

#     def go_right(self):
#         """ Called when the user hits the right arrow. """
#         self.change_x = 6
#         self.direction = "R"

#     def stop(self):
#         """ Called when the user lets off the keyboard. """
#         self.change_x = 0
