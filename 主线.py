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
xiaojie=-1
def game_while() :
    global xiaojie
    pygame.display.set_mode((map_wide,map_high))
    pygame.display.set_caption("自制")
    while True :
        w=jiance(0,512,0,256,1)
        if w==0:
            print("yes")
game_while()

