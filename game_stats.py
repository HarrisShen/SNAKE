from math import log

class GameStats():
	
	def __init__(self):
		self.high_score = 0
		self.game_status = 'start'
		self.status = ['start', 'game', 'confirm', 'end']
		self.initialize_dynamic_stats()
	
	def initialize_dynamic_stats(self):
		self.score = 0
		self.level = 0	
		self.game_active = False	
		
	def update_level(self):		
		if self.score < 5:
			self.level = 0
		elif self.score >= 5:
			self.level = int(log(self.score/5, 2)) + 1
			
	def update_game_speed(self, ai_settings):
		ai_settings.game_speed = ai_settings.speed_list[self.level]
