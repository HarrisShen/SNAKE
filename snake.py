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
    food = Food(ai_settings, screen)

    # create game stats
    stats = GameStats()

    # create a message board
    mb = MessageBoard(ai_settings, stats, screen)

    # main loop
    while True:

        # monitor keyboard and mouse event
        gf.check_events(ai_settings, stats, screen,
                        snake, food, mb)

        gf.update_screen(ai_settings, stats, screen, snake, food, mb)
        # pause a little while for first frame
        if snake.first_frame:
            pygame.time.delay(300)
            snake.first_frame = False
        # update snake when game is on
        if stats.game_active:
            snake.update(ai_settings, stats, food)


if __name__ == "__main__":
    run_game()
