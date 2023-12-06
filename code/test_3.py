import pytest
import pygame
from ship import Ship

# 使用必要的属性模拟 ai_game 对象
class MockAIGame:
    def __init__(self, screen_size, ship_speed):
        self.screen = pygame.display.set_mode(screen_size)
        self.settings = type('settings', (object,), {'ship_speed': ship_speed})
        self.screen_rect = self.screen.get_rect()

# 使用 fixture 创建 Ship 实例
@pytest.fixture
def ship_fixture():
    pygame.init()
    ai_game = MockAIGame((800, 600), 1.5)
    return Ship(ai_game)

# Ship 的 __init__ 方法的参数化测试
@pytest.mark.parametrize("screen_size, ship_speed, expected_x, expected_y", [
    pytest.param((800, 600), 1.5, 400, 600, id='正常屏幕'),
    pytest.param((1024, 768), 2.0, 512, 768, id='大屏幕'),
    pytest.param((640, 480), 1.0, 320, 480, id='小屏幕'),
])
def test_ship_init(screen_size, ship_speed, expected_x, expected_y):
    # 准备
    ai_game = MockAIGame(screen_size, ship_speed)
    
    # 执行
    ship = Ship(ai_game)
    
# Ship 的 update 方法的参数化测试
@pytest.mark.parametrize("moving_right, moving_left, moving_up, moving_down, expected_position", [
    pytest.param(True, False, False, False, (1.5, 600), id='向右移动'),
    pytest.param(False, True, False, False, (398.5, 600), id='向左移动'),
    pytest.param(False, False, True, False, (400, 598.5), id='向上移动'),
    pytest.param(False, False, False, True, (400, 601.5), id='向下移动'),
    pytest.param(True, True, False, False, (400, 600), id='同时向右向左移动'),
    pytest.param(False, False, True, True, (400, 600), id='同时向上向下移动'),
])
def test_ship_update(ship_fixture, moving_right, moving_left, moving_up, moving_down, expected_position):
    # 准备
    ship_fixture.moving_right = moving_right
    ship_fixture.moving_left = moving_left
    ship_fixture.moving_up = moving_up
    ship_fixture.moving_down = moving_down
    
    # 执行
    ship_fixture.update()

# Ship 的 center_ship 方法的参数化测试
@pytest.mark.parametrize("new_position, expected", [
    pytest.param((10, 10), (400, 600), id='左上角'),
    pytest.param((790, 590), (400, 600), id='右下角'),
])
def test_ship_center_ship(ship_fixture, new_position, expected):
    # 准备
    ship_fixture.rect.x, ship_fixture.rect.y = new_position
    ship_fixture.x, ship_fixture.y = new_position
    
    # 执行
    ship_fixture.center_ship()