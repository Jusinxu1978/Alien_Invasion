'''
Created on 2020年4月4日

@author: mi
'''
import sys

import pygame
import ship

def check_events(ship):
    #响应键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.constants.QUIT:
            sys.exit()
        elif event.type == pygame.constants.KEYDOWN:
            if event.key == pygame.constants.K_RIGHT:
                #向右移动飞船
                ship.moving_right = True
            elif event.key == pygame.constants.K_LEFT:
                #向右移动飞船
                ship.moving_left = True
            elif event.key == pygame.constants.K_UP:
                #向右移动飞船
                ship.moving_up = True
            elif event.key == pygame.constants.K_DOWN:
                #向右移动飞船
                ship.moving_down = True
        elif event.type == pygame.constants.KEYUP:
            if event.key == pygame.constants.K_RIGHT:
                #向右移动飞船
                ship.moving_right = False
            elif event.key == pygame.constants.K_LEFT:
                #向右移动飞船
                ship.moving_left = False
            elif event.key == pygame.constants.K_UP:
                #向右移动飞船
                ship.moving_up = False
            elif event.key == pygame.constants.K_DOWN:
                #向右移动飞船
                ship.moving_down = False
            
def update_screen(ai_settings,screen,ship):
    #更新屏幕上的图像，并切换到新屏幕
#     if ship.moving_right == True:
#         ship.rect.centerx +=1
#     if ship.moving_left == True:
#         ship.rect.centerx -=1
#     if ship.moving_up == True:
#         ship.rect.centery -=1
#     if ship.moving_down == True:
#         ship.rect.centery +=1
    ship.move()
    
    #每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #让最近绘制的屏幕可见
    pygame.display.flip()