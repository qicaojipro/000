import pygame
import random
import time
import sys
from key_jiance import jiance

pygame.init()
pygame.mixer.init()
#########def########

map_high=512
map_wide=1024
gameScreen=pygame.display.set_mode((map_wide,map_high))
font=pygame.font.Font(None,36)
text_color=(255,255,255)
kaishi=pygame.image.load("something/无标题.png")
yi_yi=pygame.image.load("something/1.1.png")
yi_er=pygame.image.load("something/1.2.png")

class juese:
    def __init__(self,name,age,tupian):
        self.name1=name
        self.age1=age
        self.image1 = pygame.image.load(tupian).convert_alpha()
        self.image2 = pygame.transform.scale(self.image1, (256, 512))
        self.weizhi=self.image2 .get_rect()
    def xianshi(self,x,y):
        self.weizhi.topleft=(x,y)
        self,gameScreen.blit(self.image2 ,self.weizhi)
class scence:
    def __init__(self,background_image,duihua):
        self.background=pygame.image.load(background_image ).convert()
        self.background=pygame.transform .scale(self.background,(map_wide ,map_high ))
        self.duihua=duihua
        self.duihuageshu=0
    def display(self):
        gameScreen.blit(self.background ,(0,0))
        text_xianshi=font.render(self.duihua[self.duihuageshu], True, (0, 0, 0 ))
        gameScreen.blit(text_xianshi ,(50,map_high-100))
    def huanci(self):
        """换词"""
        self.duihuageshu +=1
        if self.duihuageshu >=len(self.duihua):
            return True
        return False

class guanli:
    def __init__(self,changjin):
        self.scenes=changjin
        self.dangqiangeshu=0
    def dangqianchangjin(self):
        return self.scenes[self.dangqiangeshu]
    def next_changjin(self):
        if self.dangqiangeshu<len(self.scenes)-1:
            self.dangqiangeshu+=1
            return True
        else:
            print("game over")
            pygame.quit()
            sys.exit()
scence1=scence("something/无标题.png",["yes","第二句","第三局","第一章没了"])
scence2=scence("something/1.1.png",["di2一句","第2二句","第2三局","第2章没了"])
guanliyixia=guanli([scence1 ,scence2 ])
clock=pygame.time.Clock()
running=True
while running:
    gameScreen.fill((0,0,0))
    cj=guanliyixia .dangqianchangjin()
    cj.display()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                changjin_done=cj.huanci()
                if changjin_done:
                    guanliyixia.next_changjin()
    pygame.display.flip()
    clock.tick(30)





