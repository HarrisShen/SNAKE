import pygame.font

class MessageBoard():
	
	def __init__(self, ai_settings, stats, screen):
		self.screen = screen
		self.screen_rect = screen.get_rect()
		self.ai_settings = ai_settings
		self.stats = stats
		
		self.text_color = (255, 255, 255)
		self.font = pygame.font.SysFont('consolas', 12)
		
		self.prep_score()
		
	def prep_score(self):
		score_str = 'Score:' + str(self.stats.score)
		self.score_image = self.font.render(score_str, False, 
			self.text_color, self.ai_settings.bg_color)
		
		self.score_rect = self.score_image.get_rect()
		self.score_rect.left = 3
		self.score_rect.top = 267
		
	def show_score(self):
		if self.stats.game_active:
			self.screen.blit(self.score_image, self.score_rect)
		
	def show_end(self):
		end_str = 'Game over! Score: ' +\
			str(self.stats.score)
		self.end_image = self.font.render(end_str, False, 
			self.text_color, self.ai_settings.bg_color)
		
		self.end_rect = self.score_image.get_rect()
		self.end_rect.left = 3
		self.end_rect.top = 267
		self.screen.blit(self.end_image, self.end_rect)
