import random
import pygame
import time
from definitions import *
from models import Player


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
            start = (0, random.randint(0, m - 1))
        else:
            start = (n - 1, random.randint(0, m - 1))
    else:
        if random.choice([True, False]):
            start = (random.randint(0, n - 1), 0)
        else:
            start = (random.randint(0, n - 1), m - 1)
    return start


def finish_point_generate(start, n, m):
    """Выбор точки конца лабиринта

    Аргументы:
    start (tuple): координаты точки начала лабиринта в виде кортежа (x, y)
    n (int): количество строк в лабиринте
    m (int): количество столбцов в лабиринте

    Возвращает:
    tuple: координаты точки конца лабиринта в виде кортежа (x, y)
    """
    return n - 1 - start[0], m - 1 - start[1]


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


def create_labyrinth(n=5, m=5):
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
    start = start_point_generate(n, m)
    finish = finish_point_generate(start, n, m)
    list_transition = [start]
    x, y = start
    reach_matrix[x][y] = True
    x, y, tx, ty = transition_choice(x, y, reach_matrix)
    for _ in range(1, m * n):
        while not (x >= 0 and y >= 0):
            x, y = list_transition[-1]
            list_transition.pop()
            x, y, tx, ty = transition_choice(x, y, reach_matrix)
        reach_matrix[x][y] = True
        list_transition.append((x, y))
        transition_matrix[tx][ty] = True
        x, y, tx, ty = transition_choice(x, y, reach_matrix)
    return (
        transition_matrix,
        start,
        finish,
    )  # возвращаем матрицу проходов и начальную точку


def draw_labyrinth(
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
                pygame.draw.line(window, color_wall, [i, j], [i, j], 1)
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
                    pygame.draw.line(window, color_way, [i, j], [i, j], 1)
                else:
                    pygame.draw.line(window, color_wall, [i, j], [i, j], 1)
    pygame.draw.rect(
        window,
        color_start,
        (
            border + start[0] * (width_line + width_walls),
            border + start[1] * (width_line + width_walls),
            width_line,
            width_line,
        ),
    )
    pygame.draw.rect(
        window,
        color_finish,
        (
            border + finish[0] * (width_line + width_walls),
            border + finish[1] * (width_line + width_walls),
            width_line,
            width_line,
        ),
    )


# def delete_player():
#     """Функция удаления игрока при движении и оставления следов"""
#     if (player[0], player[1]) == start:
#         pygame.draw.circle(
#             window,
#             color_start,
#             (
#                 border + player[0] * (width_line + width_walls) + width_line // 2,
#                 border + player[1] * (width_line + width_walls) + width_line // 2,
#             ),
#             width_line // 2 - 3,
#         )
#     else:
#         pygame.draw.circle(
#             window,
#             color_way,
#             (
#                 border + player[0] * (width_line + width_walls) + width_line // 2,
#                 border + player[1] * (width_line + width_walls) + width_line // 2,
#             ),
#             width_line // 2 - 3,
#         )
#     if trace:
#         pygame.draw.circle(
#             window,
#             color_trace,
#             (
#                 border + player[0] * (width_line + width_walls) + width_line // 2,
#                 border + player[1] * (width_line + width_walls) + width_line // 2,
#             ),
#             width_line // 3 - 3,
#         )


# def draw_player():
#     """Отрисовка игрока на экране"""
#     pygame.draw.circle(
#         window,
#         color_player,
#         (
#             border + player[0] * (width_line + width_walls) + width_line // 2,
#             border + player[1] * (width_line + width_walls) + width_line // 2,
#         ),
#         width_line // 2 - 3,
#     )
#

def tick():
    """Cекудномер"""
    global start_time, t
    t = time.time() - start_time



def setting_trace():
    """Изменение флага оставления следов"""
    global trace
    if trace:
        trace = False
    else:
        trace = True


def new_game(player):
    global record_time, start_time, matrix, start, finish, matrix_base
    window.fill((0, 0, 0))
    start_time = time.time()
    pygame.draw.rect(window, (0, 0, 0), (0, height_window - 70, width_window, 70))
    matrix, start, finish = create_labyrinth(width, height)
    k = 0
    while matrix in matrix_base or start[0] == finish[0] or start[1] == finish[1]:
        matrix, start, finish = create_labyrinth(width, height)
        k += 1
        if k > 20:
            print("Не найдено лабиринтов без повторения")
            break
    matrix_base.append(matrix)

    draw_labyrinth(
        matrix,
        start,
        finish,
        width_line,
        width_walls,
        color_way,
        color_wall,
        border,
        color_start,
        color_finish,
    )
    player.draw_player(window)


if __name__ == "__main__":
    """Системные переменные"""
    if width < 10:
        info = False
    if info:
        height_window += 70
    matrix_base = []

    pygame.init()
    window = pygame.display.set_mode((width_window, height_window))
    pygame.display.set_caption("Лабиринт")
    font = pygame.font.Font(None, 25)
    flag_game = True
    # start is a tuple with x and y
    matrix, start, finish = create_labyrinth(width, height)
    k = 0
    while matrix in matrix_base or start[0] == finish[0] or start[1] == finish[1]:
        k += 1
        if k > 20:
            print("Не найдено лабиринтов без повторения")
            break
        matrix, start, finish = create_labyrinth(width, height)

    player = Player("Fedor", 0, *start)

    matrix_base.append(matrix)
    start_time = time.time()
    draw_labyrinth(
        matrix,
        start,
        finish,
        width_line,
        width_walls,
        color_way,
        color_wall,
        border,
        color_start,
        color_finish,
    )
    player.draw_player(window)

    while flag_game:  # основной игровой цикл
        player.delete_player(start, window)
        if (player.x, player.y) == finish:
            window.fill((0, 0, 0))
            player.level += 1
            if t < record_time:
                record_time = t
            start_time = time.time()
            pygame.draw.rect(
                window, (0, 0, 0), (0, height_window - 70, width_window, 70)
            )
            matrix, start, finish = create_labyrinth(width, height)
            k = 0
            while (
                matrix in matrix_base or start[0] == finish[0] or start[1] == finish[1]
            ):
                matrix, start, finish = create_labyrinth(width, height)
                k += 1
                if k > 20:
                    print("Не найдено лабиринтов без повторения")
                    break
            matrix_base.append(matrix)
            player.move_to_point(*start)

            draw_labyrinth(
                matrix,
                start,
                finish,
                width_line,
                width_walls,
                color_way,
                color_wall,
                border,
                color_start,
                color_finish,
            )
            player.draw_player(window)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag_game = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.click_right(matrix)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.click_left(matrix)
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.click_up(matrix)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.click_down(matrix)
                if event.key == pygame.K_p:
                    pass
                if event.key == pygame.K_q:
                    setting_trace()
                if event.key == pygame.K_r:
                    new_game(player)
                if event.key == pygame.K_e:
                    player.move_to_point(*start)

        if info and width >= 10:
            text1 = font.render(
                "Пройдено лабиринтов: " + str(player.level), True, (255, 255, 255)
            )
            window.blit(text1, [5, height_window - 65])
            pygame.draw.rect(
                window, (0, 0, 0), (5, height_window - 40, width_window, 20)
            )
            text2 = font.render("Время: " + str(int(t)), True, (255, 255, 255))
            window.blit(text2, [5, height_window - 40])
            if record_time == 9999:
                text3 = font.render("Рекордное время: " + str(0), True, (255, 255, 255))
                window.blit(text3, [5, height_window - 20])
            else:
                text3 = font.render(
                    "Рекордное время: " + str(int(record_time)), True, (255, 255, 255)
                )
                window.blit(text3, [5, height_window - 20])
        player.draw_player(window)
        tick()
        pygame.display.update()
