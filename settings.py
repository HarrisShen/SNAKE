class Settings:
    def __init__(self):
        # screen settings
        self.screen_width = 270
        self.screen_height = 300
        self.bg_color = (0, 0, 0)
        self.wall_color = (255, 255, 255)

        # snake settings
        self.cube_size = 10
        self.step = 12
        # 'dirs' stands for directions
        self.dirs = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

        # game settings
        self.game_speed = 30
        self.speed_list = [self.game_speed, 0, 0, 0, 0, 0, 0, 0]
        self.acc_factor = 0.75
        self.fill_speed_list()

    def initialize_dynamic_settings(self):
        self.game_speed = 30
        self.speed_list = [self.game_speed, 0, 0, 0, 0, 0, 0, 0]
        self.acc_factor = 0.75
        self.fill_speed_list()

    def fill_speed_list(self):
        for level in range(1, 7):
            self.speed_list[level] = int(self.acc_factor *
                                         self.speed_list[level - 1])
