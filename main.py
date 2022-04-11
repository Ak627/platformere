import pygame
import random
pygame.init()  
pygame.display.set_caption("platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop
Birb = pygame.image.load('bigbirb.png') #load your spritesheet
Birb.set_colorkey((255,255,255)) #this makes bright pink (255, 0, 255) transparent (sort of)
Back = pygame.image.load('backgroundp.png')
Back.set_colorkey((255,0,255))
#CONSTANTS
LEFT=0
RIGHT=1
UP = 2
DOWN = 3

#platform class

class Platform:
    def __init__ (self, xpos, ypos):#constructor
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.rect(screen, (0, 250,100),(self.xpos, self.ypos, 100, 20), 5)
    def collide(self, x, y):
        if x>self.xpos and x<self.xpos+100 and y+112> self.ypos and y+112 < self.ypos + 20:
            return self.ypos
        else:
            return False

#player variables
Px= 500 #xpos of player
Py= 600 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
frameWidth = 77
frameHeight = 112
RowNum = 1 #for left animation, this will need to change for other animations
frameNum = 0
ticker = 0
#controller = pygame.joystick.Joystick(0) 
#controller.init()
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform

#SOUND
jump = pygame.mixer.Sound('birb.wav')
music = pygame.mixer.music.load('background.wav')
pygame.mixer.music.play(-1)

p1=Platform(420, 600)
p2 = Platform(100, 750)
p3 = Platform(200, 650)
p4 = Platform(300, 575) 
p5  = Platform(175, 500)
p6=Platform(500, 470)
p7 = Platform(360, 430)
p8 = Platform(220, 350)
p9 = Platform(335, 270)
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    #if controller.get_button(0):
       # keys[UP] = True
    #else:
        #keys[UP] = False
    #Input Section------------------------------------------------------------
    for event in pygame.event.get(): #quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True
      
        if event.type == pygame.KEYDOWN: #keyboard input
            if event.key == pygame.K_LEFT:
                keys[LEFT]=True
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=True

            elif event.key == pygame.K_UP:
                keys[UP]=True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[LEFT]=False
            elif event.key == pygame.K_RIGHT:
                keys[RIGHT]=False

            elif event.key == pygame.K_UP:
                keys[UP]=False
                
    
        #vx = controller.get_axis(0)
        #Px += int(vx * 10)
          
    #physics section--------------------------------------------------------------------
    
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT
    
    #turn off velocity
    #else:
        #vx = 0
    else :
        vx*=.95
        
      #JUMPING  
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
        pygame.mixer.Sound.play(jump)
        isOnGround = False

    if vx < 0: #left animation
        RowNum = 1
        # Ticker is a spedometer. We don't want Birb animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>2: 
           frameNum = 0
           
    if vx > 0: #left animation
        RowNum = 0
        # Ticker is a spedometer. We don't want Birb animating as fast as the
        # processor can process! Update Animation Frame each time ticker goes over
        ticker+=1
        if ticker%10==0: #only change frames every 10 ticks
          frameNum+=1
           #If we are over the number of frames in our sprite, reset to 0.
           #In this particular case, there are 10 frames (0 through 9)
        if frameNum>2: 
           frameNum = 0
           
    #stop animation if you slow down enough       
    if vx < .2 and vx >-.2:
        RowNum = 0
        frameNum = 0

        
    #COLLISION
        
    isOnGround = False
    if p1.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p1.collide(Px, Py) - 112 #need to subtract 40

    elif p2.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p2.collide(Px, Py)  - 112
     
    elif p3.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p3.collide(Px, Py)  - 112
        
    elif p4.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p4.collide(Px, Py)  - 112
        
    elif p5.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p5.collide(Px, Py)  - 112
    elif p6.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p6.collide(Px, Py)  - 112
    elif p7.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p7.collide(Px, Py)  - 112
    elif p8.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p8.collide(Px, Py)  - 112
    elif p9.collide(Px, Py) != False:
        isOnGround = True
        vy = 0
        Py = p9.collide(Px, Py)  - 112
    print(isOnGround)
    #stop falling if on bottom of game screen
    if Py + 75 > 760:
        isOnGround = True
        vy = 0
        Py = 760 -75
    
    #gravity
    if isOnGround == False:
        vy+=.3 #notice this grows over time, aka ACCELERATION
    

    #update player position
    Px+=vx 
    Py+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
    
    screen.fill((255,255,255)) #wipe screen so it doesn't smear
    screen.blit(Back, (0,0), (0,0,800,800))
    screen.blit(Birb, (Px, Py), (frameWidth*frameNum, RowNum*frameHeight, frameWidth, frameHeight))    
    
    #class platforms
    p1.draw()
    p2.draw()
    p3.draw()
    p4.draw()
    p5.draw()
    p6.draw()
    p7.draw()
    p8.draw()
    p9.draw()
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
