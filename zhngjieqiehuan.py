import pygame
import random
from time import sleep
from key_jiance import jiance
from main import zhangjie,xiaojie,kaishi,gameScreen
pygame.init()
pygame.mixer.init()
def youxi():
    global zhangjie,xiaojie
    x, y = jiance()
    if x == -1 and y == -2:
        pygame.quit()
    if zhangjie == 0:
        if 294 < x < 722:
            if 337 < y < 389:
                zhangjie = zhangjie + 1
                print("next")
            elif 430 < y < 481:
                print(1)
                pygame.quit()
    if zhangjie == 1:
        gameScreen.blit(kaishi, (0, 0))
        print(1)
