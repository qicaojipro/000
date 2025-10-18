import pygame
import random
from time import sleep
pygame.init()
pygame.mixer.init()
def jiance():
    event=pygame.event.poll()
    if event.type==pygame.KEYDOWN:
        return -1,-1
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = event.pos
        button = event.button
        if event.button ==1:
            return mouse_x,mouse_y
    if event.type == pygame.QUIT:
        return -1,-2
    return -1,-3