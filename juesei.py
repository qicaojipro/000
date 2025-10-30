import pygame
import random
from time import sleep
from key_jiance import jiance
pygame.init()
pygame.mixer.init()
kaishi=pygame.image.load("something/无标题.png")
class juese:
    def __init__(self,name,age,haogan,tupian):
        self.name=name
        self.age=age
        self.haogan = haogan
        self.tupian = tupian
    def weizhi(self,x,y):
        self.tupian.weizhi=(x,y)

bob=juese(name="bob",age= 18,haogan=50,tupian=kaishi)