from game_stat import GameStat
from text_interface import Text
from config import *


class Player:
    st: GameStat
    xpos: int
    ypos: int
    used: str
    coming: str

    def __init__(self):
        self.st = GameStat()
        pygame.init()
        self.screen = pygame.display.set_mode((HEIGHT, WIDTH))
        pygame.font.init()
        self.font = pygame.font.Font(pygame.font.match_font("arial"), 25)
        self.xpos = 0
        self.ypos = 0
        self.used = ''
        self.coming = ''

    def start_game(self, txt: str):
        self.screen.fill(BLACK)
        pygame.display.set_caption('keyboard_game')
        self.coming = txt
        Text.print_text(txt, self.screen, self.font, 0, 0, GREY)

    def restart(self, txt: str):
        self.st.restart()
        self.xpos = 0
        self.ypos = 0
        self.screen.fill(BLACK)
        self.used = ''
        self.coming = txt
        Text.print_text(txt, self.screen, self.font, 0, 0, GREY)

    def handle_text_input(self):
        cur = self.coming[0]
        need_mode = 0
        if cur.isupper() or cur == '(' or cur == ') ':
            need_mode = 1
        if pygame.key.get_pressed()[bind[cur]] and pygame.key.get_mods() == need_mode:
            self.used += cur
            self.coming = self.coming[1:]

            self.screen.fill(BLACK)

            Text.print_text(self.used, self.screen, self.font, 0, 0, WHITE)
            self.xpos += self.font.metrics(cur)[0][4]
            # print(self.font.metrics(cur)[0])
            Text.print_text(self.coming, self.screen, self.font, self.xpos, self.ypos, GREY)

        else:
            self.st.add_error()

    def get_errors(self) -> int:
        return self.st.get_avg_errors()

    def get_speed(self) -> float:
        return self.st.get_avg_speed()
