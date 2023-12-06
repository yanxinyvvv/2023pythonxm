import pytest
import pygame
from alien import Alien

# 模拟 ai_game 对象以传递给 Alien 类
class MockSettings:
    def __init__(self, alien_speed, fleet_direction):
        self.alien_speed = alien_speed
        self.fleet_direction = fleet_direction

class MockAIGame:
    def __init__(self, screen_width, screen_height, alien_speed, fleet_direction):
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.settings = MockSettings(alien_speed, fleet_direction)

@pytest.fixture
def ai_game_fixture():
    # 设置一个可在测试中重复使用的 fixture
    screen_width = 800
    screen_height = 600
    alien_speed = 1.0
    fleet_direction = 1
    return MockAIGame(screen_width, screen_height, alien_speed, fleet_direction)

@pytest.mark.parametrize("alien_speed,fleet_direction,expected_x", [
    (1.0, 1, 31.0),
    (1.5, -1, 28.5),
])
def test_update(ai_game_fixture, alien_speed, fleet_direction, expected_x):
    # 准备
    ai_game_fixture.settings.alien_speed = alien_speed
    ai_game_fixture.settings.fleet_direction = fleet_direction
    alien = Alien(ai_game_fixture)
    
    # 执行
    alien.update()

@pytest.mark.parametrize("screen_width,screen_height,alien_x,alien_speed,fleet_direction,expected_result", [
    (800, 600, 790, 1.0, 1, True),
    (800, 600, 10, 1.0, -1, True), 
    (800, 600, 799, 1.0, 1, True),
])
def test_check_edges(screen_width, screen_height, alien_x, alien_speed, fleet_direction, expected_result):
    # 准备
    ai_game = MockAIGame(screen_width, screen_height, alien_speed, fleet_direction)
    alien = Alien(ai_game)
    alien.rect.x = alien_x
    alien.x = float(alien_x)
    
    # 执行
    result = alien.check_edges()
    