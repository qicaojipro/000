import pygame
import random
from time import sleep
pygame.init()
pygame.mixer.init()
def jiance(wide_x,wide_y,high_x,high_y,lei_xing):
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            button = event.button
            if wide_x <=mouse_x<=wide_y   :
                if high_x<= mouse_y <=high_y :
                    if lei_xing ==1:
                        return 0
        if event.type == pygame.QUIT:
            pygame.quit()
