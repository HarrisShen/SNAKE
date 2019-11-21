import sys

import pygame


def check_events(ai_settings, stats, screen, snake_body, food, mb):
    # monitor keyboard and mouse event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                # quit game, close window
                if stats.game_status == 'start':
                    sys.exit()
            elif event.key == pygame.K_SPACE:
                # pause the game
                if stats.game_status == 'game':
                    stats.game_active = not stats.game_active
                # restart the game
                elif stats.game_status == 'end':
                    reset_game(ai_settings, stats, screen,
                               snake_body, food, mb)
            elif event.key == pygame.K_RETURN:
                # start a game
                if stats.game_status == 'start':
                    stats.game_active = True
                    stats.game_status = 'game'
                    reset_game(ai_settings, stats, screen,
                               snake_body, food, mb)
                # confirm to quit a game
                elif stats.game_status == 'confirm':
                    stats.game_status = 'start'
            elif event.key == pygame.K_ESCAPE:
                # quit game after it ends
                if stats.game_status == 'end':
                    stats.game_active = False
                    stats.game_status = 'start'
                # get ready to quit a game
                elif stats.game_status == 'game':
                    stats.game_active = False
                    stats.game_status = 'confirm'
                # false alarm, resume game
                elif stats.game_status == 'confirm':
                    stats.game_active = True
                    stats.game_status = 'game'
            # control the direction of the snake
            elif event.key == pygame.K_DOWN:
                if stats.game_active:
                    if not snake_body.up_down():
                        snake_body.crt_dir = ai_settings.dirs['down']
                        snake_body.update(ai_settings, stats, food)
            elif event.key == pygame.K_UP:
                if stats.game_active:
                    if not snake_body.up_down():
                        snake_body.crt_dir = ai_settings.dirs['up']
                        snake_body.update(ai_settings, stats, food)
            elif event.key == pygame.K_LEFT:
                if stats.game_active:
                    if snake_body.up_down():
                        snake_body.crt_dir = ai_settings.dirs['left']
                        snake_body.update(ai_settings, stats, food)
            elif event.key == pygame.K_RIGHT:
                if stats.game_active:
                    if snake_body.up_down():
                        snake_body.crt_dir = ai_settings.dirs['right']
                        snake_body.update(ai_settings, stats, food)


def update_screen(ai_settings, stats, screen, snake_body, food, mb):
    if stats.game_status == 'start':
        draw_start_screen(ai_settings, stats, screen, mb)
    else:
        update_game_screen(ai_settings, stats, screen,
                           snake_body, food, mb)


def update_game_screen(ai_settings, stats, screen, snake_body, food, mb):
    # re-paint screen in each loop when game is on
    screen.fill(ai_settings.bg_color)
    draw_wall(ai_settings, screen)
    snake_body.draw(ai_settings)
    food.draw()
    mb.show_status()

    # show the most recent screen
    pygame.display.flip()


def draw_start_screen(ai_settings, stats, screen, mb):
    screen.fill(ai_settings.bg_color)
    draw_wall(ai_settings, screen)
    mb.show_status()
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


def reset_game(ai_settings, stats, screen, snake_body, foody, mb):
    # re-initialize settins and stats
    ai_settings.initialize_dynamic_settings()
    stats.initialize_dynamic_stats()

    # re-create snake and food
    snake_body.create_new()
    foody.create_new(stats, snake_body)

    # reset flags
    stats.game_active = True
    stats.game_status = 'game'
