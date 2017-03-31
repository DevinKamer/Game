#testGame.py
#Devin Kamer
#4/14/16

"""The Main Runtime for the Game"""

from Tkinter import *
from EnemyLib import Enemy
from PlayerLib import Player
from PlatformLib import Platform
from ScreenLoaderLib import ScreenLoader
import pygame
import os

class Application(Frame):
    """A Tets Main Menu GUI"""
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #Creates Label
        Label(self,
              text = "Original Game: Doughnut Steal"
              ).grid(row = 0, column = 0, columnspan = 3)


        self.inputs = StringVar()
        self.inputs.set(None)
        inputs = ["Keyboard", "JoyStick"]
        for c in range(0, 2):
            Radiobutton(self, text = inputs[c],
                        variable = self.inputs,
                        value = inputs[c]
                        ).grid(row = 2, column = c)

        Button(self,
               text = "Let's Play!",
               command = self.Play
               ).grid(row = 3, column = 0, columnspan = 3)

    def Play(self):
        global choice
        global inputs
        choice = "Celery"
        inputs = self.inputs.get()
        self.quit()
        self.destroy()



# main
"""
Removed for compatibility with python2

root = Tk()
root.title("Main Menu")
app = Application(root)
root.mainloop()
root.iconify()
tryAgain = True
"""
workingDir = os.getcwd()

inputs = "Keyboard"
choice = "Celery"

if inputs == "Keyboard":
    inputs = False   #Changing from str to bool is easier to manage
else:
    pygame.joystick.init()
    inputs = True
    playerJoy = pygame.joystick.Joystick(0)
    playerJoy.init()


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1500, 720)
screen = pygame.display.set_mode(size)

font = pygame.font.SysFont('Calibri', 25, True, False)
 
pygame.display.set_caption("Doughnut Man")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create Characters and Platforms
ScreenChanger = ScreenLoader()

curY = 575

testChar = Player(125, 0, choice)
platform1_1 = Platform(100, 300, 200, 30, BLACK)
platform1_2 = Platform(300, 500, 200, 30, BLACK)
platform1_3 = Platform(600, 100, 200, 30, BLACK)
platform1_4 = Platform(900, 400, 200, 30, BLACK)
platform3_1 = Platform(0, size[1] - 20, 200, 30, BLACK)
platform3_2 = Platform(250, 400, 200, 30, BLACK)
platform3_3 = Platform(500, 200, 200, 30, BLACK)
platform3_4 = Platform(1300, 700, 200, 30, BLACK)
platform3_5 = Platform(1100, 700, 200, 30, BLACK)
enemy1_1 = Enemy(1000, 275, 5, 1, 3, "Guy1")
enemy2_1 = Enemy(1000, 575, 5, 2, 3, "Guy2")
enemy3_1 = Enemy(1250, 575, 5, 2, 3, "Guy3")

background = pygame.transform.scale(pygame.image.load(workingDir + "/Images/trees0.png"),
                                     (size[0], size[1]))
background2 = pygame.transform.scale(pygame.image.load(workingDir + "/Images/Lose.png"),
                                     (size[0], size[1]))
background3 = pygame.transform.scale(pygame.image.load(workingDir + "/Images/BonusRoom.png"),
                                     (size[0], size[1]))

for i in range(0, 8):
    pieceOfGround = Platform(200 * i, size[1] - 20, 200, 50, BLACK)
    ScreenChanger.Add_Objects(pieceOfGround, 1, "plat")
    ScreenChanger.Add_Objects(pieceOfGround, 2, "plat")
    

    
ScreenChanger.Add_Objects(testChar, 1, "char")

ScreenChanger.Add_Objects(platform1_1, 1, "plat")
ScreenChanger.Add_Objects(platform1_2, 1, "plat")
ScreenChanger.Add_Objects(platform1_3, 1, "plat")
ScreenChanger.Add_Objects(platform1_4, 1, "plat")
ScreenChanger.Add_Objects(platform3_1, 3, "plat")
ScreenChanger.Add_Objects(platform3_2, 3, "plat")
ScreenChanger.Add_Objects(platform3_3, 3, "plat")
ScreenChanger.Add_Objects(platform3_4, 3, "plat")
ScreenChanger.Add_Objects(platform3_5, 3, "plat")
ScreenChanger.Add_Objects(enemy1_1, 1, "enemy")
ScreenChanger.Add_Objects(enemy2_1, 2, "enemy")
ScreenChanger.Add_Objects(enemy3_1, 3, "enemy")

for i in range(1, 5):
    bonusPlat = Platform(0, 180 * i - 20, 200, 50, BLACK)
    ScreenChanger.Add_Objects(bonusPlat, "bonus", "plat")
    for j in range(1, 4):
        bonusEnemy = Enemy(size[0] - (j * 200), 180 * i, 3, 1, 2, "Bonus Guy"\
                           + str(i) + "-" + str(j))
        ScreenChanger.Add_Objects(bonusEnemy, "bonus", "enemy")


# Define some Variables
xSpeed = 0
ySpeed = 0
curX = 50
isJumping = False
allReadyJump = False
gravity = 0
collide = False
grounded = False
numTicks = 0
superRun = False
points = 0

isRunningLeft = False
isRunningRight = False

nomSound = pygame.mixer.Sound(workingDir + "/music/nom.ogg")
hitSound = pygame.mixer.Sound(workingDir + "/music/hit.ogg")
fallSound = pygame.mixer.Sound(workingDir + "/music/Fall.ogg")

img1 = pygame.image.load(workingDir + "/Images/walk1.png").convert()
img = img1
direction = "Right"
pygame.mixer.music.load(workingDir + "/music/Doughnut_Guy_Music.ogg")
pygame.mixer.music.play()
img.set_colorkey(BLACK)


# -------- Main Program Loop -----------
while not done:
    #numTicks += 1
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

            

        elif inputs:
            xSpeed = 0
            
            hatDir = playerJoy.get_hat(0)[0]
            if hatDir < 0 and xSpeed >= 0:
                xSpeed = hatDir * 5 * testChar.baseSpeed
                isRunningLeft = True
                if direction == "right":
                    img = pygame.transform.flip(img, True, False)
                direction = "left"

            elif hatDir > 0 and xSpeed <= 0:
                xSpeed = hatDir * 5 * testChar.baseSpeed
                isRunningRight = True
                if direction == "left":
                    img = pygame.transform.flip(img, True, False)
                direction = "right"

            if hatDir == 0:
                isRunningRight = False
                isRunningLeft = False
                xSpeed = 0
            
            if playerJoy.get_button(2):
                xSpeed += 1 * hatDir * testChar.baseSpeed


            if playerJoy.get_button(0):
                isJumping = True

            else:
                isJumping = False
                allReadyJump = False
                
            

        else:
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and xSpeed >= 0:
                    xSpeed = -5 * testChar.baseSpeed
                    isRunningLeft = True
                    if direction == "right":
                        img = pygame.transform.flip(img, True, False)
                    direction = "left"
                    
                elif event.key == pygame.K_RIGHT and xSpeed <= 0:
                    xSpeed = 5 * testChar.baseSpeed
                    isRunningRight = True
                    if direction == "left":
                        img = pygame.transform.flip(img, True, False)
                    direction = "right"
                    
                elif event.key == pygame.K_SPACE:
                    isJumping = True

                elif event.key == pygame.K_LSHIFT and xSpeed != 0:
                    superRun = True
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    isRunningLeft = False
                    xSpeed = 0
                elif event.key == pygame.K_RIGHT:
                    isRunningRight = False
                    xSpeed = 0

                elif event.key == pygame.K_SPACE:
                    isJumping = False
                    allReadyJump = False

                elif event.key == pygame.K_LSHIFT:
                    superRun = False

            if superRun:
                if direction == "left":
                    xSpeed -= 3
                elif direction == "right":
                    xSpeed += 3

                
 
    # --- Game logic should go here

        

    collide = False
    
    for platform in pygame.sprite.spritecollide(
        testChar, ScreenChanger.Get_Cur_Plat(), False):

        #Testing where they collide
        #Top
        platformCollide = platform.check_collision(testChar.rect)
        if platformCollide[0]:
            collide = True

        #Sides
        if platformCollide[1]:
            xSpeed = 0
            
        if platformCollide[2]:
            xSpeed = 0

                       

    if isJumping and not allReadyJump and collide:
        allReadyJump = True   
        ySpeed = -20
        collide = False
    

    if not collide:
        gravity += .1
        ySpeed += gravity
    else:
        gravity = 0
        ySpeed = 0
        curY -= 1
        


    if curY < - 200 and ScreenChanger.curScreen == 1:
        ScreenChanger.Update_Screen("bonus")
        curX = 50
        curY = 575
        gravity = 0
        ySpeed = 0

    if curY > size[1]:
        curX = 50
        curY = 575
        gravity = 0
        ySpeed = 0
        if ScreenChanger.curScreen == "bonus":
            ScreenChanger.Update_Screen(1)
            pygame.mixer.music.load(workingDir + "/music/Background Music.ogg")
            pygame.mixer.music.play()
        else:
            testChar.hp -= 1
            fallSound.play()

    while curX < 0:
        curX += 1

    if curX > 700:
        if len(ScreenChanger.Get_Cur_Enemy()) == 0:
            
            if ScreenChanger.curScreen == 1:
                ScreenChanger.Update_Screen(2)
            elif ScreenChanger.curScreen == 2:
                ScreenChanger.Update_Screen(3)
            elif ScreenChanger.curScreen == 3:
                ScreenChanger.Update_Screen(1)
                ScreenChanger.Add_Objects(enemy1_1, 1, "enemy")
                ScreenChanger.Add_Objects(enemy2_1, 2, "enemy")
                ScreenChanger.Add_Objects(enemy3_1, 3, "enemy")
            curX = 50
            curY = 575

        else:
            while curX > 700:
                curX -= 1
    
    for i in ScreenChanger.Get_Cur_Enemy():
        i.update()
    
    fatStomp = False
    for i in ScreenChanger.Get_Cur_Enemy():
        if i.check_collision(testChar.rect):
            fatStomp = True
        
    for enemy in pygame.sprite.spritecollide(testChar, ScreenChanger.Get_Cur_Enemy(), fatStomp):
        if not fatStomp:
            curX = 50
            curY = 575
            gravity = 0
            ySpeed = 0
            testChar.hp -= 1
            nomSound.play()
            
        else:
            hitSound.play()
            gravity = 0
            ySpeed = 0
            curY -= 40
            points += 100
            
        
    if testChar.hp <= 0:
        ScreenChanger.Update_Screen("lose")

        

    if ScreenChanger.curScreen != "lose":    
        curX += xSpeed
        curY += ySpeed       
        testChar.update(curX, curY)


    img.set_colorkey(BLACK)
    testChar.set_image(img)


 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.

            
    if type(ScreenChanger.curScreen) == int:
        screen.blit(background, [0, 0])
    else:
        if ScreenChanger.curScreen == "lose":
            screen.blit(background2, [0,0])
        else:
            screen.blit(background3, [0,0])
         
    # --- Drawing code should go here
    ScreenChanger.Draw_Screen(screen)

    text = font.render("Health: " + str(testChar.hp), True, BLACK)
    screen.blit(text, [15, 15])
    pointText = font.render("Points: " + str(points), True, BLACK)
    screen.blit(pointText, [1350, 15])
     
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(120)
 
# Close the window and quit.
pygame.quit()
