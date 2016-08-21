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

def text_objects(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, color,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gameDisplay, color,(x,y,w,h))

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
                
        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

        # print(mouse)
                
        gameDisplay.fill(black)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("In the Eyes of a Refugee", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        screen.blit(TextSurf, TextRect)

        button("PLAY", 150,450,100,50,red,"play")
        button("QUIT", 550,450,100,50,red,"quit")
        mouse = pygame.mouse.get_pos()

        # print(mouse)

        pygame.display.update()
        clock.tick(15) 

def main():
<<<<<<< HEAD
    
    pygame.init()

    # Set the height and width of screen
    size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Platformer with sprite sheets")

    # Create player
    player = Player()

    # Create all levels
=======
    """ Main Program """
    # Set the height and width of the screen
    # Create the player
    # Create all the levels
>>>>>>> 5668344183ecd90a5540da47bed95f6b7a637767
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

    #Loop until the user clicks the close button
    done = False

    # Used for FPS
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True 

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

        # Update player
        active_sprite_list.update()

        # Update current level
        current_level.update()

        # If the player nears right side, shift world left
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets nears left side, shift world right
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # Update to next level when reach end of current level
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

        # Limit to 60 FPS
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
