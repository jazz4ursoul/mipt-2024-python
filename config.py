import pygame
import time

WIDTH = 600
HEIGHT = 800
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (100, 100, 100)

symb_height = 18

bind = {'q': pygame.K_q, 'w': pygame.K_w, 'e': pygame.K_e, 'r': pygame.K_r, 't': pygame.K_t, 'y': pygame.K_y,
        'u': pygame.K_u, 'i': pygame.K_i, 'o': pygame.K_o, 'p': pygame.K_p, "a": pygame.K_a, 's': pygame.K_s,
        'd': pygame.K_d, 'f': pygame.K_f, 'g': pygame.K_g, 'h': pygame.K_h, 'j': pygame.K_j, 'k': pygame.K_k,
        'l': pygame.K_l, 'z': pygame.K_z, 'x': pygame.K_x, 'c': pygame.K_c, 'v': pygame.K_v, 'b': pygame.K_b,
        'n': pygame.K_n, 'm': pygame.K_m, ' ': pygame.K_SPACE, ',': pygame.K_COMMA, '.': pygame.K_PERIOD,
        '(': pygame.K_LEFTPAREN, ')': pygame.K_RIGHTPAREN,
        'Q': pygame.K_q, 'W': pygame.K_w, 'E': pygame.K_e, 'R': pygame.K_r, 'T': pygame.K_t, 'Y': pygame.K_y,
        'U': pygame.K_u, 'I': pygame.K_i, 'O': pygame.K_o, 'P': pygame.K_p, "A": pygame.K_a, 'S': pygame.K_s,
        'D': pygame.K_d, 'F': pygame.K_f, 'G': pygame.K_g, 'H': pygame.K_h, 'J': pygame.K_j, 'K': pygame.K_k,
        'L': pygame.K_l, 'Z': pygame.K_z, 'X': pygame.K_x, 'C': pygame.K_c, 'V': pygame.K_v, 'B': pygame.K_b,
        'N': pygame.K_n, 'M': pygame.K_m
        }

texts = ["Random is a term used in mathematics"]
