import time

from config import *
from player import *

cur_game = Player()

run = True
run_game = True
cur_game.start_game("blah blah")

while run:
    start_time = time.time()

    # main game
    while run_game:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit(0)
            if i.type == pygame.KEYDOWN:
                cur_game.handle_text_input()
                if cur_game.coming == '':
                    run_game = False
        pygame.display.flip()

    # pause
    stop_time = time.time()
    cur_game.st.upd(len(cur_game.used), stop_time - start_time)

    cur_game.screen.fill(BLACK)
    Text.print_text(f"Errors: {cur_game.st.get_last_errors()}", cur_game.screen, cur_game.font, 0, 0, WHITE)
    Text.print_text(f"Speed: {cur_game.st.get_last_speed()} symb/sec", cur_game.screen, cur_game.font, 0, 20, WHITE)
    Text.print_text(f"Avg errors: {cur_game.st.get_avg_errors()}", cur_game.screen, cur_game.font, 0, 40, WHITE)
    Text.print_text(f"Avg speed: {cur_game.st.get_avg_speed()} symb/sec", cur_game.screen, cur_game.font, 0, 60, WHITE)
    Text.print_text("Press SPACE to continue", cur_game.screen, cur_game.font, 0, 80, WHITE)

    while not run_game:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                exit(0)

            if i.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    run_game = True
        pygame.display.flip()

    cur_game.restart(texts[0])
