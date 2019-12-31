from app.libs.cell import Cell
from app.libs.snake import Snake
from app.libs.apple import Apple

import pygame
from pygame.locals import *


def run():
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    DIRECTION = RIGHT
    WIDTH = 800
    HEIGHT= 600
    FPS = 10
    GRID_SIZE = 25
    PAUSED = True
    CELLS_NUM = 4
    GAME_OVER = False
    GREEN = (40, 228, 21)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    HALF_BLACK = (0, 0, 0, 150)
    BLACK = (0, 0, 0)  


    messages = [
        "[ * ]  Pressione  [ r ]  ou [ p ] para iniciar a partida",
        "[ * ]  Pressione  [ r ]  para iniciar uma nova partida",
        "[ * ]  Pressione  [ ESC ]  para encerrar o Jogo"
    ]

    pygame.init()
    pygame.mixer.init()

    display = pygame.display.set_mode((WIDTH, HEIGHT), NOFRAME)
    pygame.display.set_caption('Snake')
    
    cover = pygame.Surface((WIDTH, HEIGHT), flags=SRCALPHA)
    cover.fill(HALF_BLACK)
    
    clock = pygame.time.Clock()

    score_font = pygame.font.Font("./assets/fonts/retro_computer.ttf", 16)
    messages_font = pygame.font.Font("./assets/fonts/retro_computer.ttf", 18)
    game_over_font = pygame.font.Font("./assets/fonts/retro_computer.ttf", 78)
    game_title_font = pygame.font.Font("./assets/fonts/retro_computer.ttf", 72)
    
    game_over_audio_file = 'assets/game_over.wav'
    game_over_audio = pygame.mixer.Sound(game_over_audio_file)
    
    snake = Snake(cells_num=CELLS_NUM, grid_size=GRID_SIZE)
    apple = Apple(grid_size=GRID_SIZE).new_position()
    apple.color = RED
    
    def game_over():
        display.blit(cover, (0, 0))
        display.blit(game_over_font.render("Game Over", True, RED), (130, 220))
        PAUSED = True

    def draw_messages(msgs):
        msg_pos = [80, 400]
        for msg in messages:
            display.blit(messages_font.render(msg, True, WHITE), msg_pos)
            msg_pos[1] += 35

    while True:
        display.fill((0, 0, 0))

        if snake.eat(apple):
            snake.score += 1
            apple.new_position()
            FPS += 1

        display.blit(score_font.render("Score: {}".format(str(snake.score)), True, GREEN), (690, 20))
        apple.show(display)
        snake.draw_cells(display)

        if not PAUSED:
            if not snake.override_edges() and not snake.self_collide():
                snake.move(DIRECTION)
            else:
                FPS = 2000
                pygame.mixer.Sound.play(game_over_audio)
                game_over()
                draw_messages(messages)
        else:
            display.blit(cover, (0, 0))
            display.blit(game_over_font.render("Snake", True, GREEN), (230, 200))
            draw_messages(messages)
            

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                if event.key == K_r:
                    pygame.mixer.Sound.stop(game_over_audio)
                    snake = Snake(cells_num=CELLS_NUM, grid_size=GRID_SIZE)
                    PAUSED = False
                    DIRECTION = RIGHT
                    FPS = 10
                if event.key == K_p:
                    PAUSED = True if not PAUSED else False                
                if event.key == K_UP:
                    if snake.direction is not DOWN:
                        DIRECTION = UP
                if event.key == K_RIGHT:
                    if snake.direction is not LEFT:
                        DIRECTION = RIGHT
                if event.key == K_DOWN:
                    if snake.direction is not UP:
                        DIRECTION = DOWN
                if event.key == K_LEFT:
                    if snake.direction is not RIGHT:
                        DIRECTION = LEFT

        pygame.display.flip()
        clock.tick(FPS)
