# importing libraries to python

import pygame, sys, random
from pygame.locals import *   # '*' mark is used to import everything from pygame.locals


# All these variables were generated here as they were used at appropriate place.
# Generating variables required for programming.
PlayerSpeed=7
MaxAddRate=6
MinObstacle=15
MaxObstacle=40
MinSpeed=1
MaxSpeed=6
topScore=0




# All the functions needed in program were written just before they had to be called and then shifted to the start of program
# Defining function to quit Game

def quitfunc():
    pygame.quit()
    sys.exit()


# Condition for quitting the game by pressing Escape key

def KeyPress_QuitCond():
    while True:
        for event in pygame.event.get(): # This gets each event from all events happening which are extracted using .get()

            if event.type == QUIT:
                quitfunc()

            if event.type == KEYDOWN:

                if event.key == K_ESCAPE:
                    quitfunc()
                return


# Defining Function To Display Text On Screen

def TextWriting(text,font,surface,x,y):
    Txtline = font.render(text, 1, '#ffbb33')
    Txtinfo = Txtline.get_rect()
    Txtinfo.topleft = (x, y)
    surface.blit(Txtline, Txtinfo)


# Defining Function for breaking game loop when the player collides with obstacle

def collidecond(playerobj, obstacles):
    for rock in obstacles:

        if playerobj.colliderect(rock['rect']):
            return True

    return False





# Initialising all modules of pygame

pygame.init()

# Setting up Window's width and length
width = 800
height = 750
WindowSize = pygame.display.set_mode((width, height))


# Adding Caption on the title bar

pygame.display.set_caption('Dodger')


# Adding Clock using pygame
# The variable is named as Clocktime because Clock is the attribute of pygame
# So, it is advised not to use clock as variable name.
Clocktime = pygame.time.Clock()


# Making mouse cursor invisible inside the game window
pygame.mouse.set_visible(False)





# Adding fonts, audio, player image, and obstacle image

#font
font = pygame.font.SysFont(None, 100)
font1 = pygame.font.SysFont(None, 52)
font2 = pygame.font.SysFont(None, 45)
font3 = pygame.font.SysFont(None, 20)
font4 = pygame.font.SysFont(None, 27)

#Audio

# Background Music needs to be played continuously so we load the music
pygame.mixer.music.load('bgmusic.wav')
# This music(Misty Dungeon) is taken from PlayOnLoop.com
# Licensed under Creative Commons Attribution 4.0


# The sound played when game is over is at particular time or condition so we store music
gameOverSound = pygame.mixer.Sound('gameover.wav')



#Images
playerImg = pygame.image.load('player.png')   # This player image has been made by my friend "MEDHANSH SINGH"

playerRect = playerImg.get_rect()

ObsImg = pygame.image.load('ObsImg.png')





# Start-Screen
# Displaying Text On Start Screen
TextWriting('Pause: P', font4, WindowSize, 350, 720)

TextWriting('RevCheat: Z', font4, WindowSize, 445, 720)

TextWriting('SlowCheat: X', font4, WindowSize, 570, 720)

TextWriting('Exit: Esc', font4, WindowSize, 700, 720)

TextWriting('Dodger!!!', font, WindowSize, 230, 75)

TextWriting("Don't Go Much Closer To Asteriods!", font2, WindowSize, 145, 180)

TextWriting('Press any key to start', font2, WindowSize, 225, 250)

TextWriting('Use "A or Left Arrow Key" to move to left', font2, WindowSize, 25, 350)

TextWriting('Use "D or Right Arrow Key" to move to right', font2, WindowSize, 25, 400)

TextWriting('Use "W or Up Arrow Key" to move to up', font2, WindowSize, 25, 450)

TextWriting('Use "S or Down Arrow Key" to move to left', font2, WindowSize, 25, 500)

TextWriting('OR', font1, WindowSize, 300, 550)

TextWriting('Use mouse to move the space shuttle', font2, WindowSize, 25, 600)

TextWriting('Music: "Misty Dungeon", from PlayOnLoop.com', font3, WindowSize, 10, 710)

TextWriting('Licensed under Creative Commons By Attribution 4.0', font3, WindowSize, 10, 730)

pygame.display.update()





# Starting Game
# We need to check if pressed key is "Escape" then quit the game so we call "KeyPress_QuitCond" function
KeyPress_QuitCond()

while True:

# Initial Values Of Variables Just After Any Key Is Pressed
# Initial Position Of playerImg

    obstacles = []

    playerRect.topleft = (375, 700)

    LArrow = RArrow = UArrow = DArrow = False

    pause = slowCheat = revCheat = False

    ObstacleCount=0
    score = 0
    pausecount=0

    pygame.mixer.music.play(-1, 0.0)   # Start playing music

    while True:

# Main Game Loop Starts Here

        # Increase Score
        if pausecount==0:
            score += 1

        for event in pygame.event.get():

            if event.type == QUIT:   # It is good practice to check the terminating condition right at start so loop doesn't need to go through many conditional executions.

                 quitfunc()



            # If any key is pressed down then an event konown as "KEYDOWN" is generated.
            # Changing variable values as any key is pressed.
            if event.type == KEYDOWN:

                # Note that here I'm using multiple if blocks and not if-elif block
                # It is so cause if user presses two buttons(For Eg. UpArrow And LeftArrow) simultaneously then the effect should be added
                # The python reads the keyboard inputs in only 'Ordinal Value' of a character(alphabets).

                if event.key == ord('p'):
                    if pause == True:
                        pause = False
                        pausecount=0
                    else:
                        pause = True
                        pausecount=1

                if event.key == ord('z'):

                    revCheat = True

                if event.key == ord('x'):

                    slowCheat = True

                if event.key == K_LEFT or event.key == ord('a'):

                    RArrow = False

                    LArrow = True

                if event.key == K_RIGHT or event.key == ord('d'):

                    LArrow = False

                    RArrow = True

                if event.key == K_UP or event.key == ord('w'):

                    DArrow = False

                    UArrow = True

                if event.key == K_DOWN or event.key == ord('s'):

                    UArrow = False

                    DArrow = True



            # If any key is released then an event konown as "KEYUP" is generated.
            # Changing variable values as any key is released.
            if event.type == KEYUP:

                if event.key == ord('z'):

                    revCheat = False

                    score = 0

                if event.key == ord('x'):

                    slowCheat = False

                    score = 0

                if event.key == K_ESCAPE:

                        quitfunc()


                if event.key == K_LEFT or event.key == ord('a'):

                    LArrow = False

                if event.key == K_RIGHT or event.key == ord('d'):

                    RArrow = False

                if event.key == K_UP or event.key == ord('w'):

                    UArrow = False

                if event.key == K_DOWN or event.key == ord('s'):

                    DArrow = False



            # Whenever mouse is moved, then a event known as "MOUSEMOTION" is generated.
            if event.type == MOUSEMOTION and pause==False:

                 # The playerObj should move according to position of mouse.

                playerRect.move_ip(event.pos[0] - playerRect.centerx, event.pos[1] - playerRect.centery)





         # Moving player according to key presses.
        if pause==False:
            if LArrow and playerRect.left > 0:

                playerRect.move_ip(-1 * PlayerSpeed, 0)

            if RArrow and playerRect.right < width:

                playerRect.move_ip(PlayerSpeed, 0)

            if UArrow and playerRect.top > 0:

                playerRect.move_ip(0, -1 * PlayerSpeed)

            if DArrow and playerRect.bottom < height:

                playerRect.move_ip(0, PlayerSpeed)





        # If the playerObj moves using keyboard then mouse pointer should also follow the playerObj.
        pygame.mouse.set_pos(playerRect.centerx, playerRect.centery)





        # Adding new obstacles
        if pause==False and slowCheat==False and revCheat==False:
            ObstacleCount += 1

        if ObstacleCount == MaxAddRate:
            ObstacleCount = 0

            ObstacleSize = random.randint(MinObstacle, MaxObstacle)

            AddedObstacle = {
                        'rect': pygame.Rect(random.randint(0, width - ObstacleSize), 0 - ObstacleSize, ObstacleSize, ObstacleSize),

                        'speed': random.randint(MinSpeed, MaxSpeed),

                        'surface': pygame.transform.scale(ObsImg, (ObstacleSize, ObstacleSize)),

                        }

            obstacles.append(AddedObstacle)





        # Moving the obstacles.
        for asteroid in obstacles:

            if pause==False and slowCheat==False and revCheat==False:
                asteroid['rect'].move_ip(0, asteroid['speed'])

            elif revCheat and pause==False:

                asteroid['rect'].move_ip(0, -5)

            elif slowCheat and pause==False:

                 asteroid['rect'].move_ip(0, 1)

            elif pause:
                asteroid['rect'].move_ip(0,0)
                pausecount=1





         # Removing Obstacles that exceed windowlength
        for asteroid in obstacles[:]:

            if asteroid['rect'].top > height:

                obstacles.remove(asteroid)





        # Adding BackGround Colour
        WindowSize.fill('#000000')





        # Draw the score and top score.
        TextWriting('Score: %s' % (score), font1, WindowSize, 10, 0 )

        TextWriting(' Top Score: %s' % (topScore), font1, WindowSize, 10 ,40)





        # Draw the player's rectangle
        WindowSize.blit(playerImg, playerRect)


        # Dispaying every obstacle on screen
        for asteroid in obstacles:

            WindowSize.blit(asteroid['surface'], asteroid['rect'])


        pygame.display.update()





        # Checking if player collides with asteroid
        if collidecond(playerRect, obstacles):

            if score > topScore:

                topScore = score # set new top score

            break



        # Setting Frames per second
        Clocktime.tick(40)





    # Game Over screen is displayed
    pygame.mixer.music.stop()

    gameOverSound.play()

    TextWriting('GAME OVER', font1, WindowSize, 250, 250)

    TextWriting('Press a key to play again.', font2, WindowSize, 175, 300)

    pygame.display.update()

    KeyPress_QuitCond()

    gameOverSound.stop()