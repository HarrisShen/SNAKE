import pygame.font

class MessageBoard():
	
	def __init__(self, ai_settings, stats, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('consolas', 14)
		
		self.left = 5
		self.first_line_top = 267
		self.second_line_top = 281
	
	def show_msg(self, msg_str, sec_msg_str=''):
		self.msg_image = self.font.render(msg_str, False, 
			self.text_color, self.ai_settings.bg_color)
		
		self.msg_rect = self.msg_image.get_rect()
		self.msg_rect.left = self.left
		self.msg_rect.top = self.first_line_top
		self.screen.blit(self.msg_image, self.msg_rect)
		
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
			info_str = 'P-pause, Q-quit'
			self.show_msg(score_str, info_str)
		else:
			score_str = 'Paused, Score:' + str(self.stats.score)
			info_str = 'P-resume, Q-quit'
			self.show_msg(score_str, info_str)
	
	def show_start(self):
		start_str = 'Space/Enter-start'
		info_str = 'Q-quit'
		self.show_msg(start_str, info_str)
		
	def show_end(self):
		end_str = 'Game over! Score: ' +\
			str(self.stats.score)
		info_str = 'R-restart, Q-quit'
		self.show_msg(end_str, info_str)

	def show_status(self):
		if self.stats.game_status == 'game':
			self.show_score()
		elif self.stats.game_status == 'start':
			self.show_start()
		elif self.stats.game_status == 'end':
			self.show_end()
