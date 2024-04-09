import sys

import pygame

from config import *
from game_stat import GameStat

# init variables
used = ''
coming = 'this is test string'
xpos, ypos = 0, 0
err_cnt = 0
run = True
game_stop = False
stat = GameStat()

# init fonts
pygame.font.init()
path = pygame.font.match_font("arial")
Font = pygame.font.Font(path, 25)

# init window
pygame.init()
screen = pygame.display.set_mode((HEIGHT, WIDTH))
screen.fill((0, 0, 0))
pygame.display.set_caption('keyboard_game')


def start_game():
    screen.fill((0, 0, 0))
    global xpos
    xpos = 0
    sec_ = Font.render(coming, 1, (100, 100, 100))
    screen.blit(sec_, (0, 0))


start_time = time.time()
start_game()

while run:

    if game_stop:
        end_time = time.time()

        screen = pygame.display.set_mode((HEIGHT, WIDTH))
        screen.fill((0, 0, 0))
        st = f"Errors count: {err_cnt} Time: {round(end_time - start_time, 2)}"
        stat_rendered = Font.render(st, 1, WHITE)
        screen.blit(stat_rendered, (0, 0))

        str = "Press SPACE to play again"
        str_rend = Font.render(str, 1, WHITE)
        screen.blit(str_rend, (0, 20))

        while game_stop:
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    game_stop = False
                    run = False

                if i.type == pygame.KEYDOWN:
                    if pygame.key.get_pressed()[pygame.K_SPACE]:
                        game_stop = False
            pygame.display.flip()

        used = ''
        coming = 'hello'
        start_game()
        start_time = time.time()
    else:
        if coming == '':
            game_stop = True

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        if i.type == pygame.KEYDOWN:
            if not game_stop:
                cur = coming[0]
                if pygame.key.get_pressed()[bind[cur]]:
                    used += cur
                    coming = coming[1:]
                    xpos += Font.metrics(cur)[0][4]
                    a = Font.render(used, 1, WHITE)
                    b = Font.render(coming, 1, (100, 100, 100))

                    screen.fill(BLACK)
                    screen.blit(a, (0, 0))
                    screen.blit(b, (xpos, 0))
                else:
                    err_cnt += 1

    pygame.display.flip()
