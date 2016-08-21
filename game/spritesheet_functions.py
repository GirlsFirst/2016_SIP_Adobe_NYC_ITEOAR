"""
Pull sprites from a sprite sheet
"""
import pygame

import constants

class SpriteSheet(object):
    '''
    Cut out images from sprite sheet
    '''

    sprite_sheet = None

    def __init__(self, file_name):

        # Load sprite sheet
        self.sprite_sheet = pygame.image.load(file_name).convert()


    def get_image(self, x, y, width, height):
        '''
        (x,y) location and width, height from sprite sheet to cut out
        '''

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # White BG becomes transparent
        image.set_colorkey(constants.WHITE)

        # Return image
        return image
