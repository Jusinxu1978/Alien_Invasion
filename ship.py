import pygame
from settings import Settings

class Ship():
    def __init__(self,screen,settings):
        #初始化飞船并设置其初始位置
        self.screen = screen
        
        #初始化飞船配置参数
        self.settings = settings
        
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/fight1.png')
        self.image = pygame.transform.scale(self.image,(settings.ship_width ,settings.ship_height))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        #
        
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
        
    def move(self):
        if self.moving_right == True:
            if self.rect.centerx < self.screen_rect.width - self.rect.width/2 :
                self.rect.centerx +=1
        if self.moving_left == True:
            if self.rect.centerx > self.rect.width/2 :
                self.rect.centerx -=1
        if self.moving_up == True:
            if self.rect.centery > self.rect.height/2 :
                self.rect.centery -=1
        if self.moving_down == True:
            if self.rect.centery < self.screen_rect.height - self.rect.height/2 :
                self.rect.centery +=1