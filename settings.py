class Settings():
	
	def __init__(self):
		# screen settings
		self.screen_width = 270
		self.screen_height = 300
		self.bg_color = (0, 0, 0)
		self.wall_color = (255, 255, 255)
		self.cube_size = 10
		self.step = 12
		# 'dirs' stands for directions 
		self.dirs = {
			'up': (0, -1),
			'down': (0, 1),
			'left': (-1, 0),
			'right': (1, 0)}
		self.speed_of_level = [1000, 750, 560, 420, 315, 235, 175, 133]
		self.initialize_dynamic_settings()
		
	def initialize_dynamic_settings(self):
		self.game_speed = 1000
