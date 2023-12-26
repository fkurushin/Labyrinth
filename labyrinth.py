import random
import pygame
from coord2d import Coord2D


class Labyrinth:
    def __init__(self, window):
        self.window = window

    @staticmethod
    def transition_choice(x, y, rm):
        """Функция выбора дальнейшего пути в генерации лабиринта

        Аргументы:
        x (int): текущая координата x
        y (int): текущая координата y
        rm (list): двумерный список, представляющий лабиринт

        Возвращает:
        tuple: новые координаты x и y, а также координаты tx и ty для создания перехода между текущей и новой точками
        Если нет доступных путей, возвращает (-1, -1, -1, -1)
        """
        choice_list = []
        if x > 0:
            if not rm[x - 1][y]:
                choice_list.append((x - 1, y))
        if x < len(rm) - 1:
            if not rm[x + 1][y]:
                choice_list.append((x + 1, y))
        if y > 0:
            if not rm[x][y - 1]:
                choice_list.append((x, y - 1))
        if y < len(rm[0]) - 1:
            if not rm[x][y + 1]:
                choice_list.append((x, y + 1))
        if choice_list:
            nx, ny = random.choice(choice_list)
            if x == nx:
                if ny > y:
                    tx, ty = x * 2, ny * 2 - 1
                else:
                    tx, ty = x * 2, ny * 2 + 1
            else:
                if nx > x:
                    tx, ty = nx * 2 - 1, y * 2
                else:
                    tx, ty = nx * 2 + 1, y * 2
            return nx, ny, tx, ty
        else:
            return -1, -1, -1, -1

    def create(self, n=5, m=5):
        """Генерация лабиринта"""
        reach_matrix = []
        for i in range(n):  # создаём матрицу достижимости ячеек
            reach_matrix.append([])
            for j in range(m):
                reach_matrix[i].append(False)
        transition_matrix = []
        for i in range(n * 2 - 1):  # заполнение матрицы переходов
            transition_matrix.append([])
            for j in range(m * 2 - 1):
                if i % 2 == 0 and j % 2 == 0:
                    transition_matrix[i].append(True)
                else:
                    transition_matrix[i].append(False)
        start = Coord2D().start_point_generate(n, m)
        finish = Coord2D().finish_point_generate(start, n, m)

        list_transition = [start]
        x, y = start.x, start.y
        reach_matrix[x][y] = True
        x, y, tx, ty = self.transition_choice(x, y, reach_matrix)
        for _ in range(1, m * n):
            while not (x >= 0 and y >= 0):
                x, y = list_transition[-1]
                list_transition.pop()
                x, y, tx, ty = self.transition_choice(x, y, reach_matrix)
            reach_matrix[x][y] = True
            list_transition.append((x, y))
            transition_matrix[tx][ty] = True
            x, y, tx, ty = self.transition_choice(x, y, reach_matrix)
        return (
            transition_matrix,
            start,
            finish,
        )  # возвращаем матрицу проходов и начальную точку

    def draw(
        self,
        matrix,
        start,
        finish,
        width_line=20,
        width_walls=5,
        color_way=(255, 255, 255),
        color_wall=(0, 0, 0),
        border=5,
        color_start=(0, 255, 0),
        color_finish=(255, 0, 0),
    ):
        """Рисование лабиринта"""
        width = (
            (len(matrix) // 2 + 1) * width_line
            + (len(matrix) // 2) * width_walls
            + border * 2
        )
        height = (
            (len(matrix[0]) // 2 + 1) * width_line
            + (len(matrix[0]) // 2) * width_walls
            + border * 2
        )
        for i in range(width):
            for j in range(height):
                if (
                    i < border or width - i <= border or j < border or height - j <= border
                ):  # отображение границ лабиринта
                    pygame.draw.line(self.window, color_wall, [i, j], [i, j], 1)
                else:
                    if (i - border) % (width_line + width_walls) <= width_line:
                        x = (i - border) // (width_line + width_walls) * 2
                    else:
                        x = (i - border) // (width_line + width_walls) * 2 + 1
                    if (j - border) % (width_line + width_walls) <= width_line:
                        y = (j - border) // (width_line + width_walls) * 2
                    else:
                        y = (j - border) // (width_line + width_walls) * 2 + 1
                    if matrix[x][y]:
                        pygame.draw.line(self.window, color_way, [i, j], [i, j], 1)
                    else:
                        pygame.draw.line(self.window, color_wall, [i, j], [i, j], 1)
        pygame.draw.rect(
            self.window,
            color_start,
            (
                border + start.x * (width_line + width_walls),
                border + start.y * (width_line + width_walls),
                width_line,
                width_line,
            ),
        )
        pygame.draw.rect(
            self.window,
            color_finish,
            (
                border + finish.x * (width_line + width_walls),
                border + finish.y * (width_line + width_walls),
                width_line,
                width_line,
            ),
        )