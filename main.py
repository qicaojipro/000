import pygame
import random
from time import sleep
from key_jiance import jiance
pygame.init()
pygame.mixer.init()
#########def########
main_game=[[0,1,2]]
map_high=512
map_wide=1024
zhangjie=0
xiaojie=0
gameScreen=pygame.display.set_mode((map_wide,map_high))
kaishi=pygame.image.load("something/无标题.png")
def game_while() :
    global xiaojie,zhangjie
    pygame.display.set_caption("自制")
    gameScreen.blit(kaishi, (0, 0))
    while True :
        pygame.display.update()
game_while()

