#!/user/bin/env python
# -*-coding:utf-8 -*-


class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """"初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        """飞船设置"""
        # 移动速度
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        """"子弹设置"""
        self.bullet_speed_factor = 1
        self.bullet_width = 5
        self.bullet_height = 10
        self.bullet_color = (0, 255, 0)
        self.bullets_allowed = 5

        """外星人设置"""
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

        """以1.1倍的速度加快游戏的节奏"""
        self.speedup_scale = 1.1
        # 外星人点数的提高速度
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

        """击落一个外星人记分"""
        self.alien_points = 10

    def initialize_dynamic_settings(self):
        """初始化游戏进行变量的设置"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 0.2

        # fleet_direction为1表示向右移动，-1表示向左移动
        self.fleet_direction = 1

        """击落一个外星人记分"""
        self.alien_points = 10

    def increase_speed(self):
        """提高速度设置和击中外星人的点数"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.bullets_allowed = int(self.bullets_allowed * self.speedup_scale)
