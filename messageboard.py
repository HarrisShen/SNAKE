import pygame.font

class MessageBoard():
	
	def __init__(self, ai_settings, stats, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		# text settings
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('consolas', 14)
		# msg board are positioned right under the game frame
		self.left = 5
		self.first_line_top = 267
		self.second_line_top = 281
	
	def show_msg(self, msg_str, sec_msg_str=''):
		# prepare (first) line of message
		self.msg_image = self.font.render(msg_str, False, 
			self.text_color, self.ai_settings.bg_color)
		
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.left = self.left
		self.msg_rect.top = self.first_line_top
		# show (first) line
		self.screen.blit(self.msg_image, self.msg_rect)
		
		# show second line, if provided
		if sec_msg_str:
			self.sec_msg_image = self.font.render(sec_msg_str, False, 
				self.text_color, self.ai_settings.bg_color)
		
			self.sec_msg_rect = self.sec_msg_image.get_rect()
			self.sec_msg_rect.left = self.left
			self.sec_msg_rect.top = self.second_line_top
			self.screen.blit(self.sec_msg_image, self.sec_msg_rect)
		
	def show_score(self):
		if self.stats.game_active:
			score_str = 'Score:' + str(self.stats.score) +\
				', High:' + str(self.stats.high_score)
			info_str = 'Space-pause, Esc-quit'
			self.show_msg(score_str, info_str)
		else:
			score_str = 'Paused, Score:' + str(self.stats.score)
			info_str = 'Space-resume, Esc-quit'
			self.show_msg(score_str, info_str)
			
	def show_confirm(self):
		cnfm_str = 'Sure to quit? Score:' + str(self.stats.score)
		info_str = 'Enter-quit, Esc-resume'
		self.show_msg(cnfm_str, info_str)
		
	def show_start(self):
		start_str = 'Enter-start'
		info_str = 'Q-quit'
		self.show_msg(start_str, info_str)
		
	def show_end(self):
		end_str = 'Game over! Score: ' +\
			str(self.stats.score)
		info_str = 'Space-restart, Esc-quit'
		self.show_msg(end_str, info_str)

	def show_status(self):
		if self.stats.game_status == 'game':
			self.show_score()
		elif self.stats.game_status == 'confirm':
			self.show_confirm()
		elif self.stats.game_status == 'start':
			self.show_start()
		elif self.stats.game_status == 'end':
			self.show_end()
