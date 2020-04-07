class Settings():
    #存储《外星人入侵》的所有设置的类
    
    def __init__(self):
        #初始化游戏的设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.move_step = 1
        
        #各对象大小
        self.ship_width = 60
        self.ship_height = 90
        
        #子弹类型
        self.bullet_type = ("common","gold","wood","water","fire","soil")
        self.bullet_speed = (1,2,3,4,5)
        self.bullet_track = ("straight_line","bias")
        self.bullet_maxnum = 10
        self.fire_frequency = 50