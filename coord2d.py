import random


class Coord2D:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

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

    @staticmethod
    def start_point_generate(n, m):
        """Функция выбора точки начала лабиринта

        Аргументы:
        n (int): количество строк в лабиринте
        m (int): количество столбцов в лабиринте

        Возвращает:
        tuple: координаты точки начала лабиринта в виде кортежа (x, y)
        """
        if random.choice([True, False]):
            if random.choice([True, False]):
                x, y = 0, random.randint(0, m - 1)
            else:
                x, y = n - 1, random.randint(0, m - 1)
        else:
            if random.choice([True, False]):
                x, y = (random.randint(0, n - 1), 0)
            else:
                x, y = (random.randint(0, n - 1), m - 1)
        return Coord2D(x, y)

    @staticmethod
    def finish_point_generate(start, n, m):
        """Выбор точки конца лабиринта

        Аргументы:
        start (tuple): координаты точки начала лабиринта в виде кортежа (x, y)
        n (int): количество строк в лабиринте
        m (int): количество столбцов в лабиринте

        Возвращает:
        tuple: координаты точки конца лабиринта в виде кортежа (x, y)
        """
        return Coord2D(n - 1 - start.x, m - 1 - start.y)
