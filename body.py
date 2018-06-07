import random

import pygame

from settings import Settings
from game_stats import GameStats

class SnakeBody():
	
	def __init__(self, ai_settings, screen):
		self.screen = screen		
		# set body pos, size and color
		self.rect =  pygame.Rect(0, 0, 
			ai_settings.cube_size, ai_settings.cube_size)
		self.gen_random_pos()
		self.color = (0, 255, 0)
		self.cnt = 0
		self.crt_dir = random.choice(list(ai_settings.dirs.values()))
		self.nxt_dir = self.crt_dir
		self.footstep = []
		self.body = []
		self.first_cnt = True
	
	def update(self, ai_settings):
		if self.cnt == ai_settings.game_speed:
			self.crt_dir = self.nxt_dir
			self.footstep.insert(0, (self.rect.left, self.rect.top))
			if len(self.footstep) > 400:
				self.footstep.pop()
			self.rect.left += ai_settings.step * self.crt_dir[0]
			self.rect.top += ai_settings.step * self.crt_dir[1]
			self.cnt = 0
		elif self.cnt < ai_settings.game_speed:
			self.cnt += 1
	
	def drawme(self, ai_settings, stats):
		# draw the snake body
		pygame.draw.rect(self.screen, self.color, self.rect)
		if stats.score > 0:
			for step in self.footstep[:stats.score]:
				step_rect = pygame.Rect(step[0], step[1],
					ai_settings.cube_size, ai_settings.cube_size)
				pygame.draw.rect(self.screen, self.color, step_rect)
		
	def get_pos(self):
		return (self.rect.left, self.rect.top)
		
	def gen_random_pos(self):
		# generate a random position for snake
		self.rect.x = 10 + 12 * random.randint(0, 20)
		self.rect.y = 10 + 12 * random.randint(0, 20) 
	
	def gen_good_random_pos(self):
		# generate a position that won't easily die
		return 0

	def eat_food(self, ai_settings, stats, foody, mb):
		# eat the food just when step into it
		if self.get_pos() == foody.get_pos():
			foody.update(stats, self)
			stats.score += 1
			mb.prep_score()
			stats.update_level()
			stats.update_game_speed(ai_settings)
	
	def hit_wall(self, stats, mb):
		if self.rect.left < 10 or self.rect.top < 10\
			or self.rect.left > 250 or self.rect.top > 250:
			print("Press Q to quit")
			stats.game_active = False
			mb.show_end()
	
	def hit_self(self, stats, mb):
		for step in self.footstep[:stats.score]:
			if self.get_pos() == step:
				print("Press Q to quit")
				stats.game_active = False
				mb.show_end()
				
	def up_down(self, ai_settings):
		if self.crt_dir == ai_settings.dirs['up']:
			return True
		elif self.crt_dir == ai_settings.dirs['down']:
			return True
		else:
			return False
