#ScreenLoaderLib.py
#Devin Kamer
#4/18/16

"""The Classes that contain which objects belong on which screen"""

import pygame

class ScreenLoader(object):

    def __init__(self):
        self.curScreen = 1
        self.bossSwitch = False
        self.play = False #For Keeping Track of Music
        self.bonusPlay = False
        self.charGroup = pygame.sprite.Group()
        self.plat1 = pygame.sprite.Group()
        self.enemy1 = pygame.sprite.Group()
        self.plat2 = pygame.sprite.Group()
        self.enemy2 = pygame.sprite.Group()
        self.plat3 = pygame.sprite.Group()
        self.enemy3 = pygame.sprite.Group()
        self.bonusEnemy = pygame.sprite.Group()
        self.bonusPlat = pygame.sprite.Group()

        self.lose = pygame.sprite.Group()

    def Add_Objects(self, sprite, screen, group):
        if screen == 1 and group == "char":
            self.charGroup.add(sprite)
        elif screen == 1 and group == "plat":
            self.plat1.add(sprite)
        elif screen == 1 and group == "enemy":
            self.enemy1.add(sprite)
        
        elif screen == 2 and group == "plat":
            self.plat2.add(sprite)
        elif screen == 2 and group == "enemy":
            self.enemy2.add(sprite)

        elif screen == 3 and group == "plat":
            self.plat3.add(sprite)
        elif screen == 3 and group == "enemy":
            self.enemy3.add(sprite)

        elif screen == "bonus" and group == "plat":
            self.bonusPlat.add(sprite)
        elif screen == "bonus" and group == "enemy":
            self.bonusEnemy.add(sprite)

        elif screen == "lose":
            self.lose.add(sprite)
        

    def Update_Screen(self, screen):
        self.curScreen = screen
        
        if screen == 2 and not self.play:
            pygame.mixer.music.load("music/Background Music.ogg")
            pygame.mixer.music.play(loops=-1)
            self.play = True
        elif screen == "lose" and not self.bossSwitch:
            pygame.mixer.music.load("music/Boss_Music.ogg")
            pygame.mixer.music.play(loops=-1)
            self.bossSwitch = True

        elif screen == "bonus" and not self.bonusPlay:
            pygame.mixer.music.load("music/Music.ogg")
            pygame.mixer.music.play(loops=-1)
            self.bonusPlay = True
            
    def Get_Cur_Plat(self):
        if self.curScreen == 1:
            return self.plat1
        elif self.curScreen == 2:
            return self.plat2
        elif self.curScreen == 3:
            return self.plat3
        elif self.curScreen == "bonus":
            return self.bonusPlat
        else:
            return self.lose

    def Get_Cur_Enemy(self):
        if self.curScreen == 1:
            return self.enemy1
        elif self.curScreen == 2:
            return self.enemy2
        elif self.curScreen == 3:
            return self.enemy3
        elif self.curScreen == "bonus":
            return self.bonusEnemy
        else:
            return self.lose

    def Draw_Screen(self, screen):
        """screen = screen from game"""
        if type(self.curScreen) == int:
            self.charGroup.draw(screen)
            if self.curScreen == 1:
                self.plat1.draw(screen)
                self.enemy1.draw(screen)

            elif self.curScreen == 2:
                self.plat2.draw(screen)
                self.enemy2.draw(screen)

            elif self.curScreen == 3:
                self.plat3.draw(screen)
                self.enemy3.draw(screen)
        else:
            if self.curScreen == "bonus":
                self.charGroup.draw(screen)
                self.bonusPlat.draw(screen)
                self.bonusEnemy.draw(screen)
            else:
                self.lose.draw(screen)
