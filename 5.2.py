def plot_point(grid, x, y):
    if grid[y][x] == '.':
        grid[y][x] = 1
    else:
        grid[y][x] = grid[y][x] + 1


def draw_vertical_line(grid, x, y_min, y_max):
    x = x - 1
    y_min = y_min - 1
    for y in range(y_min, y_max):
        plot_point(grid, x, y)

def draw_horizontal_line(grid, y, x_min, x_max):
    y = y - 1
    x_min = x_min - 1
    for x in range(x_min, x_max):
        plot_point(grid, x, y)


def draw_diagonal_line(grid, y_min, y_max, x, x_increasing):
    y_min = y_min - 1
    x = x - 1
    for y in range(y_min, y_max):
        plot_point(grid, x, y)
        if x_increasing:
            x = x + 1
        else:
            x = x - 1

with open('5.txt') as f:
    data = f.read().splitlines()

lines = []
for line in data:
    line_to_cords = line.split(' -> ')
    cords = [list(map(int, line_to_cords[0].split(','))), list(map(int, line_to_cords[1].split(',')))]
    lines.append(cords)

max_axis = 0
for cords in lines:
    max_0 = max(cords[0])
    max_1 = max(cords[1])

    if max_axis < max(max_0, max_1):
        max_axis = max(max_0, max_1)

grid = []
for y in range(max_axis):
    grid.append([])
    for x in range(max_axis):
        grid[y].append('.')


for line in lines:
    if line[0][0] == line[1][0]:
        # vertical line
        x = line[0][0]
        y_min = min(line[0][1], line[1][1])
        y_max = max(line[0][1], line[1][1])

        draw_vertical_line(grid, x, y_min, y_max)

    elif line[0][1] == line[1][1]:
        # horizontal line
        y = line[0][1]
        x_min = min(line[0][0], line[1][0])
        x_max = max(line[0][0], line[1][0])

        draw_horizontal_line(grid, y, x_min, x_max)

    else: 
        # diagonal line
        y_min = min(line[0][1], line[1][1])
        y_max = max(line[0][1], line[1][1])
        x = line[0][0] if y_min == line[0][1] else line[1][0]
        x_increasing = x == min(line[0][0], line[1][0])

        draw_diagonal_line(grid, y_min, y_max, x, x_increasing)

two_plus_count = 0
for y in grid:
    for x in y:
        if x != '.' and x >= 2:
            two_plus_count = two_plus_count + 1

print(f'Count of 2 plus points: {two_plus_count}')
