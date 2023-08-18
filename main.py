import pygame
from Ping_pong import *

pygame.init()

setting_win =  (700, 500)
setting_board = (30, 250)

window = pygame.display.set_mode(setting_win)
pygame.display.set_caption("PONG")

player_left = Board(10, setting_win[1] // 2 - setting_board[1] // 2, setting_board[0], setting_board[1], (255,255,255), 5)
player_right = Board(setting_win[0] - setting_board[0]- 10, setting_win[1] // 2 - setting_board[1] // 2, setting_board[0], setting_board[1], (255,255,255), 5)

clock = pygame.time.Clock()

game = True
while game:
    window.fill((0, 0, 0))

    player_left.move(window)
    player_right.move(window)

    pygame.draw.line(window, (255, 255, 255), (setting_win[0] // 2, 0), (setting_win[0] // 2, setting_win[1]), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    clock.tick(60)
    pygame.display.flip()