import random

import pygame

from settings import Settings

class Food():
	
	def __init__(self, ai_settings, screen):
		self.screen = screen
		# set food pos, size and color
		self.rect =  pygame.Rect(10, 10, 
			ai_settings.cube_size, ai_settings.cube_size)
		self.color = (255, 0, 0)
		
		self.rect.left = 10 + 12 * random.randint(0, 20)
		self.rect.top = 10 + 12 * random.randint(0, 20)
		
	def drawme(self):
		# draw the food cube
		pygame.draw.rect(self.screen, self.color, self.rect)
		
	def get_pos(self):
		return (self.rect.left, self.rect.top)

	def create_new(self, stats, snake_body):
		self.rect.left = 10 + 12 * random.randint(0, 20)
		self.rect.top = 10 + 12 * random.randint(0, 20)
		# if food overlaps snake, then re-create food
		for step in snake_body.footstep[:stats.score]:
			if self.get_pos() == step:
				self.create_new(stats, snake_body)
