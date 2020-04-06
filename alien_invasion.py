import sys
from turtle import Screen

import pygame

import game_functions as gf
from settings import Settings 
from ship import Ship


def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.base.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #设置背景颜色
    #bg_color = (230,230,230)
    
    #创建一艘飞船
    ship = Ship(screen,ai_settings)
    
    
    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 sys.exit()
        gf.check_events(ship)
                
        #每次循环时重绘屏幕
#         screen.fill(ai_settings.bg_color)
#         ship.blitme()
        gf.update_screen(ai_settings,screen,ship)
        
        #让最近绘制的屏幕可见
        pygame.display.flip()
        
run_game()
        