import pygame
import constants
import levels
from player import Player

pygame.init()

size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)


pygame.display.set_caption("In the Eyes of a Refugee")

pygame.font.init()

player = Player()

# Screen Menu Stuff
def text_objects(text, font):
    textSurface = font.render(text, True, constants.WHITE)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,color,action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, color,(x,y,w,h), 5)
        if click[0] == 1 and action != None:
            if action == "play":
                main()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "instructions":
                game_instructions()
    else:
        pygame.draw.rect(screen, color,(x,y,w,h), 3)

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_intro():
    intro = True
    bg = pygame.image.load("start.gif")

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(constants.WHITE)
        largeText = pygame.font.Font('freesansbold.ttf', 50)
        TextSurf, TextRect = text_objects("In the Eyes of a Refugee", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)


        mouse = pygame.mouse.get_pos()

                
        screen.blit(bg, (0,0))
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("In the Eyes of a Refugee", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
        screen.blit(TextSurf, TextRect)

        button("START", 150,450,100,50,constants.WHITE,"play")
        button("INSTRUCTIONS", 300, 450, 200, 50, constants.WHITE, "instructions")
        button("QUIT", 550,450,100,50,constants.WHITE,"quit")
        mouse = pygame.mouse.get_pos()


        clock = pygame.time.Clock()

        pygame.display.update()
        clock.tick(15) 

def game_instructions():
    instructions = True
    bg = pygame.image.load("waves.png")

    while instructions:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
        screen.fill(constants.WHITE)
        screen.blit(bg, (0,0))

        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf, TextRect = text_objects("Instructions", largeText)
        # Text is centered at the top middle
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/5))
        screen.blit(TextSurf, TextRect)

        button("START", 150,450,100,50,constants.WHITE,"play")
        button("QUIT", 550,450,100,50,constants.WHITE,"quit")
        mouse = pygame.mouse.get_pos()

        clock = pygame.time.Clock()
        pygame.display.update()
        clock.tick(15) 

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, color,(x,y,w,h), 5)
        if click[0] == 1 and action != None:
            if action == "start":
                game_instructions()
            elif action == "quit":
                pygame.quit()
                quit()
            elif action == "play":
                main()

    else:
        pygame.draw.rect(screen, color,(x,y,w,h), 3)

    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def main():

    '''
    Main Program
    '''

    # Create all levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))
    level_list.append(levels.Level_03(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 320
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

        # If the user gets nears left side, shift world right
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

    game_intro()
    game_instructions()
    main()


