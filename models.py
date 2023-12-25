import pygame
from definitions import *


class Coord2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Player:
    def __init__(self, name, level, x, y):
        # global record_time, start_time, player, matrix, start, finish, matrix_base
        self.name = name
        self.level = level
        self.x = x
        self.y = y

    def move_to_point(self, x, y):
        self.x = x
        self.y = y

    def draw_player(self, window):
        """Отрисовка игрока на экране"""
        pygame.draw.circle(
            window,
            color_player,
            (
                border + self.x * (width_line + width_walls) + width_line // 2,
                border + self.y * (width_line + width_walls) + width_line // 2,
            ),
            width_line // 2 - 3,
        )

    def click_right(self, m):
        """Движение вправо"""
        if len(m) > self.x * 2 + 2:
            if m[self.x * 2 + 1][self.y * 2]:
                self.x += 1

    def click_left(self, m):
        """Движение влево"""
        if -1 < self.x * 2 - 2:
            if m[self.x * 2 - 1][self.y * 2]:
                self.x -= 1

    def click_down(self, m):
        """Движение вниз"""
        if len(m[0]) > self.y * 2 + 2:
            if m[self.x * 2][self.y * 2 + 1]:
                self.y += 1

    def click_up(self, m):
        """Движение вверх"""
        if -1 < self.y * 2 - 2:
            if m[self.x * 2][self.y * 2 - 1]:
                self.y -= 1

    def get_position(self):
        return self.x, self.y

    def delete_player(self, start, window):
        """Функция удаления игрока при движении и оставления следов"""
        if (self.x, self.y) == start:
            pygame.draw.circle(
                window,
                color_start,
                (
                    border + self.x * (width_line + width_walls) + width_line // 2,
                    border + self.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 2 - 3,
            )
        else:
            pygame.draw.circle(
                window,
                color_way,
                (
                    border + self.x * (width_line + width_walls) + width_line // 2,
                    border + self.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 2 - 3,
            )
        if trace:
            pygame.draw.circle(
                window,
                color_trace,
                (
                    border + self.x * (width_line + width_walls) + width_line // 2,
                    border + self.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 3 - 3,
            )