import sys

import pygame

def check_events(ai_settings, stats, snake_body):
	# monitor keyboard and mouse event
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				sys.exit()
			elif event.key == pygame.K_p:
				stats.game_active = not stats.game_active
			elif event.key == pygame.K_r:
				if stats.game_active == False:
					reset_game()
			elif event.key == pygame.K_DOWN:
				if stats.game_active:
					if snake_body.up_down(ai_settings) == False:
						snake_body.nxt_dir = ai_settings.dirs['down']
			elif event.key == pygame.K_UP:
				if stats.game_active:
					if snake_body.up_down(ai_settings) == False:
						snake_body.nxt_dir = ai_settings.dirs['up']
			elif event.key == pygame.K_LEFT:
				if stats.game_active:
					if snake_body.up_down(ai_settings) == True:
						snake_body.nxt_dir = ai_settings.dirs['left']
			elif event.key == pygame.K_RIGHT:
				if stats.game_active:
					if snake_body.up_down(ai_settings) == True:
						snake_body.nxt_dir = ai_settings.dirs['right']

def update_screen(ai_settings, stats, screen, snake_body, foody, mb):
	# re-paint screen in each loop
	screen.fill(ai_settings.bg_color)
	draw_wall(ai_settings, screen)
	snake_body.drawme(ai_settings, stats)
	snake_body.update(ai_settings)
	snake_body.hit_wall(stats, mb)
	snake_body.hit_self(stats, mb)
	snake_body.eat_food(ai_settings, stats, foody, mb)
	foody.drawme()
	mb.show_score()
	# show the most recent screen
	pygame.display.flip()

def draw_wall(ai_settings, screen):
	up_wall = pygame.Rect(5, 5, 260, 3)
	pygame.draw.rect(screen, ai_settings.wall_color, up_wall)
	bt_wall = pygame.Rect(5, 262, 260, 3)
	pygame.draw.rect(screen, ai_settings.wall_color, bt_wall)
	lf_wall = pygame.Rect(5, 5, 3, 260)
	pygame.draw.rect(screen, ai_settings.wall_color, lf_wall)
	rt_wall = pygame.Rect(262, 5, 3, 260)
	pygame.draw.rect(screen, ai_settings.wall_color, rt_wall)

def reset_game():
	return 0
