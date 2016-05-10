#EnemyLib.py
#Devin Kamer
#4/8/16

"""Uses CharacterLib to create Enemies"""

import pygame
from CharacterLib import Character
import random

class Enemy(Character):

    def __init__(self, x, y, hp, attack, speed, name):
        Character.__init__(self, x, y, hp, speed, attack)
        self.name = name
        self.myX = random.randrange(100, 150)
        self.origX = self.myX
        self.dir = 'l'

    def __str__(self):
        text = self.get_str()
        text += " " + self.name
        return text

    def update(self):

        if self.dir == 'l':
            if self.myX > 0:
                self.rect.x -= self.baseSpeed
                self.myX -= self.baseSpeed
            else:
                self.dir = 'r'
                self.image = pygame.transform.flip(self.image, True, False)
                self.image.set_colorkey((255, 255, 255))
        elif self.dir == 'r':
            if self.myX < self.origX:
                self.rect.x += self.baseSpeed
                self.myX += self.baseSpeed
            else:
                self.dir = 'l'
                self.image = pygame.transform.flip(self.image, True, False)

    def check_collision(self, rect):
        return rect.collidepoint(self.rect.midtop)
        
        

if __name__ == "__main__":
    
    WHITE = (255, 255, 255)
    
    pygame.init()
    
    allSpritesList = pygame.sprite.Group()


    screenWidth = 1280
    screenHeight = 720
    screen = pygame.display.set_mode([screenWidth, screenHeight])
    char = Enemy(500, 500, 5, 1.0, 2, "Test Guy")
    allSpritesList.add(char)


    myX = 250
    myY = 200
    done = False
    playerMoveX = 0
    
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            

        char.update()

                
        screen.fill(WHITE)        
        allSpritesList.draw(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
