import pygame
import sys
from snake_object import Snake
from setting import Setting
from apple import Apple

def press_keydown(snake, event):
    if event.key == pygame.K_LEFT:
        snake.go_x = -1
        snake.go_y = 0
    elif event.key == pygame.K_RIGHT:
        snake.go_x = 1
        snake.go_y = 0
    elif event.key == pygame.K_UP:
        snake.go_x = 0
        snake.go_y = -1
    elif event.key == pygame.K_DOWN:
        snake.go_x = 0
        snake.go_y = 1
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        snake.del_tail=False


def show_apple(sn_setting):
    for apple in sn_setting.mass_apple:
        apple.blitme()

def add_apple(sn_setting,screen):
    sn_setting.new_apple += 1
    if sn_setting.new_apple == sn_setting.speed_apple:
        sn_setting.new_apple = 0
        new_apple = Apple(sn_setting, screen)
        sn_setting.mass_apple.append(new_apple)


def play_game():
    pygame.init()

    sn_setting = Setting()
    screen = pygame.display.set_mode((sn_setting.screen_width, sn_setting.screen_heigth))
    pygame.display.set_caption("Snake ))")

    snake = Snake(sn_setting)

    new_apple = Apple(sn_setting, screen)
    sn_setting.mass_apple.append(new_apple)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                press_keydown(snake, event)

        screen.fill(sn_setting.bg_color)

        snake.update_snake()

        add_apple(sn_setting,screen)

        snake.test_tail()
        snake.eat_apple()

        snake.flip_tail(screen)
        snake.flip_head(screen)
        show_apple(sn_setting)

        pygame.display.flip()

play_game()
