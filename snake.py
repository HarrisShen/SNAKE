import pygame

from settings import Settings
from body import SnakeBody
from food import Food 
from messageboard import MessageBoard
import game_functions as gf
from game_stats import GameStats

def run_game():
	# initialize game and create a screen object
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("SNAKE")
	
	# create a snake
	snake = SnakeBody(ai_settings, screen)
	
	# create food
	foody = Food(ai_settings, screen)
	
	# create game stats
	stats = GameStats(ai_settings)
	
	# create a messageboard
	mb = MessageBoard(ai_settings, stats, screen)
	
	# draw first frame - show start point
	gf.update_screen(ai_settings, stats, screen, snake, foody, mb)
	pygame.time.delay(500)
	
	# main loop
	while True:
		
		# monitor keyboard and mouse event
		gf.check_events(ai_settings, stats, snake)
		if stats.game_active:
			gf.update_screen(ai_settings, stats, screen, 
				snake, foody, mb)
		
run_game()
