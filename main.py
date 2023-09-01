import pygame
from Ping_pong import *
from PyQt5.QtWidgets import QInputDialog, QApplication

pygame.init()

app = QApplication([])


window = pygame.display.set_mode(setting_win)
pygame.display.set_caption("PONG")

player_left = Board(10, setting_win[1] // 2 - setting_board[1] // 2, setting_board[0], setting_board[1], (255,255,255), 5)
player_right = Board(setting_win[0] - setting_board[0]- 10, setting_win[1] // 2 - setting_board[1] // 2, setting_board[0], setting_board[1], (255,255,255), 5)
player_left.NAME = QInputDialog().getText(QInputDialog(), "PING-PONG", "Введіть ім'я лівого гравця. До 7 символов!")[0][:7].lower()
player_right.NAME = QInputDialog().getText(QInputDialog(), "PING-PONG", "Введіть ім'я правого гравця. До 7 символов!")[0][:7].lower()
ball = Ball(setting_win[0] // 2 - 20, setting_win[1] // 2, 20, (220,155,115), 5)

clock = pygame.time.Clock()

game = True
while game:
    window.fill((0, 0, 0))
    blit_player_score(window, player_left, player_right, setting_win)
    player_left.move(window)
    player_right.move(window)
    ball.move(window, player_left, player_right)
    check_goal(ball, player_left, player_right)

    pygame.draw.line(window, (255, 255, 255), (setting_win[0] // 2, 0), (setting_win[0] // 2, setting_win[1]), 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_left.MOVE["UP"] = True
            elif event.key == pygame.K_s:
                player_left.MOVE["DOWN"] = True
            if event.key == pygame.K_UP:
                player_right.MOVE["UP"] = True
            elif event.key == pygame.K_DOWN:
                player_right.MOVE["DOWN"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_left.MOVE["UP"] = False
            elif event.key == pygame.K_s:
                player_left.MOVE["DOWN"] = False
            if event.key == pygame.K_UP:
                player_right.MOVE["UP"] = False
            elif event.key == pygame.K_DOWN:
                player_right.MOVE["DOWN"] = False
            

    clock.tick(60)
    pygame.display.flip()