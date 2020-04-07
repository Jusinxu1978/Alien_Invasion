import pygame
from settings import Settings

class Bullet():
    def __init__(self,screen,settings,ship,bullet_type,bullet_speed,bullet_track):
        #初始化飞船并设置其初始位置
        self.screen = screen
        
        #初始化飞船配置参数
        self.settings = settings
        self.bullet_type = bullet_type
        self.bullet_speed = bullet_speed
        self.bullet_track = bullet_track
        
        #加载飞船图像并获取其外接矩形
        if self.bullet_type == self.settings.bullet_type[0]:
            self.image = pygame.image.load('images/bullet_common.png')
        else:
            self.image = pygame.image.load('images/bullet_common.png')

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #将每艘新飞船放在屏幕底部中央
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.bottom - ship.rect.height - 1
        
        #移动轨迹
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        #
        
    def blitme(self):
        #在指定位置绘制飞船
        self.screen.blit(self.image,self.rect)
        
    def move(self):
        if self.bullet_track == self.settings.bullet_track[0]:
            self.rect.bottom -= self.bullet_speed
        
    def overScreen(self):
        if self.rect.left < self.screen_rect.left or self.rect.right > self.screen_rect.right or self.rect.top < self.screen_rect.top or self.rect.bottom > self.screen_rect.bottom:
            return True
        else:
            return False