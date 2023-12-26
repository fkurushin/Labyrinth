import pygame
import time
from definitions import *
from player import Player
from labyrinth import Labyrinth


class CustomGame:
    def __init__(self, player, labyrinth):
        self.player = player
        self.start_time = time.time()

        self.labyrinth = labyrinth
        self.matrix, self.start, self.finish = self.labyrinth.create(width, height)
        self.matrix_base = []
        self.__trace = trace
        self.record_time = 9999

    def new_game(self, window):
        pygame.draw.rect(window, (0, 0, 0), (0, height_window - 70, width_window, 70))
        i = 0
        while self.matrix in self.matrix_base \
                or self.start.x == self.finish.x \
                or self.start.y == self.finish.y:
            self.matrix, self.start, self.finish = self.labyrinth.create(width, height)
            i += 1
            if i > 20:
                print("Не найдено лабиринтов без повторения")
                break
        self.matrix_base.append(matrix)

        self.labyrinth.draw(
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
        self.player.draw_player(window)

    def setting_trace(self):
        """Изменение флага оставления следов"""
        if self.__trace:
            self.__trace = False
        else:
            self.__trace = True

    def play(self, window):
        flag_game = True
        curr_time = 0
        while flag_game:
            player.delete(self.start, window)
            if player.coord == self.finish:
                window.fill((0, 0, 0))
                player.level += 1
                if curr_time < self.record_time:
                    self.record_time = curr_time
                self.start_time = time.time()
                pygame.draw.rect(
                    window, (0, 0, 0), (0, height_window - 70, width_window, 70)
                )
                self.matrix, self.start, self.finish = self.labyrinth.create(width, height)
                i = 0
                while (
                    self.matrix in self.matrix_base
                    or self.start.x == self.finish.x
                    or self.start.y == self.finish.y
                ):
                    self.matrix, self.start, self.finish = self.labyrinth.create(width, height)
                    i += 1
                    if i > 20:
                        print("Не найдено лабиринтов без повторения")
                        break
                self.matrix_base.append(matrix)
                player.move_to_point(start)

                self.labyrinth.draw(
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
                        player.click_right(self.matrix)
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        player.click_left(matrix)
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        player.click_up(matrix)
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        player.click_down(matrix)
                    if event.key == pygame.K_p:
                        pass
                    if event.key == pygame.K_q:
                        self.setting_trace()
                    if event.key == pygame.K_r:
                        self.new_game(player)
                    if event.key == pygame.K_e:
                        player.move_to_point(start)

            if info and width >= 10:
                text1 = font.render(
                    "Пройдено лабиринтов: " + str(player.level), True, (255, 255, 255)
                )
                window.blit(text1, [5, height_window - 65])
                pygame.draw.rect(
                    window, (0, 0, 0), (5, height_window - 40, width_window, 20)
                )
                text2 = font.render("Время: " + str(int(curr_time)), True, (255, 255, 255))
                window.blit(text2, [5, height_window - 40])
                if self.record_time == 9999:
                    text3 = font.render("Рекордное время: " + str(0), True, (255, 255, 255))
                    window.blit(text3, [5, height_window - 20])
                else:
                    text3 = font.render(
                        "Рекордное время: " + str(int(self.record_time)), True, (255, 255, 255)
                    )
                    window.blit(text3, [5, height_window - 20])
            player.draw(window)
            curr_time = time.time() - self.start_time
            pygame.display.update()


if __name__ == "__main__":
    """Системные переменные"""
    if width < 10:
        info = False
    if info:
        height_window += 70
    pygame.init()
    window = pygame.display.set_mode((width_window, height_window))
    pygame.display.set_caption("Лабиринт")
    font = pygame.font.Font(None, 25)

    window.fill((0, 0, 0))
    labyrinth = Labyrinth(window)

    matrix, start, finish = labyrinth.create(width, height)
    player = Player("Fedor", 0, start)

    game = CustomGame(player, labyrinth)

    k = 0
    while matrix in game.matrix_base or start.x == finish.x or start.y == finish.y:
        k += 1
        if k > 20:
            print("Не найдено лабиринтов без повторения")
            break
        matrix, start, finish = labyrinth.create(width, height)

    player.move_to(start)

    game.matrix_base.append(matrix)
    start_time = time.time()
    labyrinth.draw(
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
    player.draw(window)

    # основной игровой цикл
    game.play(window)

