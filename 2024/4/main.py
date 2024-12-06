"""
Advent of Code
year: 2024
part: 4
"""


def part_1(input_lines):
    """
    Word search for XMAS
    """

    xmases = 0

    for y, line in enumerate(input_lines):
        for x, letter in enumerate(line):
            if letter == "X":
                # Check to the right
                if x + 1 < len(input_lines[y]) and input_lines[y][x + 1] == "M":
                    if x + 2 < len(input_lines[y]) and input_lines[y][x + 2] == "A":
                        if x + 3 < len(input_lines[y]) and input_lines[y][x + 3] == "S":
                            xmases += 1

                # Check to the left (backwards)
                if x - 1 >= 0 and input_lines[y][x - 1] == "M":
                    if x - 2 >= 0 and input_lines[y][x - 2] == "A":
                        if x - 3 >= 0 and input_lines[y][x - 3] == "S":
                            xmases += 1

                # Check down
                if y + 1 < len(input_lines) and input_lines[y + 1][x] == "M":
                    if y + 2 < len(input_lines) and input_lines[y + 2][x] == "A":
                        if y + 3 < len(input_lines) and input_lines[y + 3][x] == "S":
                            xmases += 1

                # Check up (backwards)
                if y - 1 >= 0 and input_lines[y - 1][x] == "M":
                    if y - 2 >= 0 and input_lines[y - 2][x] == "A":
                        if y - 3 >= 0 and input_lines[y - 3][x] == "S":
                            xmases += 1

                # Check diagonal right down
                if y + 1 < len(input_lines) and x + 1 < len(input_lines[y]) and input_lines[y + 1][x + 1] == "M":
                    if y + 2 < len(input_lines) and x + 2 < len(input_lines[y]) and input_lines[y + 2][x + 2] == "A":
                        if (
                            y + 3 < len(input_lines)
                            and x + 3 < len(input_lines[y])
                            and input_lines[y + 3][x + 3] == "S"
                        ):
                            xmases += 1

                # Check diagonal left down (backwards)
                if y + 1 < len(input_lines) and x - 1 >= 0 and input_lines[y + 1][x - 1] == "M":
                    if y + 2 < len(input_lines) and x - 2 >= 0 and input_lines[y + 2][x - 2] == "A":
                        if y + 3 < len(input_lines) and x - 3 >= 0 and input_lines[y + 3][x - 3] == "S":
                            xmases += 1

                # Check diagonal right up
                if y - 1 >= 0 and x + 1 < len(input_lines[y]) and input_lines[y - 1][x + 1] == "M":
                    if y - 2 >= 0 and x + 2 < len(input_lines[y]) and input_lines[y - 2][x + 2] == "A":
                        if y - 3 >= 0 and x + 3 < len(input_lines[y]) and input_lines[y - 3][x + 3] == "S":
                            xmases += 1

                # Check diagonal left up (backwards)
                if y - 1 >= 0 and x - 1 >= 0 and input_lines[y - 1][x - 1] == "M":
                    if y - 2 >= 0 and x - 2 >= 0 and input_lines[y - 2][x - 2] == "A":
                        if y - 3 >= 0 and x - 3 >= 0 and input_lines[y - 3][x - 3] == "S":
                            xmases += 1

    return xmases


def part_2(input_lines):
    """
    Word search for XMAS but in an X of M A S
    """

    xmases = 0

    for y, line in enumerate(input_lines):
        for x, letter in enumerate(line):
            if letter == "A":
                if y + 1 < len(input_lines) and x + 1 < len(input_lines[y]) and y - 1 >= 0 and x - 1 >= 0:
                    if (input_lines[y + 1][x + 1] == "S" and input_lines[y - 1][x - 1] == "M") or (
                        input_lines[y + 1][x + 1] == "M" and input_lines[y - 1][x - 1] == "S"
                    ):
                        if y + 1 < len(input_lines) and x - 1 >= 0 and y - 1 >= 0 and x + 1 < len(input_lines[y]):
                            if (input_lines[y + 1][x - 1] == "M" and input_lines[y - 1][x + 1] == "S") or (
                                input_lines[y + 1][x - 1] == "S" and input_lines[y - 1][x + 1] == "M"
                            ):
                                xmases += 1

    return xmases
