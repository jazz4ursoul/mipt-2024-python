from config import *


class Text:
    @staticmethod
    def print_text(txt, screen, font, xpos, ypos, color):
        a = font.render(txt, 1, color)
        screen.blit(a, (xpos, ypos))
