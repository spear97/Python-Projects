
#----------Import all Modules and .py files to Program----------#

#Import All Needed Modules
import pygame, sys, math

#Import Cannon from Cannon.py
from Cannon import Cannon
from CannonBall import CannonBall as cball
from SpaceShip import SpaceShip as ship

#----------Variable and Module Initialization----------#

#Initialize Pygame Modules
pygame.init()

#Initialize and Set height and Width for the Window Resolution
height = 500
width = 800

#Set Up the Window for the Game
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cannon Game")

#Load all Images Needed for Game
cannon_Img = pygame.image.load("Cannon.png")
cannonBall_Img = pygame.image.load("CannonBall.png")
spaceShip_Img = pygame.image.load("SpaceShip.png")

#Stores Cannon and CannonBalls
gameObj = []

#Enemies that Exist in the Scene
enemies = []

#The Direction that Enemies will be moving in
dir = ['Left', 'Right', 'Down']

#Set and Initialize cannon Object
cannon = Cannon(cannon_Img, width/2, (height/2)+125)
gameObj.append(cannon)

#The Speed which the Cannon will be moved at
cannon_vel = 10 

#The Speed which the Cannon will be moved at
cannonBall_vel = 8

#The Speed which the Cannon will be moved at
spaceShip_vel = 5

#Number of CannonBalls that exist in the Game
numBalls = 0

#The Maximum Number of CannonBalls that can Exist in the Game
maxBalls = 8

#The Index that Cannon's Data will be located at
cannonIndex = 0

#Time that delay spawning between CannonBalls
timeSinceFire = 0
cooldown = 5

#----------Function definition for Program----------#

#Add Enemies to List
def spawnEnemies():
    #The Total Number of Enemies of Enemies the list will contain
    total = 10

    #Index for the current of Enemies Appended to the list
    curr = 0

    #The Position the Enemy will be located on the x-Axis
    x = 225

    #The Position the Enemy will be located on the y-Axis
    y = 50

    #While the Total Number of Enemies haven't be added to the list
    while curr < total:

        #Check if 5 Enemies have been placed in a row and is not the first instance
        if curr % 5 == 0 and curr != 0:

            #Move x to the Left-Side of the Screen
            x = 225 

            #Move y to the next corresponding Row by spaceShip_Img height
            y += (spaceShip_Img.get_height() * 1.5)

        #Check if if 5 Enemies have not been placed in a row
        if curr % 5 != 0:

            #Move x to the right by spaceShip_Img width
            x += spaceShip_Img.get_width()

        #Create saucer object
        saucer = ship(spaceShip_Img, x, y)

        #Append saucer to enemies list
        enemies.append(saucer)

        #Increment curr 
        curr += 1

#Blit Enemies from Enemies List
def blitEnemies():

    #Loop through all Enemies in enemies
    for i in enemies:

        #Blit Cannon/CannonBall at position
        win.blit(i.image, i.getPosition())

#Update the Rects of all Enemies
def updateEnemyRect():

     #Loop through all CannonBalls in gameObj
    for i in enemies:

        #Update the rect of the current Index of gameObj
        i.rect = pygame.Rect(i.getPosition(), i.getResolution())

#Blit Cannon and CannonBalls
def blitGameObjImages():

    #Loop through all CannonBalls in gameObj
    for i in gameObj:

        #Blit Cannon/CannonBall at position
        win.blit(i.image, i.getPosition())

#Update the Rects of all Objects
def updateGameObjRects():

    #Loop through all CannonBalls in gameObj
    for i in gameObj:

        #Update the rect of the current Index of gameObj
        i.rect = pygame.Rect(i.getPosition(), i.getResolution())

#Make CannonBalls Fired Move Up
def launchBalls():
    #Set index i to 0 where the first CannonBall is located
    i = 1 

    #Loop through all CannonBalls in gameObj
    while i < len(gameObj):

        #Fill Previous blit of CannonBall as Black
        win.fill((0, 0, 0))

        #Set New Position for CannonBall to Blit at
        gameObj[i].y = gameObj[i].moveUp(cannonBall_vel)

        #Increment i
        i += 1 

#Delete Balls when Going out of Bounds
def cleanupBalls():
   #Check if there are any CannonBalls in the gameObj List
   if len(gameObj) >= 2:

       #Set index i to 1 where the first CannonBall is located
        i = 1  

        #Loop through all CannonBalls in gameObj
        while i < len(gameObj):

            #Check is CannonBall at Index is off-Screen
            if gameObj[i].rect.center[1] < -5:

                del gameObj[i] #Delete CannonBall from gameObj List

            #Increment i
            i += 1

   #Return the Number of CannonBalls that exist in gameObj
   return len(gameObj)-1

#Get the Distance between two points
def distance(a = (int(), int()), b = (int(), int())):
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2)

#Move Each Enemy that is in the game
def moveEnemy():

    #Iterate through enemies
    for i in enemies:

        #Move Enemies Left
        if way == dir[0]:
            i.x = i.moveLeft(win, spaceShip_vel)
            win.fill((0, 0, 0))
            win.blit(i.image, i.getPosition())

        #Move Enemies Right
        if way == dir[1]:
            i.x = i.moveRight(win, spaceShip_vel)
            win.fill((0, 0, 0))
            win.blit(i.image, i.getPosition())

        #Move Enemies Down
        if way == dir[2]:
            i.y = i.moveDown(win, spaceShip_vel)
            win.fill((0, 0, 0))
            win.blit(i.image, i.getPosition())

#Determine if CannonBall and SpaceShip are Colliding and Delete Both 
def enemyCollision():
    #If any CannonBalls have been Spawned
    if len(gameObj) >= 2:

        #Determine if any CannonBall collides with any Enemy
        for i in range(len(gameObj)):

            #If i is cannonIndex skip to next iteration
            if i == cannonIndex:
                continue

            #Compare the Current gameObj index with each Enemies index
            for j in range(len(enemies)):

                #TODO: Change Condition so it reflect center of a rect not top left corner
                if distance(gameObj[i].rect.center, enemies[j].rect.center) < 30:

                    #Deletes CannonBall
                    del gameObj[i] 

                    #Deletes Enemy
                    del enemies[j] 

                    #Returns function and breaks out of loop
                    return 

#Find the Enemy that is closest to the Right Side of the Screen
def getClosestRight():
    closest_dist = 0

    closest_index = 0

    for i in range(len(enemies)):

        if distance(enemies[i].rect.center, (width, enemies.rect.centery)) < closest_dist or closest_dist == 0:

            closest_dist = distance(enemies[i].rect.center, (width, enemies.rect.centery))

            closest_index = i

    return closet_index

#Find the Enemy that is the closest to the Left Side of the Screen
def getClosestLeft():

    closest_dist = 0

    closest_index = 0

    for i in range(len(enemies)):

        if distance(enemies[i].rect.center, (0, enemies.rect.centery)) < closest_dist or closest_dist == 0:

            closest_dist = distance(enemies[i].rect.center, (0, enemies.rect.centery))

            closest_index = i

    return closet_index

#Determine if any Enemy has collided with the Cannon
def CannonCollision():

    for i in range(len(enemies)):

       if distance(gameObj[0].rect.center, enemies[0].rect.center) < 30:

           del gameObj[0]

           break

#----------During the Program's Execution----------#

#Set the way that enemies are moving in
way = dir[1]

#Spawn Enemies into the Game before Games starts running
spawnEnemies()

#While the Game is Running
while 1:

    #Delay the Game for 100ms
    pygame.time.delay(100)

    #Loop throug to see if QUIT needs to be Executed
    for event in pygame.event.get():

       #Check to see if the user has Quit the Game
        if event.type is pygame.QUIT:

            #Exit Game when "X" on the Top-Right Portion of Screen is clicked
            sys.exit(0)

    #Set and Intialize the keys variables that stores all keys
    keys = pygame.key.get_pressed()
        
    #Exit Game using the Escape Key
    if keys[pygame.K_ESCAPE]:
        #Break the Loop to stop Game from still running
        break

    #Fire Cannon
    if keys[pygame.K_SPACE]:

        #Manage the time period in which CannonBalls have been last fired
        #Manage the number of CannonBalls that can exist in the game at one time
        if timeSinceFire == 0 and numBalls < maxBalls:

            #Set Delay
            timeSinceFire = 5 

            #Create Ball Obj
            ball = cball(cannonBall_Img, gameObj[cannonIndex].rect.midtop[0]-10, gameObj[cannonIndex].rect.midtop[1]-50) 

            #Append ball to gameObj List
            gameObj.append(ball)

            #Increment numballs
            numBalls += 1

    #Move the Cannon Left
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:

        #Fill Screen to be Black
        win.fill((0, 0, 0))

        #Move Cannon to the Left
        cannon.x = cannon.moveLeft(win, cannon_vel)

    #Move the Cannon Right
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:

        #Fill Screen to be Black
        win.fill((0, 0, 0))

        #Move Cannon to the Right
        cannon.x = cannon.moveRight(win, cannon_vel)

    #Move all Spawned CannonBalls Up
    launchBalls()

    #Move all Enemies that are in the Game
    moveEnemy()

    #Check if any Spawned CannonBalls are Colliding with SpaceShips
    enemyCollision()

    #Blit Cannon and all Spawned CannonBalls
    blitGameObjImages()

    #Blit all Enemies in game
    blitEnemies()

    #Update all rects of Cannon and Spawned CannonBalls
    updateGameObjRects()

    #Update all rects of Enemies in Game
    updateEnemyRect()

    #Delete all Balls that Move off Screen and updates numBalls
    numBalls = cleanupBalls()

    #Check to see if timeSinceFire needs to be decremented
    if timeSinceFire > 0:

        #Decrement timesSinceFire
        timeSinceFire -= 1

    #Displays Output to Game
    pygame.display.update()

#Destory Memory Allocation that was allocated for the Pygame Module
pygame.quit()