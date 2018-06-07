class GameStats():
	
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.score = 0
		self.level = 1
		self.game_active = True
		self.game_status = 'start'
		self.status = ['start', 'active', 'end']
		
	def update_level(self):
		if self.score < 5:
			return
		elif self.score < 10:
			self.level = 2
		elif self.score < 20:
			self.level = 3
		elif self.score < 40:
			self.level = 4
		elif self.score < 80:
			self.level = 5
		elif self.score < 160:
			self.level = 6
		elif self.score < 320:
			self.level = 7
		elif self.score <= 400:
			self.level = 8
			
	def update_game_speed(self, ai_settings):
		ai_settings.game_speed = ai_settings.speed_of_level[self.level]
