import pygame
from random import randint

class Star:
    """表示单个星星的类"""
    def __init__(self, ai_game, star_count=100):
        """初始化星星并设置其初始位置"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        # 加载星星图片并获取矩形区域
        self.image = pygame.image.load('images/star.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = randint(0, self.settings.screen_width)
        self.rect.y = randint(0, self.settings.screen_height)
        # 计算星星速度以确保它们在相同的时间内移动
        self.speed = ai_game.settings.star_speed_factor * (star_count / ai_game.settings.star_count) + 1


    def update(self):
        """更新星星的位置"""
        self.rect.y += 0.1

    def draw_star(self):
        """在屏幕上绘制星星"""
        self.screen.blit(self.image, self.rect)
