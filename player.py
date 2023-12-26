import pygame
from definitions import *
from coord2d import Coord2D


class Player:
    def __init__(self, name, level, init_coord):
        self.name = name
        self.level = level
        self.coord = init_coord

    def move_to(self, new_coord):
        self.coord = new_coord

    def draw(self, window):
        """Отрисовка игрока на экране"""
        pygame.draw.circle(
            window,
            color_player,
            (
                border + self.coord.x * (width_line + width_walls) + width_line // 2,
                border + self.coord.y * (width_line + width_walls) + width_line // 2,
            ),
            width_line // 2 - 3,
        )

    def click_right(self, m):
        self.coord.click_right(m)

    def click_left(self, m):
        self.coord.click_left(m)

    def click_down(self, m):
        self.coord.click_down(m)

    def click_up(self, m):
        self.coord.click_up(m)

    def get_position(self):
        return self.coord

    def delete(self, start, window):
        """Функция удаления игрока при движении и оставления следов"""
        if self.coord == start:
            pygame.draw.circle(
                window,
                color_start,
                (
                    border + self.coord.x * (width_line + width_walls) + width_line // 2,
                    border + self.coord.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 2 - 3,
            )
        else:
            pygame.draw.circle(
                window,
                color_way,
                (
                    border + self.coord.x * (width_line + width_walls) + width_line // 2,
                    border + self.coord.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 2 - 3,
            )
        if trace:
            pygame.draw.circle(
                window,
                color_trace,
                (
                    border + self.coord.x * (width_line + width_walls) + width_line // 2,
                    border + self.coord.y * (width_line + width_walls) + width_line // 2,
                ),
                width_line // 3 - 3,
            )
