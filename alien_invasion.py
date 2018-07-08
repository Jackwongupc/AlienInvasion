#!/user/bin/env python
# -*-coding:utf-8 -*-

import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStates
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例,并创建计分牌
    stats = GameStates(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一搜飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人编组
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏循环主体
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens,
                         bullets, play_button)


if __name__ == '__main__':
    run_game()
