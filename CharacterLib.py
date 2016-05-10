#CharacterLib.py
#Devin Kamer
#4/7/16

"""The Bases for the Player and Enemy Classes"""

import pygame

class Character(pygame.sprite.Sprite):
    """Base class for Player and Enemy"""
    def __init__(self, x=200, y=200, hp=1, baseSpeed=1, baseAttack=1):
        super().__init__()
        
        image = pygame.image.load("Images/FatGuy.png").convert()
        image.set_colorkey((255, 255, 255))
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.hp = hp
        self.baseSpeed = baseSpeed
        self.baseAttack = baseAttack

    def __str__(self):
        return self.get_str()

    def update(self, x, y):
        self.rect.x = x * self.baseSpeed
        self.rect.y = y 
        
    def get_str(self):
        text = str(self.image) + " "
        text += str(self.rect) + " "
        text += str(self.hp) + " "
        text += str(self.baseSpeed) + " "
        text += str(self.baseAttack)
        return text

    def getXY(self):
        return (self.rect.x, self.rect.y)

    def get_collision(self):
        return (self.rect.x, self.rect[3] + self.rect.x)

    def set_image(self, image):
        self.image = image
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


if __name__ == "__main__":
    
    WHITE = (255, 255, 255)
    
    pygame.init()
    
    allSpritesList = pygame.sprite.Group()


    screenWidth = 1280
    screenHeight = 720
    screen = pygame.display.set_mode([screenWidth, screenHeight])

    image = pygame.image.load("images/FatGuy.png").convert()
    char = Character(200, 250, 1, 2, 3)
    allSpritesList.add(char)

    myX = 250
    myY = 200
    done = False
    playerMoveX = 0
    playerCurX = 0
    
    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerMoveX = -1
                elif event.key == pygame.K_RIGHT:
                    playerMoveX = 1
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerMoveX = 0

        playerCurX += playerMoveX

        image.set_colorkey(WHITE)
        char.set_image(image)

        char.update(playerCurX, 0)

                
        screen.fill((0, 0, 0))        
        allSpritesList.draw(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()
