import random

import pygame

from settings import Settings
from game_stats import GameStats

class SnakeBody():
	
	def __init__(self, ai_settings, screen):
		self.ai_settings = ai_settings
		self.screen = screen		
		# set snake(cube) size and color
		self.rect =  pygame.Rect(0, 0, 
			ai_settings.cube_size, ai_settings.cube_size)
		self.color = (0, 255, 0)
		
		self.create_new()
	
	def create_new(self):
		# 'cnt' - counter using for control update frequency
		self.cnt = 0
		# direction sets - current and next direction
		self.crt_dir = self.gen_random_dir()
		self.nxt_dir = self.crt_dir
		
		self.gen_good_random_pos()
		# store previous position
		self.last_pos = self.get_pos()
		
		self.footstep = []
		self.body = []
		# status flags
		self.first_frame = True
		self.hit = False
		
	def update(self, ai_settings, stats, foody):
		self.update_pos(ai_settings, stats)
		self.eat_food(ai_settings, stats, foody)
		
	def update_pos(self, ai_settings, stats):
		if self.cnt == ai_settings.game_speed:
			self.crt_dir = self.nxt_dir
			self.last_pos = self.get_pos()
			self.footstep.insert(0, (self.rect.left, self.rect.top))
			# avoid too long array
			if len(self.footstep) > 400:
				self.footstep.pop()
			# move the snake
			self.rect.left += ai_settings.step * self.crt_dir[0]
			self.rect.top += ai_settings.step * self.crt_dir[1]
			# detect hits
			self.hit_end(stats)
			# reset counter
			self.cnt = 0
		elif self.cnt < ai_settings.game_speed:
			self.cnt += 1
	
	def drawme(self, ai_settings, stats):
		# draw the snake head
		pygame.draw.rect(self.screen, self.color, self.rect)
		# draw the snake body
		if stats.score > 0:
			for step in self.footstep[:stats.score]:
				step_rect = pygame.Rect(step[0], step[1],
					ai_settings.cube_size, ai_settings.cube_size)
				pygame.draw.rect(self.screen, self.color, step_rect)
				
	def gen_random_dir(self):
		return random.choice(list(self.ai_settings.dirs.values()))
		
	def gen_random_pos(self):
		# generate a random start position for snake
		self.rect.x = 10 + 12 * random.randint(0, 20)
		self.rect.y = 10 + 12 * random.randint(0, 20) 
	
	def gen_good_random_pos(self):
		# generate a position that won't easily die
		self.gen_random_pos()
		pos_after_ten = (self.rect.x + 120 * self.crt_dir[0],
			self.rect.y + 120 * self.crt_dir[1])
		# if fail, try again
		if pos_after_ten[0] < 10 or pos_after_ten[1] < 10\
			or pos_after_ten[0] > 250 or pos_after_ten[1] > 250:
				self.gen_good_random_pos()
		
	def get_pos(self):
		return (self.rect.left, self.rect.top)

	def eat_food(self, ai_settings, stats, foody):
		# eat the food just when step into it
		if self.get_pos() == foody.get_pos():
			foody.create_new(stats, self)
			stats.score += 1
			# update high score, level and speed, if needed
			if stats.score > stats.high_score:
				stats.high_score = stats.score
			stats.update_level()
			stats.update_game_speed(ai_settings)
	
	def hit_wall(self):
		if self.rect.left < 10 or self.rect.top < 10\
			or self.rect.left > 250 or self.rect.top > 250:
			self.hit = True
	
	def hit_self(self, stats):
		for step in self.footstep[:stats.score]:
			if step == (self.rect.left, self.rect.top):
				self.hit = True
	
	def hit_end(self, stats):
		self.hit_wall()
		self.hit_self(stats)
		# if hits, then game ends
		if self.hit:
			self.rect.left = self.last_pos[0]
			self.rect.top = self.last_pos[1]
			self.footstep.pop(0)
			stats.game_active = False
			stats.game_status = 'end'			
				
	def up_down(self, ai_settings):
		if self.crt_dir == ai_settings.dirs['up']\
			or self.crt_dir == ai_settings.dirs['down']:
			return True
		else:
			return False
