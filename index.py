#Imports
import pygame #import pygame library, before you run this make sure this was installed with "pip install pygame"
import random #import randomm number library, which helps to generate random values
import math #import math library, for math shit

#Initialize stuff
pygame.init() #initialize pygame, which basically starts the game thing
screen = pygame.display.set_mode((800,600)) #creates a window that's 800 wide 600 tall. The reason why it isn't just pygame.set_mode is that the set_mode function is under pygame.display (helps organization)
pygame.display.set_caption("Tutorial") #change the title of the window

#Creates a player character
pImg = pygame.image.load('elder.png') #loads in an image representing a player image, feel free to replace with a more attractive image if possible, but make sure it's under the same directory as this python file
def player(x, y): #a function that draws a player based on the location you want them to spawn at
    screen.blit(pImg,(x,y)) #function that draws an image given the loaded image variable and the location as a tuple
pX = 400-pImg.get_size()[0]/2 #400 is half of 800, which is the width of the window, but we don't make it exactly 400 because the location of the image is based on it's top left corner, and we have to account for the width of the image when centering it. To understand what i mean feel free to make this variable just 400. Also we divide the width by two as we want to center it, delete the /2 to understand ig.
pY = 300-pImg.get_size()[1]/2 #read above
pChangeX = 0 #a variable for the current rate of change in the x axis, to be used later
pChangeY = 0 #read above

#Creates a doubloon
dImg = pygame.image.load('doubloon.png') #loads in image of doubloon
dImg = pygame.transform.scale(dImg,(200,200)) #scales it down so it isn't so big
def doubloon(x, y): #makes a function to generate a doubloon
    screen.blit(dImg,(x,y)) #draws image of doubloon
dX = random.randint(0,800) #random coordinate within the boundaries of the window. ik i didn't account for the size of the image do it yourself if it bothers you so much
dY = random.randint(0,600) #same as above

#Checks for Collision
def isCollided(px_py,dx_dy): #checks for a collision between the player and the doubloon, where the inputs are tuples :O
    px, py=px_py #takes the variable (which is a tuple) and splits it into two variables for coordinates
    dx, dy=dx_dy #same as above
    distance = math.sqrt((px-dx)**2+(py-dy)**2) #distance formula but in code form, to measure if it collided
    if(distance<=200): #checking if the distance between doubloon and player is within a certain threshold for collision, in this case 200 pix. Also didn't account for width of the image i still don't care.
        return True #returns True if the collision did happen
    else:
        return False #false if not

#Pygame basically runs off the concept that theres a constantly updating and running Game Loop, where the states are consistently checked and updated
running = True #initialize a variable that sets the current state to running
while running: #Game loop, runs when 'running' variable is true
    screen.fill((0, 255, 255)) #creates a solid color, basically how drawing things on screen works is that whatevers drawn later in the code is drawn over what's drawn earlier. So since this is the earliest thing drawn it's the background

    #Event Checking
    for event in pygame.event.get(): #pygame.event.get() is basically a list of all of the events that have occured that still need to be processed since the last iteration of the loop ended, and you run through each event to process it.
        if event.type == pygame.QUIT: #checks if the event is a QUIT event, meaning that the user pressed the X key on the game window
            running = False #since running turns False, the loop stops running, the window closes, and thus the game stops
        if event.type == pygame.KEYDOWN: #checks if the event is due to a keyboard key being pressed down
            print("key pressed") #just a print to the console to check if pygame actually registered a keypress
            if event.key == pygame.K_LEFT: #if the key pressed is the left key
                print("left arrow pressed") #it outputs something to the console just so you know it worked
                pChangeX = -1 #and sets the rate of change in the x direction to negative 1. Since PyGame works on a Game Loop every iteration it subtracts 1 from the current position
            if event.key == pygame.K_RIGHT:
                print("right arrow is pressed")
                pChangeX = 1
            if event.key == pygame.K_DOWN:
                print("down arrow pressed")
                pChangeY = 1
            if event.key == pygame.K_UP:
                print("up arrow is pressed")
                pChangeY = -1
        if event.type == pygame.KEYUP: #Once the key is released it stops changing direction
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT: #checks if the key that was released was left or right
                print("left or right key released")
                pChangeX = 0 #and changes the rate of change to be 0 to stop movement horizontally
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP: #checks if key that was released was up or down
                print("up or down key released")
                pChangeY = 0 #and changes the rate of change to be 0 to stop movement vertically

    #Checking if the character hit the borders of the window
    if pY+pChangeY>=600-pImg.get_size()[1] or pY+pChangeY<=0: #Checks if the current position of the character, plus the amount it would move if we let it, is crossing the right or left side of the window border respectively
        pChangeY = 0; #stops it from moving any further if so
    if pX+pChangeX>=800-pImg.get_size()[1] or pX+pChangeX<=0: #see above
        pChangeX = 0;
    pX += pChangeX #updates the current position by an amount to move in the x direction
    pY += pChangeY #see above
    player(pX, pY) #draws the player at position
    doubloon(dX, dY)
    if isCollided((pX,pY),(dX,dY)): #checks if there is a collision between the player and doubloon by measuring distance, inputs are tuples
        dX = random.randint(0, 800) #if it collided it randomly generates an x and y coordinate
        dY = random.randint(0, 600)
        doubloon(dX, dY) #and draws another doubloon in that random location
    pygame.display.update() #every time a drawing is done or a change is made the display needs to be updated with the changes.