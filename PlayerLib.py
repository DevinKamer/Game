#Player.py
#Devin Kamer
#4/8/16

"""Class for the Player Character"""

import pygame
from CharacterLib import Character

class Player(Character):
    """Player Sprite the User Controlls"""

    def __init__(self, x=50, y=575, weapon="Brussle"):
        """Weapon is Celery, Broccili or Brussle, Default Is Brussle"""
        if weapon == "Celery":
            super().__init__(x, y, 4, 2, 1)
        elif weapon == "Broccli":
            super().__init__(x, y, 4, 3, .75)
        else:
            super().__init__(x, y, 4, 1, 1.25)
        self.weapon = weapon
        
    def __str__(self):
        text = self.get_str()
        text += " " + self.weapon
        return text


if __name__ == "__main__":
    
    WHITE = (255, 255, 255)
    
    pygame.init()
    
    allSpritesList = pygame.sprite.Group()
    char = Player(300, 200, "Broccoli")
    allSpritesList.add(char)

    screenWidth = 1280
    screenHeight = 720
    screen = pygame.display.set_mode([screenWidth, screenHeight])

    myX = 250
    myY = 200
    done = False
    playerMoveX = 0
    
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

        char.update(playerMoveX, 0)

                
        screen.fill(WHITE)        
        allSpritesList.draw(screen)

        clock.tick(60)

        pygame.display.flip()

    pygame.quit()

