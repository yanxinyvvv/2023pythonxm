import json

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 读取最高分
        self.high_score = self.load_high_score()

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def update_high_score(self):
        """更新最高分"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def load_high_score(self):
        """从文件中加载最高分"""
        try:
            with open('E:\\2023pythonxm\\code\\score.txt') as f:
                high_score = json.load(f)
        except FileNotFoundError:
            return 0
        else:
            return high_score

    def save_high_score(self):
        """将最高分保存到文件中"""
        with open('E:\\2023pythonxm\\code\\score.txt', 'w') as f:
            json.dump(self.high_score, f)
