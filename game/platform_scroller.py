"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/

Main module for platform scroller exampl
From:
http://programarcadegames.com/python_examples/sprite_sheets/

Explanation video: http://youtu.be/czBDKWJqOao

Part of a series:
http://programarcadegames.com/python_examples/f.php?file=move_with_walls_example.py
http://programarcadegames.com/python_examples/f.php?file=maze_runner.py
http://programarcadegames.com/python_examples/f.php?file=platform_jumper.py
http://programarcadegames.com/python_examples/f.php?file=platform_scroller.py
http://programarcadegames.com/python_examples/f.php?file=platform_moving.py
http://programarcadegames.com/python_examples/sprite_sheets/

Game art from Kenney.nl:
http://opengameart.org/content/platformer-art-deluxe

"""

import pygame
import constants
import levels

from player import Player
# from player import Boat
pygame.init()

size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Platformer with sprite sheets")

player = Player()

# Screen Menu stuff not working 
# ignore for now
def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()
 
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 25)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
    gameDisplay.blit(TextSurf, TextRect)
 
    pygame.display.update()
 
    time.sleep(2)
 
    main()
    
    

def button(msg,x,y,w,h,color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, color,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(screen, color,(x,y,w,h))

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("In the Eyes of a Refugee", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        # print(mouse)
                
        screen.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("In the Eyes of a Refugee", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        button("PLAY", 150,450,100,50,red,"play")
        button("QUIT", 550,450,100,50,red,"quit")
        mouse = pygame.mouse.get_pos()

        # print(mouse)

        pygame.display.update()
        clock.tick(15) 

def main():
    """ Main Program """
    # Set the height and width of the screen
    # Create the player
    # Create all the levels
    level_list = []
    # levelNow = 1
    level_list.append(levels.Level_01(player))
    # levelNow = 2
    level_list.append(levels.Level_02(player))
    # levelNow = 3
    level_list.append(levels.Level_03(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 340
    player.rect.y = constants.SCREEN_HEIGHT - player.rect.height
    active_sprite_list.add(player)

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.change_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.change_x > 0:
                    player.stop()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the player gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
game_intro()