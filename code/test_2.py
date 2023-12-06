import pytest
import pygame
from unittest.mock import Mock
from star import Star

# 使用必要的属性模拟 ai_game 对象
@pytest.fixture
def mock_ai_game():
    mock_game = Mock()
    mock_game.screen = Mock()
    mock_game.settings = Mock()
    mock_game.settings.screen_width = 800
    mock_game.settings.screen_height = 600
    mock_game.settings.star_speed_factor = 1
    mock_game.settings.star_count = 100
    return mock_game

# Star 类初始化的参数化测试
@pytest.mark.parametrize(
    "star_count, expected_speed",
    [
        (50, 1.5),
        (100, 2),
        (200, 3),
        (1, 1.01),
        (0, 1),
    ]
)
def test_star_init(mock_ai_game, star_count, expected_speed):
    # 准备
    pygame.init()

    # 执行
    star = Star(mock_ai_game, star_count)

    # 断言
    assert star.rect.x >= 0 and star.rect.x <= mock_ai_game.settings.screen_width
    assert star.rect.y >= 0 and star.rect.y <= mock_ai_game.settings.screen_height
    assert star.speed == expected_speed

    pygame.quit()

# update 方法的测试
@pytest.mark.parametrize(
    "initial_y, expected_y",
    [
        (0, 0.1),
        (299.9, 300),
        (599.9, 600),
    ]
)
def test_star_update(mock_ai_game, initial_y, expected_y):
    # 准备
    pygame.init()
    star = Star(mock_ai_game)
    star.rect.y = initial_y

    # 执行
    star.update()

    pygame.quit()

# draw_star 方法的测试
def test_draw_star(mock_ai_game):
    # 准备
    pygame.init()
    star = Star(mock_ai_game)
    mock_ai_game.screen.blit = Mock()

    # 执行
    star.draw_star()

    # 断言
    mock_ai_game.screen.blit.assert_called_once_with(star.image, star.rect)

    pygame.quit()
