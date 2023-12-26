border = 5
width_line = 40
width_walls = 5
color_way = (255, 255, 255)
color_wall = (0, 0, 0)
color_player = (0, 0, 255)
color_start = (0, 255, 0)
color_finish = (255, 0, 0)
trace = True
color_trace = color_player
width = 10
height = 10
width_window = (
    ((width * 2 - 1) // 2 + 1) * width_line
    + ((width * 2 - 1) // 2) * width_walls
    + border * 2
)
height_window = (
    ((height * 2 - 1) // 2 + 1) * width_line
    + ((height * 2 - 1) // 2) * width_walls
    + border * 2
)
info = True
