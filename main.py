import pygame
import random
pygame.init()  
pygame.display.set_caption("easy platformer")  # sets the window title
screen = pygame.display.set_mode((800, 800))  # creates game screen
screen.fill((0,0,0))
clock = pygame.time.Clock() #set up clock
gameover = False #variable to run our game loop

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
        pygame.draw.rect(screen, (random.randrange(0,250), random.randrange(0,250),random.randrange(0,250)),(self.xpos, self.ypos, 100, 20))
    def collide(self, x, y):
        if x+20>self.xpos and x<self.xpos+100 and y+20> self.ypos and y < self.ypos + 20:
            return True

#player variables
xpos = 500 #xpos of player
ypos = 200 #ypos of player
vx = 0 #x velocity of player
vy = 0 #y velocity of player
keys = [False, False, False, False] #this list holds whether each key has been pressed
isOnGround = False #this variable stops gravity from pulling you down more when on a platform


p1=Platform(420, 600)
p2 = Platform(100, 750)
while not gameover: #GAME LOOP############################################################
    clock.tick(60) #FPS
    
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
          
    #physics section--------------------------------------------------------------------
    #LEFT MOVEMENT
    if keys[LEFT]==True:
        vx=-3
        direction = LEFT
    elif keys[RIGHT]==True:
        vx=3
        direction = RIGHT

    #turn off velocity
    else:
        vx = 0
        #JUMPING
    if keys[UP] == True and isOnGround == True: #only jump when on the ground
        vy = -8
        isOnGround = False
        direction = UP
    
    

    
    #COLLISION
    if xpos>100 and xpos<200 and ypos+40 >750 and ypos+40 <770:
        ypos = 750-40
        isOnGround = True
        vy = 0
    elif xpos>200 and xpos<300 and ypos+40 >650 and ypos+40 <670:
        ypos = 650-40
        isOnGround = True
        vy = 0
    elif xpos>300 and xpos<400 and ypos+40 >575 and ypos+40 <595:
        ypos = 575-40
        isOnGround = True
        vy = 0
    elif xpos>175 and xpos<275 and ypos+40 >500 and ypos+40 <520:
        ypos = 500-40
        isOnGround = True
        vy = 0
    else:
        isOnGround = False
        


    #stop falling if on bottom of game screen
    if ypos > 760:
        isOnGround = True
        vy = 0
        ypos = 760
    
    #gravity
    if isOnGround == False:
        vy+=.3 #notice this grows over time, aka ACCELERATION
    

    #update player position
    xpos+=vx 
    ypos+=vy
    
  
    # RENDER Section--------------------------------------------------------------------------------
            
    screen.fill((0,0,0)) #wipe screen so it doesn't smear
  
    pygame.draw.rect(screen, (100, 200, 100), (xpos, ypos, 20, 40))
    
    #first platform
    pygame.draw.rect(screen, (200, 0, 100), (100, 750, 100, 20))
    
    #second platform
    pygame.draw.rect(screen, (100, 0, 200), (200, 650, 100, 20))
    #third platform
    pygame.draw.rect(screen, (0, 200, 100), (300, 575, 100, 20))
    #fourth platform
    pygame.draw.rect(screen, (100, 0, 100), (175, 500, 100, 20))
    
    #class platforms
    p1.draw()
    p2.draw()
    pygame.display.flip()#this actually puts the pixel on the screen
    
#end game loop------------------------------------------------------------------------------
pygame.quit()
