#PlatformLib.py
#Devin Kamer
#4/11/16

"""Used to Creatoe Platforms for the Characters to Interact with."""

import pygame

class Platform(pygame.sprite.Sprite):
    """Creates a Platform with xy coords size and color"""
    def __init__(self, x, y, width, height, color):
        """x y are coords, width(250 max) height are size and color is color... duh"""
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = width
        self.height = height
        self.color = color

        self.collision = []
        for i in range(8):
            self.collision.append(False)

    def check_collision(self, rect):
        """Use Sprite.rect as for rect
            Indexes: 0=Top 1 = Right 2 = Left 3 = Bottom"""
        returnList = []
        self.collision[0] = rect.collidepoint(self.rect.topleft)
        self.collision[1] = rect.collidepoint(self.rect.topright)
        self.collision[2] = rect.collidepoint(self.rect.bottomleft)
        self.collision[3] = rect.collidepoint(self.rect.bottomright)

        self.collision[4] = rect.collidepoint(self.rect.midleft)
        self.collision[5] = rect.collidepoint(self.rect.midright)
        self.collision[6] = rect.collidepoint(self.rect.midtop)
        self.collision[7] = rect.collidepoint(self.rect.midbottom)

        if self.collision[0] or self.collision[1] or self.collision[6]: #Top
            returnList.append(True)
        else:
            returnList.append(False)

        returnList.append(self.collision[4])#Left
        returnList.append(self.collision[5])#Right
        
        if self.collision[2] or self.collision[3] or self.collision[7]: #Bottom
            returnList.append(True)
        else:
            returnList.append(False)
        return returnList

    def get_side_pos(self, side):
        """returns the X coord of the side"""
        if side == "left":
            return self.rect[0]
        elif side == "right":
            return self.rect[2] + self.rect[0]

    def update(self, x, y):
        self.rect.x += x
        self.rect.y = y
        

if __name__ == "__main__":
    pygame.init()

    screenWidth = 1280
    screenHeight = 720
    screen = pygame.display.set_mode([screenWidth, screenHeight])

    platformList = pygame.sprite.Group()
    plat1 = Platform(100, 200, 100, 50, (255, 0, 255))  
    plat2 = Platform(100, 300, 100, 50, (0, 255, 255))
    platformList.add(plat1)
    platformList.add(plat2)

    
    done = False

    clock = pygame.time.Clock()

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        screen.fill((255, 255, 255))

        platformList.draw(screen)

        pygame.display.flip()

        clock.tick(60)

    pygame.quit()
