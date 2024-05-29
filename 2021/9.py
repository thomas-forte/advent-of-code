with open("9.txt") as f:
    data = f.read().splitlines()

depths = []
for line in data:
    depths.append(list(map(int, list(line))))

points = []
for y in range(len(depths)):
    for x in range(len(depths[y])):
        if y - 1 < 0 or depths[y - 1][x] > depths[y][x]:
            if y + 1 >= len(depths) or depths[y + 1][x] > depths[y][x]:
                if x - 1 < 0 or depths[y][x - 1] > depths[y][x]:
                    if x + 1 >= len(depths) or depths[y][x + 1] > depths[y][x]:
                        points.append([x, y])

point_values = list(map(lambda p: depths[p[1]][p[0]] + 1, points))

print(f"The sum of all the risk values is: {sum(point_values)}")
